const ethers = require('ethers');
const networks = require('../truffle-config').networks;
const dotenv = require('dotenv');

dotenv.config()

async function main() {
    providerUrl = `http://${networks.development.host}:${networks.development.port}` 
    const web3 = new ethers.providers.JsonRpcProvider(providerUrl);
    const signer = new ethers.Wallet(process.env.WALLET_PRIV_KEY).connect(web3);
    const bouncerContract = new ethers.Contract(process.env.CONTRACT_ADDR, [
      "function bribe() external payable",
      "function get_flag(uint index, uint answer) external view returns(address)"
    ], web3);

    let tx = await bouncerContract.populateTransaction.bribe();
    tx = {
      value: 10001,
      from: signer.address,
      ...tx
    }
    await signer.sendTransaction(tx);


    for (let i=0; i<5; i++) {
        console.log(await bouncerContract.get_flag(i, 0x31337, {from:signer.address}))
    }
}

main()