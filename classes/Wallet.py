import uuid
import os
import json


class Wallet:
    def __init__(self, unique_id=None):
        if unique_id is None:
            self.unique_id = self.generate_unique_id()
            self.balance = 100
            self.history = []
        else:
            self.unique_id = unique_id
            if self.load() is False:
                return False

    def generate_unique_id(self):
        wallet_uuid = uuid.uuid4()

        if os.path.exists(f"./content/wallets/{wallet_uuid}.json"):
            return self.generate_unique_id()
        else:
            self.save()

            return wallet_uuid

    def add_balance(self, transaction):
        self.balance += transaction["value"]
        self.send(transaction)

    def sub_balance(self, transaction):
        self.balance -= transaction["value"]
        self.send(transaction)

    def send(self, transaction):
        self.history.append({
            'type': 'send',
            'amount': transaction["value"],
            'transmitter': transaction["transmitter_uuid"],
            'receiver': transaction["receiver_uuid"],
            'date': transaction["date"],
            'transaction': transaction["number"]
        })

    def save(self):
        data = {
            'unique_id': self.unique_id,
            'balance': self.balance,
            'history': []
        }

        for h in self.history:
            data['history'].append(h)

        with open(f"./content/wallets/{self.unique_id}.json", "w") as file:
            json.dump(data, file)

    def load(self):
        if os.path.exists(f"./content/wallets/{self.unique_id}.json"):
            with open(f"./content/wallets/{self.unique_id}.json") as file:
                data = json.load(file)
                self.unique_id = data["unique_id"]
                self.balance = data["balance"]
                self.history = data["history"]

            return True
        else:
            return False
