import os
import sys, pygame
import time

from openai import OpenAI
from dotenv import load_dotenv
import serial

from src.app import App

load_dotenv('.env')
openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
SERIAL_PORT = '/dev/cu.usbserial-110'
BAUD_RATE = 9600

level = 1

messages = [
    {
        "role": "system",
        "content": f"You are a quiz generator tasked with creating a multiple-choice quiz question about science, history or geography. The question should have three answer options, and the correct answer must be clearly marked with an asterisk (*). The difficulty level of the question should correspond to {level} on a scale of 0 to 2, where 0 is easy, 1 is medium, and 2 is hard. DO NOT REPEAT YOURSELF"
    },
    {
        "role": "user",
        "content": f"Generate a single quiz question of level {level}."
    }
]

in_menu = True
in_intermediate = False
in_settings = False
in_game = False

def get_result():
    """Receive the result from Arduino."""
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        print("Waiting for result...")
        while True:
            if ser.in_waiting > 0:
                result = ser.readline().decode('utf-8').strip()
                print(f"Arduino says: {result}")
                return result


def main():
    """
        The main function initializes the application and handles the main event loop.

        It manages the state transitions between the menu, game, and settings screens,
        and processes user input to navigate through the application and interact with
        the quiz game.
    """
    global in_menu
    global in_game
    global in_settings
    global in_intermediate
    global level
    app = App()
    app.show_menu()
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_BACKSPACE:
                in_menu = True
                in_game = False
                in_settings = False
                in_intermediate = False
                app.show_menu()
            if in_menu:
                if event.key == pygame.K_w:
                    app.menu.selected_index = (app.menu.selected_index - 1) % len(app.menu.menu_items)
                    app.show_menu()
                elif event.key == pygame.K_s:
                    app.menu.selected_index = (app.menu.selected_index + 1) % len(app.menu.menu_items)
                    app.show_menu()
                elif event.key == pygame.K_RETURN:
                    if app.menu.selected_index == 0:
                        in_menu = False
                        in_game = True
                        in_intermediate = True
                        artificial_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
                        pygame.event.post(artificial_event)
                    if app.menu.selected_index == 1:
                        in_menu = False
                        in_settings = True
                        app.settings.draw(level)
                    if app.menu.selected_index == 2:
                        pygame.quit()
            elif in_game:
                if event.key == pygame.K_RETURN and in_intermediate:
                    app.fetch_and_render_question(openai, messages, level)
                    in_intermediate = False
                    pygame.display.update()
                if not in_intermediate:
                    with serial.Serial(SERIAL_PORT, BAUD_RATE) as ser:
                        ans = app.get_answer_ind()
                        if ans == 0:
                            ans = "A"
                        elif ans == 1:
                            ans = "B"
                        else:
                            ans = "C"
                        ser.write(ans.encode())
                        time.sleep(0.5)
                    k = get_result()
                    if k == "A":
                        k = 0
                    elif k == "B":
                        k = 1
                    else:
                        k = 2
                    app.check_answer(k)
                    in_intermediate = True
                    pygame.display.update()

            elif in_settings:
                if event.key == pygame.K_UP and app.settings.selected_index == 0:
                    level = (level + 1) % 3
                    app.settings.draw(level)
                elif event.key == pygame.K_DOWN and app.settings.selected_index == 0:
                    level = (level - 1) % 3
                    app.settings.draw(level)
                elif event.key == pygame.K_w:
                    app.settings.selected_index = (app.settings.selected_index - 1) % len(app.settings.settings_items)
                    app.settings.draw(level)
                elif event.key == pygame.K_s:
                    app.settings.selected_index = (app.settings.selected_index + 1) % len(app.settings.settings_items)
                    app.settings.draw(level)
                elif event.key == pygame.K_RETURN and app.settings.selected_index == 1:
                    artificial_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
                    pygame.event.post(artificial_event)
            pygame.display.update()


main()
