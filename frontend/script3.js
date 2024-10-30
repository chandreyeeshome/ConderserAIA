// const ethers = require('ethers'); // Ensure ethers.js is imported if needed
// const convertButton = document.getElementById("convert");

// const contractAddress = "0xe14fB6a80ca5F5fd7F861Fa71Cf558835a531648";
// const contractABI = [ 
//     {
//         "inputs": [
//           {
//             "internalType": "uint256",
//             "name": "_conversionFee",
//             "type": "uint256"
//           }
//         ],
//         "stateMutability": "nonpayable",
//         "type": "constructor"
//       },
//       {
//         "anonymous": false,
//         "inputs": [
//           {
//             "indexed": true,
//             "internalType": "address",
//             "name": "user",
//             "type": "address"
//           },
//           {
//             "indexed": false,
//             "internalType": "uint256",
//             "name": "amount",
//             "type": "uint256"
//           }
//         ],
//         "name": "ConversionPaid",
//         "type": "event"
//       },
//       {
//         "inputs": [],
//         "name": "conversionFee",
//         "outputs": [
//           {
//             "internalType": "uint256",
//             "name": "",
//             "type": "uint256"
//           }
//         ],
//         "stateMutability": "view",
//         "type": "function"
//       },
//       {
//         "inputs": [],
//         "name": "owner",
//         "outputs": [
//           {
//             "internalType": "address",
//             "name": "",
//             "type": "address"
//           }
//         ],
//         "stateMutability": "view",
//         "type": "function"
//       },
//       {
//         "inputs": [],
//         "name": "payForConversion",
//         "outputs": [],
//         "stateMutability": "payable",
//         "type": "function"
//       },
//       {
//         "inputs": [
//           {
//             "internalType": "uint256",
//             "name": "_fee",
//             "type": "uint256"
//           }
//         ],
//         "name": "setConversionFee",
//         "outputs": [],
//         "stateMutability": "nonpayable",
//         "type": "function"
//       },
//       {
//         "inputs": [],
//         "name": "withdraw",
//         "outputs": [],
//         "stateMutability": "nonpayable",
//         "type": "function"
//       }
// ];

// async function payForConversion() {
//     // console.log("----------------------------------------------")
//     // if (typeof window.ethereum !== 'undefined') {
//     //     try {
//             console.log("Connecting to provider...");
//             const provider = new ethers.providers.Web3Provider(window.ethereum);
//             const signer = provider.getSigner();
//             const contract = new ethers.Contract(contractAddress, contractABI, signer);
            
//             console.log("Retrieving conversion fee...");
//             const conversionFee = await contract.conversionFee();
//             console.log("Conversion Fee:", ethers.utils.formatEther(conversionFee), "ETH");

//             console.log("Sending transaction...");
//             const tx = await contract.payForConversion({
//                 value: conversionFee
//             });
            
//             console.log("Transaction sent:", tx);
//             await tx.wait(); 
//             console.log("Transaction mined:", tx);

//             alert("Payment successful. Starting conversion...");
//             // Trigger conversion logic here

//     //     } catch (error) {
//     //         console.error("Payment failed:", error);
//     //         alert("Transaction failed. Check console for details.");
//     //     }
//     // } else {
//     //     alert("Please install MetaMask!");
//     }
// // }


// convertButton.addEventListener("click", payForConversion);
