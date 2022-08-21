// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Bouncer {
  address[5] private theFlags;
  mapping (address => bool) public friends;
  address public owner;

  constructor(address[] memory flags) {
    require(theFlags.length == flags.length, "Constructor flags bad length");
    for (uint i=0; i < flags.length; i++) {
      theFlags[i] = flags[i];
    }
    owner = msg.sender;
  }

  modifier onlyOwner {
    require(msg.sender == owner, "Only owner is allowed to perform this action");
    _;
  }

  function bribe() external payable  {
    if (msg.value > 10000) {
      friends[msg.sender] = true;
    }
  }

  function get_flag(uint index, uint answer) external view returns(address) {
    require(index < theFlags.length, "We don't have so many flags");
    if (answer == 0x31337 && friends[msg.sender]) {
      return theFlags[index];
    }
    return address(0);
  }

  function withdraw(address payable _to, uint amount) public onlyOwner {
    _to.transfer(amount);
  }
}
