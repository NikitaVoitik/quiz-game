from .utils import colors


class Settings:
    """
        The Settings class manages the settings menu of the quiz game.

        Attributes:
            app (App): The main application instance.
            settings_items (list): A list of dictionaries representing the settings menu items.
            selected_index (int): The index of the currently selected menu item.
    """
    def __init__(self, app):
        """
        Initializes the Settings class with the given application instance.

        Args:
            app (App): The main application instance.
        """
        self.app = app
        self.settings_items = [
            {"text": "Level"},
            {"text": "Back"}
        ]
        self.selected_index = 0

    def draw(self, level):
        """
        Draws the settings menu on the screen.

        Args:
            level (int): The current difficulty level of the quiz questions.
        """
        self.app.display.fill(colors.DarkGray)
        for index, item in enumerate(self.settings_items):
            if index == 0:
                text = f"Level: {level + 1}"
            else:
                text = item["text"]
            color = colors.White if index != self.selected_index else colors.Green
            text_surface = self.app.font.render(text, True, color)
            tx = (self.app.size[0] - text_surface.get_width()) // 2
            ty = 200 + index * 50
            self.app.display.blit(text_surface, (tx, ty))
