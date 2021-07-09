import json
import os
import shutil
import hashlib


class Block:
    def __init__(self, base_hash, new_hash, parent_hash):
        self.base_hash = base_hash
        self.hash = new_hash
        self.parent_hash = parent_hash
        self.transactions = []
        self.check_hash()

    def __str__(self):
        return f"base_hash: {self.base_hash}\nhash: {self.hash}\nparent_hash: {self.parent_hash}\ntransactions: {self.transactions}"

    def check_hash(self):
        test_hash = hashlib.sha256(self.base_hash.encode()).hexdigest()
        return self.hash == test_hash

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self.save()

    def get_transaction(self, number):
        for t in self.transactions:
            if t["number"] == number:
                return t
        return None

    def get_weight(self):
        return os.path.getsize(f"./content/blocs/{self.hash}.json")

    def save(self):
        data = {
            'base_hash': self.base_hash,
            'hash': self.hash,
            'parent_hash': self.parent_hash,
            'transactions': []
        }

        for t in self.transactions:
            data['transactions'].append(t)

        if os.path.exists(f"./content/blocs/{self.hash}.json"):
            main_file = r"./content/blocs/"+self.hash+".json"
            backup_file = r"./content/blocs/"+self.hash+"_backup.json"
            shutil.copyfile(main_file, f"./content/blocs/{self.hash}_backup.json")
            os.system(f"attrib +h {backup_file}")
            with open(main_file, "w") as file:
                json.dump(data, file)

            if self.get_weight() >= 256000:
                os.remove(main_file)
                os.rename(backup_file, main_file)
                os.system(f"attrib -h {main_file}")
                return "The file exceed the maximum authorized length"
            else:
                os.remove(backup_file)
                return True
        else:
            main_file = f"./content/blocs/{self.hash}.json"
            with open(main_file, "w") as file:
                json.dump(data, file)
            return True

    def load(self):
        with open(f"./content/blocs/{self.hash}.json") as file:
            data = json.load(file)
            self.base_hash = data["base_hash"]
            self.hash = data["hash"]
            self.parent_hash = data["parent_hash"]
            self.transactions = data["transactions"]
