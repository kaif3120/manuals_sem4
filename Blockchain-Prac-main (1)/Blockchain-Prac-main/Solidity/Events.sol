// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract EventExample {

    // Declare an event
    event DataStored(address indexed sender, uint256 value);

    // State variable to store data
    uint256 public storedData;

    // Function to store data and emit an event
    function storeData(uint256 _value) public {
        storedData = _value;

        // Emit the event with parameters
        emit DataStored(msg.sender, _value);
    }
}
