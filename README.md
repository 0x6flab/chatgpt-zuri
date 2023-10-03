# chatgpt-zuri

[![CI](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/ci.yaml)
[![CD](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/cd.yaml/badge.svg)](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/cd.yaml)
[![CodeQL](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/0x6flab/chatgpt-zuri/actions/workflows/github-code-scanning/codeql)
![GitHub](https://img.shields.io/github/license/0x6flab/chatgpt-zuri)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/0x6flab/chatgpt-zuri)

This is a repository created to match or even beat the powers of Zuri, Safaricom Chatbot, by showcasing a chatbot powered by OpenAI's GPT-3.5 language model. The chatbot is designed to answer users' questions on a wide range of topics using natural language processing techniques.

## Features

- Natural Language Processing
- Powered by OpenAI's GPT-3.5 language model
- Telegram Bot

## TODOs

- [ ] Add Twitter Integration
- [ ] Add WhatsApp Integration
- [ ] Add Facebook Messenger Integration
- [ ] Streamline Deployment

## Pre-requisites

The following are required to run the chatbot:

- Python 3.6+
- Docker

Developing the chatbot requires the following:

- Python 3.6+
- Docker

## Installation

Once you have the pre-requisites installed, you can install the chatbot by running the following commands:

1. Clone the repository

   ```bash
   git clone https://github.com/0x6flab/chatgpt-zuri
   ```

2. Create a virtual environment

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment

   ```bash
   source venv/bin/activate
   ```

4. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Run the chatbot

   ```bash
   make run
   ```

## Usage

The chatbot can be used by sending a message to the Telegram bot. The bot can be found at [https://t.me/chatgptzuribot](https://t.me/chatgptzuribot).

## Contributing

Contributions are welcome. Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
