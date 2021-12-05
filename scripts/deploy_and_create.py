from scripts.helpful_scripts import get_account, bcolors
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/QmTtqvbKp4E67Dhs1jvS36v2ELk4coxGgsHGc9z7RuHa2f?filename=Alfie.png"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"{bcolors.OKGREEN}\nAmazing, the NFT is available at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}{bcolors.ENDC}"
    )
    print(
        f"{bcolors.WARNING}\nPlease wait up to 20 minutes for the NFT to become available online{bcolors.ENDC}\n"
    )
