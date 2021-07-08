import json
import os


class Block:
    def __init__(self, base_hash, new_hash, parent_hash):
        self.base_hash = base_hash
        self.hash = new_hash
        self.parent_hash = parent_hash
        self.transactions = []

    def check_hash(self):
        pass

    def add_transaction(self):
        pass

    def get_transaction(self):
        pass

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

        with open(f"./content/blocs/{self.hash}.json", "w") as file:
            json.dump(data, file)

    def load(self):
        with open(f"./content/blocs/{self.hash}.json") as file:
            data = json.load(file)
            self.base_hash = data["base_hash"]
            self.hash = data["hash"]
            self.parent_hash = data["parent_hash"]
            self.transactions = data["transactions"]
