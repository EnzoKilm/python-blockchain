import uuid
import os
import json


class Wallet:
    def __init__(self):
        self.unique_id = self.generate_unique_id()
        self.balance = 0
        self.history = []

    def generate_unique_id(self):
        wallet_uuid = uuid.uuid4()

        if os.path.exists(f"./content/wallets/{wallet_uuid}.json"):
            return self.generate_unique_id()
        else:
            self.save()

            return wallet_uuid

    def add_balance(self, value):
        self.balance += value

    def sub_balance(self, value):
        self.balance -= value

    def send(self):
        pass

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
        with open(f"./content/wallets/{self.unique_id}.json") as file:
            data = json.load(file)
            self.unique_id = data["unique_id"]
            self.balance = data["balance"]
            self.history = data["history"]