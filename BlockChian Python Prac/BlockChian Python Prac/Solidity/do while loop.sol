pragma solidity ^0.5.0;
// Creating a contract
contract Types {
// Declaring a dynamic array
uint[] data;
// Declaring state variable
uint8 j = 0;
// Defining a function to demonstrate 'Do-While loop'
function loop() public returns (uint[5] memory) {
do {
j++;
data.push(j);
} while (j < 5);
return data;
}
}