pragma solidity ^0.5.0;

contract SolidityTest {
    uint storedData; // State variable

    // Constructor to initialize storedData
    constructor() public {
        storedData = 10;
    }

    // Function to find the maximum of three numbers and return it as a string
    // Marked as `pure` since it does not read or modify any state variables
    function getResult() public pure returns (string memory) {
        uint a = 1;
        uint b = 2;
        uint c = 3;
        uint result;

        // if-else statement to find the maximum number
        if( a > b && a > c) {
            result = a;
        } else if( b > a && b > c ) {
            result = b;
        } else {
            result = c;
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
