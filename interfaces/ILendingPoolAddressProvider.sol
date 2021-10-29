// SPDX-License-Identified: MIT
pragma solidity 0.8.7;

interface ILendingPoolAddressProvider {
    function getLendingPool() external view returns (address);
}
