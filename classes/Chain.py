import hashlib
import string
import random
from Block import Block
from Wallet import Wallet
import sys


class Chain:
    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0

    def generate_hash(self):
        letters = string.ascii_lowercase
        index = random.randint(1, 51)

        random_string = ''
        for i in range(index):
            random_string = random_string.join(random.choice(letters))

        new_hash = hashlib.sha256(random_string.encode()).hexdigest()

        if self.verify_hash(new_hash):
            if self.add_block(random_string, new_hash) is False:
                return "The hash does not match to the string given."
            else:
                return "Block successfully created."
        else:
            self.generate_hash()

    def verify_hash(self, hash_to_verify):
        if hash_to_verify[0:4] != "0000":
            return False

        for b in self.blocks:
            if b.hash == hash_to_verify:
                return False

        return True

    def add_block(self, random_string, new_hash):
        if len(self.blocks) < 1:
            parent_hash = "00"
        else:
            parent_hash = self.blocks[len(self.blocks) - 1].hash

        block = Block(random_string, new_hash, parent_hash)
        if block is not False:
            block.save()
            self.blocks.append(block)
            return True
        else:
            return False

    def get_block(self, block_hash):
        for b in self.blocks:
            if b.hash == block_hash:
                return b

        return None

    def add_transaction(self, transmitter_uuid, receiver_uuid, amount, date):
        transmitter = Wallet(transmitter_uuid)
        if transmitter is not False:
            receiver = Wallet(receiver_uuid)
            if receiver is not False:
                last_block = self.blocks[len(self.blocks) - 1]

                transaction = {
                    'number': self.last_transaction_number + 1,
                    'transmitter': transmitter_uuid,
                    'receiver': receiver_uuid,
                    'amount': amount,
                    'date': date
                }
                if sys.getsizeof(transaction) + last_block.get_weight() <= 256000:
                    result = last_block.add_transaction(transaction)
                    if result is not True:
                        return False
                    else:
                        transmitter.sub_balance(transaction)
                        receiver.add_balance(transaction)
                        self.last_transaction_number += 1
                        return True
                else:
                    return False

    def find_transaction(self, number):
        for b in self.blocks:
            for t in b.transactions:
                if t.number == number:
                    return b

        return None

    def get_last_transaction_number(self):
        return self.last_transaction_number
