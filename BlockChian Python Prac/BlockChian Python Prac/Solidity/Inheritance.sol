pragma solidity ^0.5.0;
contract C {
// Private state variable
uint private data;
// Public state variable
uint public info;
// Constructor
constructor() public {
info = 10;
}
// Private function
function increment(uint a) private pure returns (uint) {
return a + 1;
}
// Public function
function updateData(uint a) public {
data = a;
}
function getData() public view returns (uint) {
return data;
}
function compute(uint a, uint b) internal pure returns (uint) {
return a + b;
}
}
// External Contract
contract D {
function readData() public returns (uint) {
C c = new C();
c.updateData(7);
return c.getData();
}
}
// Derived Contract
contract E is C {
uint private result;
C private c;
constructor() public {
c = new C();
}
function getComputedResult() public {
result = compute(3, 5);
}
function getResult() public view returns (uint) {
return result;}
function getData() public view returns (uint) {
return c.info();
}
}