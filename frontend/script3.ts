import { BrowserProvider, ethers } from "ethers";


declare global {
    interface Window {
      ethereum?: {
        isMetaMask: boolean;
        request: (args: { method: string; params?: any[] }) => Promise<any>;
      };
    }
  }

// Replace with your deployed contract address
const contractAddress = "0x5c83A58eE57982b784d06e8d8e879435f6301be4"; // Your deployed contract address

// Define the ABI of the contract
const abi = [
    {
        "anonymous": false,
        "inputs": [
          {
            "indexed": true,
            "internalType": "address",
            "name": "sender",
            "type": "address"
          },
          {
            "indexed": false,
            "internalType": "string",
            "name": "message",
            "type": "string"
          }
        ],
        "name": "Conversion",
        "type": "event"
      },
      {
        "inputs": [
          {
            "internalType": "string",
            "name": "_message",
            "type": "string"
          }
        ],
        "name": "convert",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      }
];

let contract: ethers.Contract;

async function initializeContract() {
    if (typeof window.ethereum !== 'undefined') {
        // Request account access
        const provider = new BrowserProvider(window.ethereum);
        const signer = provider.getSigner();

        // Initialize the contract
        contract = new ethers.Contract(contractAddress, abi, await signer);
    } else {
        alert("Please install MetaMask!");
    }
}

async function convertMessage() {
    const messageElement = document.getElementById("containerText") as HTMLElement;
    const message = messageElement.innerText;

    if (message) {
        try {
            const tx = await contract.convert(message);
            await tx.wait(); // Wait for the transaction to be mined
            alert("Conversion successful!");
        } catch (error) {
            console.error("Error during conversion:", error);
        }
    } else {
        alert("No message to convert!");
    }
}

// Event listener for the "Convert" button
document.getElementById("convert")!.addEventListener("click", async () => {
    await convertMessage();
});

// Call initializeContract when the page loads
window.addEventListener("load", async () => {
    await initializeContract();
});
