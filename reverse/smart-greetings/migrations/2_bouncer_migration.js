const Bouncer = artifacts.require("Bouncer");

module.exports = function (deployer) {
    const contract = deployer.deploy(Bouncer, [
        "0x6e6576657220676f6e6e61206769622075207570",
        "0x6e6576657220676f6e6e61206769622075207570",
        "0x67726579686174737b5930755f6172335f615f53",
        "0x6d3472745f503372736f6e7d0000000000000000",
        "0x6e6576657220676f6e6e61206769622075207570",
    ]);
    console.log(contract)
};
