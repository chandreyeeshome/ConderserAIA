# ConderserAIA

**ConderserAIA** is an innovative tool that combines audio recording, speech-to-text conversion, and blockchain technology to streamline interaction with smart contracts on the **AIA Chain**. With every audio conversion, ConderserAIA automatically deploys a smart contract, making it a unique and valuable addition to the AIA blockchain ecosystem.

### Key Features

- **Audio Recording**: Records audio input directly from the user's device.
- **Speech-to-Text Conversion**: Converts recorded audio into text with high accuracy.
- **Automated Smart Contract Deployment**: Deploys a new smart contract on the AIA chain for each successful audio-to-text conversion.
- **Blockchain Compatibility**: Designed specifically to work with the AIA Chain, adding utility in an area currently underserved on this platform.

### Why ConderserAIA?

ConderserAIA fills a significant gap in the AIA Chain ecosystem by integrating speech processing and smart contracts in a user-friendly application. This project provides a valuable tool for developers, users, and businesses seeking an efficient way to convert spoken words into actionable smart contracts.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- AIA Chain account and API access
- Required Python packages (see below)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/chandreyeeshome/ConderserAIA.git
    cd ConderserAIA
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the AIA Chain API credentials in the `.env` file or directly within the script.

### Usage

1. **Run the Application**:

    ```bash
    python main.py
    ```

2. **Recording and Conversion**:
    - Start the recording and speak clearly.
    - The app will convert the recorded audio into text using the integrated speech recognition tool.
  
3. **Smart Contract Deployment**:
    - Each audio conversion automatically triggers a smart contract deployment to the AIA Chain.
    - The deployment details, including transaction hashes, will be displayed on the terminal or saved in the logs.

### Configuration

You can customize settings in `config.json` to adjust parameters such as:

- **Recording Time Limit**: Adjust the maximum length for audio recording.
- **Conversion Language**: Set the preferred language for speech-to-text processing.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.


contract deployed to 0x5c83A58eE57982b784d06e8d8e879435f6301be4


0xe14fB6a80ca5F5fd7F861Fa71Cf558835a531648