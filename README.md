# GPT4Kids

## Description

GPT4Kids is a voice assistant designed to run on Raspberry Pi, helping children with homework and research tasks. It accepts voice commands, interacts with the ChatGPT API from OpenAI to generate responses, and converts these text responses back into spoken words.

## Features

- Voice command recognition.
- Integration with OpenAI's ChatGPT API for generating responses.
- Text-to-speech conversion for delivering the assistant's responses.

## Technologies

- Python 3.7+
- Libraries: `speech_recognition`, `pyaudio`, `openai`, `gtts`

## Installation

1. Clone the repository:
   `git clone https://github.com/mgrama/gpt4kids.git`

2. Navigate to the project directory:
   `cd gpt4kids`

3. Install the required libraries:
   `pip install -r requirements.txt`

## Usage

1. Start the assistant:
   `python assistant.py`

2. Speak into the microphone to ask questions like "What is the capital of France?" or "Help me with my math homework."

## Configuration

- Make sure to obtain and set up your OpenAI API key in the `config.py` file.
- Adjust audio input settings as necessary for your specific Raspberry Pi model and microphone setup.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions are welcome! Please read the `CONTRIBUTING.md` for how to contribute to this project.

## Support

If you encounter any issues, please open an issue on the GitHub repository.

## Authors

- Mark Grama

## Acknowledgments

- Thanks to OpenAI for providing the ChatGPT API.
