// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BasicContract {
    //a variable for storing numbers
    uint256 number;
    address owner;
    //constructor
    constructor() {
        owner = msg.sender;
    }

    //function for storing a number
    function storeNumber(uint256 _number) public {
        number = _number;
    }

    //function for reading the number
    function readNumber() public view isOwner returns (uint256) {
        return number;
    }

    modifier isOwner() {
        require(owner == msg.sender);
        _;
    }
}
