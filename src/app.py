import pygame
from .settings import Settings
from .menu import Menu
from .question import Question
from .utils import colors, api_request

class App:
    """
    The App class manages the main application logic for the quiz game.

    Attributes:
        question (Question): The current quiz question.
        size (tuple): The size of the application window.
        display (pygame.Surface): The main display surface.
        font (pygame.font.Font): The font used for rendering text.
        menu (Menu): The main menu instance.
        settings (Settings): The settings menu instance.
    """

    def __init__(self, size=(800, 600)):
        """
        Initializes the App class with the given window size.

        Args:
            size (tuple): The size of the application window.
        """
        self.question = None
        pygame.init()
        self.size = size
        self.display = pygame.display.set_mode((self.size[0], self.size[1]))
        self.display.fill(colors.DarkGray)
        pygame.display.set_caption('Quiz Game')
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.menu = Menu(self)
        self.settings = Settings(self)

    def render_question(self, question: Question):
        """
        Renders the given quiz question on the screen.

        Args:
            question (Question): The quiz question to render.
        """
        self.display.fill(colors.DarkGray)
        words = question.text.split()
        lines = []
        allowed_width = int(self.size[0] * 0.8)

        while len(words) > 0:
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = self.font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break
            line = ' '.join(line_words)
            lines.append(line)
        y_offset = 40

        for line in lines:
            fw, fh = self.font.size(line)
            self.render_line(fw, y_offset, line)
            y_offset += fh

        y_offset += 40
        for choice in question.choices:
            fw, fh = self.font.size(choice)
            fh += 20
            self.render_line(fw, y_offset, choice)
            y_offset += fh

    def render_line(self, fw, y_offset, choice):
        """
        Renders a single line of text on the screen.

        Args:
            fw (int): The width of the text.
            y_offset (int): The vertical offset for the text.
            choice (str): The text to render.
        """
        tx = (self.size[0] - fw) // 2
        ty = y_offset

        text_surface = self.font.render(choice, True, colors.White)
        self.display.blit(text_surface, (tx, ty))

    def fetch_and_render_question(self, openai, messages, level):
        """
        Fetches a quiz question from the API and renders it on the screen.

        Args:
            openai: The OpenAI API client.
            messages (list): The list of messages to send to the API.
            level (int): The difficulty level of the question.
        """
        while True:
            self.question = api_request(openai, messages, level)
            if self.question is not None:
                break
        self.render_question(self.question)

    def check_answer(self, ind):
        """
        Checks if the selected answer is correct and displays the result.

        Args:
            ind (int): The index of the selected answer choice.
        """
        fw, fh = self.font.size("Correct!")
        line = "Wrong!"
        if self.question.choices[ind] == self.question.answer:
            line = "Correct!"
        self.render_line(fw, self.size[1] - 100, line)

    def get_answer_ind(self):
        for i in range(0, len(self.question.choices)):
            if self.question.choices[i] == self.question.answer:
                return i

    def show_menu(self):
        """
        Displays the main menu on the screen.
        """
        self.menu.draw()
        pygame.display.update()