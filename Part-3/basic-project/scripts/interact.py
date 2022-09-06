from Brownie import BasicContract, accounts


def main():
    # Accessing the latest deployment instance
    contract_instance = BasicContract[-1]
    # loading the stored account
    account = accounts.load("my-new-account")
    # storing a number
    transaction_receipt = contract_instance.storeNumber(15, {"from": account})
    # Wait for transaction confirmation
    print(transaction_receipt)
    # Retrieve the number
    retrieved_number = contract_instance.readNumber()
    # Print the retrieved number
    print(f"Number Retrieved: {retrieved_number}")
