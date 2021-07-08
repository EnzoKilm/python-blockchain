from classes.Wallet import Wallet
from classes.Chain import Chain
import sys


def main():
    chain = Chain()
    result = chain.generate_hash()
    print(result)

    wallet1 = Wallet()
    print("Wallet 1: ", wallet1.unique_id, wallet1.balance)
    wallet2 = Wallet()
    print("Wallet 2: ", wallet2.unique_id, wallet2.balance)

    chain.add_transaction(wallet1.unique_id, wallet2.unique_id, 70)
    print("Wallet 1: ", wallet1.balance)
    print("Wallet 2: ", wallet2.balance)

    print(chain.blocks)
    print(chain.last_transaction_number())
    print(chain.find_transaction(1))


if __name__ == "__main__":
    sys.setrecursionlimit(50000)

    main()
