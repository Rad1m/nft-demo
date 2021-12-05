from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "hardhat",
    "local-ganache",
    "mainnet-fork",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(accounts[0].balance())
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


##################################################
### THIS IS TO PRINT COLORFUL TEXT IN TERMINAL ###
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


############## END OF COLORS ####################
