import { ethers } from "hardhat";

async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contract with account:", deployer.address);
    const ConversionPayment = await ethers.getContractFactory("ConversionPayment");

    // Set your desired conversion fee here
    const conversionFee = ethers.parseEther("0.01"); // e.g., 0.01 ETH

    const contract = await ConversionPayment.deploy(conversionFee);
    console.log(`contract deployed to ${contract.target}`);;

}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error(error);
        process.exit(1);
    });
