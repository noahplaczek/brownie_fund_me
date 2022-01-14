from brownie import accounts, network, config

# based on the type of environment, will pull in the appropriate accounts
def get_account():
    if network.show_active() == "development": # brownie run scripts/deploy.py
        return
    else: # brownie run scripts/deploy.py --network rinkeby
        return accounts.add(config["wallets"]["from_key"])

# DONT FORGET TO ADD IN YAML AND CREATE .env
# dotenv: .env
# wallets: 
#  from_key: ${PRIVATE_KEY}