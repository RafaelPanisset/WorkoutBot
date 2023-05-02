# Workout Bot

The Workout Bot is a Telegram chatbot that provides users with a random selection of exercises based on the body part they want to work on. 

## Getting Started

### Prerequisites

To use the Workout Bot, you'll need to have Python 3.x and the following Python library installed:

- telebot

### Installing

1. Clone the repository to your local machine.
2. Install the required Python library using pip: `pip install pyTelegramBotAPI`
3. In `bot.py`, replace `YOUR_BOT_TOKEN` with your own Telegram bot token.

### Running the bot

To run the bot, simply execute `bot.py`. The bot will start listening for messages and respond accordingly.

## Exercises

The list of exercises is stored in `exercises.py` as a dictionary of lists. Each list contains a number of exercises for a specific body part. You can modify this file to add or remove exercises as needed.

## Acknowledgments

This project was inspired by my passion for fitness and my desire to create useful software tools. I would like to thank the developers of the `telebot` library for making it easy to create Telegram chatbots using Python.
