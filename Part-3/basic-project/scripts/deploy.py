from Brownie import BasicContract, accounts


def main():
    # Fetch already stored account
    account = accounts.load('my-new-account')
    # deploy contract
    deploy_contract = BasicContract.deploy({"from": account})
    # print contract address
    print(f"contract deployed at {deploy_contract}")
