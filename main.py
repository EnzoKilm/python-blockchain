from classes.Wallet import Wallet
from classes.Chain import Chain

if __name__ == "__main__":
    chain = Chain()
    result = chain.generate_hash()

    print(result)