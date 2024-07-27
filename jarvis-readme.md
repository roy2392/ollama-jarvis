# JARVIS: Your AI-Powered Voice Assistant

## Overview

JARVIS (Just A Rather Very Intelligent System) is an advanced AI-powered voice assistant that combines several cutting-edge technologies to provide a seamless, voice-controlled interface for complex tasks and system operations.

## Key Components

- **Open Interpreter**: Executes complex tasks and runs code directly on your local machine.
- **Ollama**: Provides local language processing capabilities.
- **Whisper**: Converts speech to text for voice command interpretation.
- **ElevenLabs**: Generates natural-sounding voice responses.
- **Gradio**: Creates a user-friendly interface for interacting with JARVIS.

## Features

- Voice-controlled interaction
- Ability to execute complex tasks and run code
- Local processing for enhanced privacy and speed
- Natural language understanding and generation
- Customizable and extensible

## Prerequisites

- Python 3.7+
- Git
- An ElevenLabs API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/jarvis-project.git
   cd jarvis-project
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Ollama following the instructions at [Ollama's official website](https://ollama.ai/).

## Configuration

1. Open the `jarvis.py` file.
2. Replace `<your_eleven_labs_api_key>` with your actual ElevenLabs API key.

## Usage

1. Run the JARVIS script:
   ```
   python jarvis.py
   ```

2. Once the Gradio interface loads, click on the "Record from Microphone" button.
3. Speak your command clearly.
4. Click "Stop" when you're done speaking.
5. Click "Submit" to process your command.

JARVIS will process your command, execute any necessary tasks, and respond verbally.

## Example Commands

- "Find all PDF files in my Documents folder and sort them by date."
- "Analyze my monthly sales Excel file and create a trend graph."
- "Check my email inbox, filter important messages, and create a summary."
- "Write a Python script to convert all PNG images in a folder to JPEG format."
- "Monitor my computer's resource usage and alert me if any process is consuming too much."

## Customization

You can extend JARVIS's capabilities by modifying the `bot` function in `jarvis.py`. Add new command interpretations and actions based on your specific needs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the Whisper model
- ElevenLabs for the voice generation technology
- The teams behind Open Interpreter, Ollama, and Gradio

## Disclaimer

This project is for educational purposes only. Ensure you comply with all relevant laws and regulations when using voice recognition and AI technologies.
