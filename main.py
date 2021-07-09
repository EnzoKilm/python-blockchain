from classes.Wallet import Wallet
from classes.Chain import Chain


def main():
    wallet_1 = Wallet()
    print("\nWallet 1: ", wallet_1.unique_id, wallet_1.balance)
    wallet_2 = Wallet()
    print("Wallet 2: ", wallet_2.unique_id, wallet_2.balance)

    chain = Chain()
    result = chain.generate_hash()
    print(result)

    chain.add_transaction(wallet_1.unique_id, wallet_2.unique_id, 70)
    wallet_1.load()
    wallet_2.load()

    print("\nWallet 1: ", wallet_1.balance)
    print("Wallet 2: ", wallet_2.balance)

    print(f"\nLast transaction number: {chain.get_last_transaction_number()}")

    print(f"\n{chain.find_transaction(1)}")

    result = chain.generate_hash(wallet_2)
    print(result)
    print(f"New wallet 2 balance: {wallet_2.balance}")

    for b in chain.blocks:
        print(f"\n{b}")


if __name__ == "__main__":
    main()
