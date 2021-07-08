import uuid
import os


class Wallet:
    def __init__(self):
        self.unique_id = self.generate_unique_id()

    def generate_unique_id(self):
        wallet_uuid = uuid.uuid4()
        return self.check_unique_id(wallet_uuid)

    def check_unique_id(self, wallet_uuid):
        if os.path.exists(f"./content/wallets/{wallet_uuid}.json"):
            return self.generate_unique_id()
        else:
            f = open(f"./content/wallets/{wallet_uuid}.json", "w")
            f.close()

            return wallet_uuid
