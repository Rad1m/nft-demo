from scripts.helpful_scripts import get_account, bcolors, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/QmTtqvbKp4E67Dhs1jvS36v2ELk4coxGgsHGc9z7RuHa2f"

def deploy_and_create():
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
    return simple_collectible

def main():
    deploy_and_create()