pragma solidity ^0.5.0;

contract ConstructorExample {
    address public owner;
    uint256 public initialSupply;
    string public name;
    string public symbol;

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, string memory _name, string memory _symbol) public {
        owner = msg.sender; // Set the contract creator as the owner
        initialSupply = _initialSupply; // Set the initial supply of tokens
        name = _name; // Set the name of the token
        symbol = _symbol; // Set the symbol of the token
    }

    // Function to get the owner address
    function getOwner() public view returns (address) {
        return owner;
    }

    // Function to get the initial supply
    function getInitialSupply() public view returns (uint256) {
        return initialSupply;
    }

    // Function to get the name of the token
    function getName() public view returns (string memory) {
        return name;
    }

    // Function to get the symbol of the token
    function getSymbol() public view returns (string memory) {
        return symbol;
    }
}
