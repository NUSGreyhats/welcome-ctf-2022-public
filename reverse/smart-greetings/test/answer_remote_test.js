const ethers = require('ethers');
const networks = require('../truffle-config').networks;
const dotenv = require('dotenv');

dotenv.config()

async function main() {
    providerUrl = `https://eth-goerli.g.alchemy.com/v2/qqwGGHy-HABTtpsSDM7WOZkAn_bnaFe0`;
    const web3 = new ethers.providers.JsonRpcProvider(providerUrl);
    const signer = new ethers.Wallet(process.env.REMOTE_WALLET_PRIV_KEY).connect(web3);
    const bouncerContract = new ethers.Contract(process.env.REMOTE_CONTRACT_ADDR, [
      "function bribe() external payable",
      "function get_flag(uint index, uint answer) external view returns(address)"
    ], web3);

    // let tx = await bouncerContract.populateTransaction.bribe();
    // tx = {
    //   value: 10001,
    //   from: signer.address,
    //   ...tx
    // }
    // let res = await signer.sendTransaction(tx);
    // console.log(res.wait());
    for (let i=0; i<5; i++) {
        console.log(await bouncerContract.get_flag(i, 0x31337, {from:signer.address}))
    }
}

main()