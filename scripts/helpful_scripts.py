from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

# based on the type of environment, will pull in the appropriate accounts
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
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
            STARTING_PRICE,
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
