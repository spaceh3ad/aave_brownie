from brownie import network, config, interface
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth


def main():
    accounts = get_account()
    print(accounts)
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    lending_pool = get_lending_pool()
    print(lending_pool)


def get_lending_pool():
    lending_pool_addreses_provider = interface.ILendingPoolAddressProvider(
        config["networks"][network.show_active()["lending_pool_address_provider"]]
    )
    lending_pool_address = lending_pool_addreses_provider.getLendingPool()

    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
