from scripts.helpful_scripts import get_account
from scripts.deploy_fund_me import deploy_fund_me, LOCAL_BLOCKCHAIN_ENV
from brownie import FundMe, accounts, network, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    deploy_fund_me()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.adressToAmount(account) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.adressToAmount(account) == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("only for local testing")
    account = get_account()
    deploy_fund_me()
    fund_me = FundMe[-1]
    bad_account = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
      fund_me.withdraw({"from": bad_account})



