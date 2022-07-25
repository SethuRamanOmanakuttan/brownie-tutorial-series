from brownie import BasicContract , accounts 

def main():
    # fetch the account
    account = accounts[0]
    # deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    # print contract address
    print(f"contract deployed at {deploy_contract}")
    # store a number
    transaction_receipt = deploy_contract.storeNumber(15,{"from":account})
    # wait for transaction confirmation
    transaction_receipt.wait(1)
    # retrieve the number
    retrieved_number = deploy_contract.readNumber()
    # print the retrieved number
    print(f"Number Retrieved : {retrieved_number}")