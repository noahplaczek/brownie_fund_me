from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    print(account)
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mocks deployed!")
    # public_source=True: allows us to verify our code in etherscan
    # need the api setup in .env to do this
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )


def main():
    deploy_fund_me()
