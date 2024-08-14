pragma solidity ^0.5.0;

contract SolidityTest {

    // Constructor
    constructor() public {
        // No initialization needed in this example
    }

    // Function to perform addition and return the result as a string
    // Marked as `pure` since it does not interact with state variables
    function getResult() public pure returns (string memory) {
        uint a = 1;
        uint b = 2;
        uint result = a + b;
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
