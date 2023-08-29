from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account, deploy_mock_v3_aggregator, LOCAL_BLOCKCHAIN_ENV, FORK_BLOCKCHAIN_ENV


def deploy_fund_me():
  account = get_account()
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
    price_feed_adress = config["networks"][network.show_active()]["eth_usd_price_feed_adress"]
  else:
    price_feed_adress = deploy_mock_v3_aggregator()
  fund_me = FundMe.deploy(price_feed_adress,{"from":account},publish_source=config["networks"][network.show_active()].get("verify"))
  print(fund_me)



def main():
  deploy_fund_me()