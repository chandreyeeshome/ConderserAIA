// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ConversionPayment {
    address public owner;
    uint256 public conversionFee;

    event ConversionPaid(address indexed user, uint256 amount);

    constructor(uint256 _conversionFee) {
        owner = msg.sender;
        conversionFee = _conversionFee;
    }

    function payForConversion() external payable {
        require(msg.value >= conversionFee, "Insufficient funds for conversion fee");
        emit ConversionPaid(msg.sender, msg.value);
    }

    function setConversionFee(uint256 _fee) external {
        require(msg.sender == owner, "Only owner can set the fee");
        conversionFee = _fee;
    }

    function withdraw() external {
        require(msg.sender == owner, "Only owner can withdraw funds");
        payable(owner).transfer(address(this).balance);
    }
}
