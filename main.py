from classes.Wallet import Wallet
from classes.Chain import Chain
import sys


def main():
    wallet1 = Wallet()
    print("\nWallet 1: ", wallet1.unique_id, wallet1.balance)
    wallet2 = Wallet()
    print("Wallet 2: ", wallet2.unique_id, wallet2.balance)

    chain = Chain()
    result = chain.generate_hash()
    print(result)

    chain.add_transaction(wallet1.unique_id, wallet2.unique_id, 70)
    wallet1.load()
    wallet2.load()

    print("\nWallet 1: ", wallet1.balance)
    print("Wallet 2: ", wallet2.balance)

    for b in chain.blocks:
        print(f"\n{b}")

    print(f"\nLast transaction number: {chain.get_last_transaction_number()}")

    print(f"\n{chain.find_transaction(1)}")

    result = chain.generate_hash()
    print(result)


if __name__ == "__main__":
    sys.setrecursionlimit(999999999)

    main()
