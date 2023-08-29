from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    fund_me.fund({"from": account, "value": entrance_fee})
    print(entrance_fee)

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})



def main():
    fund()
    #withdraw()