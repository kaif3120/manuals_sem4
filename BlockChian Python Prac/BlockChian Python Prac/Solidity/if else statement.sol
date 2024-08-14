pragma solidity ^0.5.0;

contract SolidityTest {
    uint storedData;

    // Constructor to initialize storedData
    constructor() public {
        storedData = 10;
    }

    // Function to demonstrate if-else statement and return the result as a string
    // Marked as `pure` since it does not read or modify any state variables
    function getResult() public pure returns (string memory) {
        uint a = 1;
        uint b = 2;
        uint result;
        if(a > b) { // if else statement
            result = a;
        }
        else {
            result = b;
        }
        return integerToString(result);
    }

    // Function to convert an integer to a string
    function integerToString(uint _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint j = _i;
        uint len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint k = len - 1;
        while (_i != 0) {
            bstr[k--] = bytes1(uint8(48 + _i % 10));
            _i /= 10;
        }
        return string(bstr);
    }
}
