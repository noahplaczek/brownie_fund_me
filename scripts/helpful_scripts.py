from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000

# based on the type of environment, will pull in the appropriate accounts
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    # if we already have a mock deployed to our network, we don't need a new mock
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(
            DECIMALS,
            # toWei will add 18 decimals and make our 2,000 more readable
            Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account()},
        )
        print("Mocks deployed!")
    else:
        print("Mocks already deployed")


# DONT FORGET TO ADD IN YAML AND CREATE .env
# dotenv: .env
# wallets:
#  from_key: ${PRIVATE_KEY}

# .env
# export PRIVATE_KEY=
# export WEB3_INFURA_PROJECT_ID=
# export ETHERSCAN_TOKEN=
