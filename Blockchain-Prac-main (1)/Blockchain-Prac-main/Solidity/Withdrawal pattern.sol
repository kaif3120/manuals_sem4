// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract WithdrawalExample {
    // Mapping to keep track of user balances
    mapping(address => uint256) public balances;

    // Event to log withdrawals
    event Withdrawal(address indexed user, uint256 amount);

    // Function to deposit ether into the contract
    function deposit() public payable {
        // Increase the user's balance
        balances[msg.sender] += msg.value;
    }

    // Function to withdraw ether from the contract
    function withdraw(uint256 _amount) public {
        // Check if the user has enough balance
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= _amount;

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, _amount);

        // Transfer the ether to the user
        msg.sender.transfer(_amount);
    }

    // Function to check the balance of the contract
    function contractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
