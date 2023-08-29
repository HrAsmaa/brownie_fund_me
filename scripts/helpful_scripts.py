from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
FORK_BLOCKCHAIN_ENV = ["mainnet-fork-dev"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV or network.show_active() in FORK_BLOCKCHAIN_ENV:
        print("get account 0")
        return accounts [0]
    else:
        print("get account from wallet")
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mock_v3_aggregator():
    if len(MockV3Aggregator)<=0:
          print("deploy mock")
          MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    return MockV3Aggregator[-1].address