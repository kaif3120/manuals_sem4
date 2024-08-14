// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract EtherUnitsExample {
    // State variable to store balances
    mapping(address => uint256) public balances;

    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);
    
    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount);

    // Function to deposit ether into the contract
    function deposit() public payable {
        // Update the balance of the sender
        balances[msg.sender] += msg.value;

        // Emit a deposit event
        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw ether from the contract
    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the balance of the sender
        balances[msg.sender] -= _amount;

        // Emit a withdrawal event
        emit Withdrawn(msg.sender, _amount);

        // Transfer ether to the sender
        msg.sender.transfer(_amount);
    }

    // Function to get the contract's balance in ether
    function getContractBalanceInEther() public view returns (uint256) {
        return address(this).balance / 1 ether;
    }
    
    // Function to get the balance of a user in ether
    function getUserBalanceInEther(address _user) public view returns (uint256) {
        return balances[_user] / 1 ether;
    }
}
