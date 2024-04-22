# GeorgReborn

## Overview
"GeorgReborn" is a Telegram bot designed to assist users with various utilities including fetching weather updates, downloading videos and music tracks from YouTube. It is built using Python with the aiogram library and integrates the YouTube downloading functionality through the pytube library.

## Features
- **Weather Updates:** Fetch current weather information for any specified city.
- **Video Downloads:** Download short meme clips from YouTube directly via Telegram commands.
- **Music Downloads:** Extract and download the audio track from YouTube videos.

## Installation
### Prerequisites
- Python 3.8 or newer
- Docker
- Telegram Bot Token from BotFather

### Setup
1. Clone this repository to your local machine.
2. Create a `config.py` file and define your Telegram Bot Token as follows:
   ```python
   TOKEN = 'your_bot_token_here'

### Build and run the bot using Docker:
  ```python
  docker-compose up --build
  ```

### Usage
After setting up the bot and running it, you can interact with it through these commands:

- /start: Initializes the bot and shows the available commands.
- /help: Provides details about how to use the bot's functionalities.
- /weather <city>: Fetches and returns weather information for the specified city.
- /video <YouTube URL>: Downloads a video from the provided YouTube URL if it's under 5 minutes long.
- /music <YouTube URL>: Downloads the audio track from the specified YouTube video.

### Contributions
Contributions are welcome! Please fork this repository and submit a pull request with your enhancements.

### Contact
For any queries or technical issues, please open an issue in the GitHub repository.
