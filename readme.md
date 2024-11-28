# Quiz Game

This is a simple quiz game built using Python and Pygame. The game fetches quiz questions from the OpenAI API and displays them to the user. The user can navigate through the menu, start the game, and answer the questions.

## Features

- Main menu with options to start the game, change settings, and quit.
- Settings menu to adjust the difficulty level of the questions.
- Fetches quiz questions from the OpenAI API.
- Displays questions and choices, and checks the user's answers.

## Requirements

- Python 3.12
- Pygame
- OpenAI Python client library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NikitaVoitik/quiz-game.git
   cd quiz-game
2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
4. Set up your OpenAI API key:
   - Create an account on the OpenAI platform.
   - Create an API key.
   - Set the `OPENAI_API_KEY` environment variable to your API key.
   ```bash
    export OPENAI_API_KEY='your-api-key-here'  # On Windows use `set OPENAI_API_KEY=your-api-key-here`

## Usage
#### Run the game:
    python main.py

#### Use the following controls to navigate and play the game:
1. `W/S`: Navigate up/down in the menu.
2. `Enter`: Select menu option.
3. `Backspace`: Go back to the main menu.
4. `Q/W/E`: Select answer choices during the game.

# Project Structure
**`main.py:`** Entry point of the game.

**`src/app.py`**: Contains the `App` class which manages the game state and rendering.

**`src/menu.py`**: Contains the `Menu` class which handles the main menu.

**`src/question.py`**: Contains the `Question` class which represents a quiz question.

**`src/settings.py`**: Contains the `Settings` class which handles the settings menu.

**`src/utils.py`**: Contains utility functions and constants.
