// SPDX-License-Identifier: MIT
// SPDX-License-Identifier: MIT
// Solidity program to demonstrate
// Assignment Operator
pragma solidity ^0.5.0;

// Creating a contract
contract SolidityTest {
    uint16 public assignment = 20;
    uint assignment_add = 50;
    uint assign_sub = 50;
    uint assign_mul = 10;
    uint assign_div = 50;
    uint assign_mod = 32;

    // Defining function to
    // demonstrate Assignment Operator
    function getResult() public {
        assignment_add += 10;
        assign_sub -= 20;
        assign_mul *= 10;
        assign_div /= 10;
        assign_mod %= 20;
    }
}
