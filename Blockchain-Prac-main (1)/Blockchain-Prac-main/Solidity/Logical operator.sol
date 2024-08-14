// SPDX-License-Identifier: MIT
// Solidity program to demonstrate Logical Operators
pragma solidity ^0.5.0;
// Creating a contract
contract LogicalOperator {
// Defining function to demonstrate Logical operators
function logic(bool a, bool b) public pure returns (bool, bool, bool) {
// Logical AND operator
bool andResult = a && b;
// Logical OR operator
bool orResult = a || b;
// Logical NOT operator
bool notResult = !a;
return (andResult, orResult, notResult);
}
}