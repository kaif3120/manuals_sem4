pragma solidity ^0.5.0;
contract SolidityTest {
function sub(uint a, uint b) public pure returns (uint) {
uint result = (a > b) ? a - b : b - a;
return result;
}
}
