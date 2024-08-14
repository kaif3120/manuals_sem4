pragma solidity ^0.5.0;

// Interface defining the getResult function
interface Calculator {
    function getResult() external view returns (uint);
}

// Contract implementing the Calculator interface
contract Test is Calculator {
    // Constructor (not strictly necessary in this simple case, but included for completeness)
    constructor() public {}

    // Implementation of the getResult function from the Calculator interface
    function getResult() external view returns (uint) {
        uint a = 1;
        uint b = 2;
        uint result = a + b;
        return result;
    }
}
