import hashlib
import string
import random
from Block import Block


class Chain:
    def __init__(self):
        self.blocs = []
        self.last_transaction_number = None

    def generate_hash(self):
        letters = string.ascii_lowercase
        index = random.randint(1, 51)

        random_string = ''
        for i in range(index):
            random_string = random_string.join(random.choice(letters))

        new_hash = hashlib.sha256(random_string.encode()).hexdigest()

        if self.verify_hash(new_hash):
            self.add_block(random_string, new_hash)
        else:
            self.generate_hash()

    def verify_hash(self, hash_to_verify):
        if hash_to_verify[0:4] != "0000":
            return False

        for b in self.blocs:
            if b.hash == hash_to_verify:
                return False

        return True

    def add_block(self, random_string, new_hash):
        parent_hash = self.blocs[len(self.blocs) - 1].hash
        bloc = Block(random_string, new_hash, parent_hash)
        bloc.save()
        self.blocs.append(bloc)

    def get_block(self, block_hash):
        for b in self.blocs:
            if b.hash == block_hash:
                return b

        return None

    def add_transaction(self, block):
        pass
