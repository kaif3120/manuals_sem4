pragma solidity ^0.5.0;

contract Test {
    // Function to calculate product and sum of two numbers
    // Marked as `pure` since it does not interact with state variables
    function getResult() public pure returns (uint product, uint sum) {
        uint a = 1; // local variable
        uint b = 2;
        product = a * b;
        sum = a + b;
    }
}
