const Bouncer = artifacts.require("Bouncer");
// import { ethers } from 'ethers';
const ethers = require('ethers');
const networks = require('../truffle-config').networks;
const dotenv = require('dotenv');

dotenv.config()


/*
 * uncomment accounts to access the test accounts made available by the
 * Ethereum client
 * See docs: https://www.trufflesuite.com/docs/truffle/testing/writing-tests-in-javascript
 */
contract("Bouncer", function (/* accounts */) {
  it("should return flag", async function () {
    const bouncer = await Bouncer.deployed();
    providerUrl = `http://${networks.development.host}:${networks.development.port}` 
    const web3 = new ethers.providers.JsonRpcProvider(providerUrl);
    assert(process.env.WALLET_PRIV_KEY)
    const signer = new ethers.Wallet(process.env.WALLET_PRIV_KEY).connect(web3);
    const bouncerContract = new ethers.Contract(bouncer.address, [
      "function bribe() external payable",
      "function get_flag(uint index, uint answer) external view returns(address)"
    ]);

    let tx = await bouncerContract.populateTransaction.bribe();
    tx = {
      value: 10001,
      ...tx
    }
    let res = await signer.sendTransaction(tx);
    await res.wait();
    console.log(await bouncer.get_flag(1, 0x31337))
    return assert.isTrue(true);
  });
});
