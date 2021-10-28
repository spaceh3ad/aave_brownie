from scripts.helpful_scripts import get_account
from brownie import interface, network, config


def main():
    get_weth()


def get_weth():
    """Mints WETH by deposiyting ETH."""
    accounts = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_roken"])
    tx = weth.deposit({"from": accounts[0], "value": 0.1 * 10 ** 18})
    print(f"Received 0.1 WETH")
    return tx
