pragma solidity ^0.5.0;

contract SpecialVariablesExample {
    address public owner;
    uint256 public contractCreationTime;
    
    // State variable to store deposited ether amounts
    mapping(address => uint256) public balances;
    
    // Event to log deposit actions
    event Deposited(address indexed user, uint256 amount);

    constructor() public {
        owner = msg.sender; // Set the contract creator as the owner
        contractCreationTime = block.timestamp; // Set the creation time of the contract
    }

    // Function to deposit ether into the contract
    function deposit() public payable {
        require(msg.value > 0, "Must send ether");
        balances[msg.sender] += msg.value; // Update the sender's balance
        emit Deposited(msg.sender, msg.value);
    }

    // Function to get the contract's balance in ether
    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }

    // Function to check if the contract has been active for more than a given number of seconds
    function hasContractBeenActiveFor(uint256 _seconds) public view returns (bool) {
        return (block.timestamp - contractCreationTime) > _seconds;
    }

    // Function to get the sender's balance in ether
    function getUserBalanceInEther(address _user) public view returns (uint256) {
        return balances[_user] / 1 ether;
    }

    // Function to get the block number
    function getBlockNumber() public view returns (uint256) {
        return block.number;
    }
}
