from .utils import colors

class Menu:
    """
    The Menu class manages the main menu of the quiz game.

    Attributes:
        app (App): The main application instance.
        menu_items (list): A list of dictionaries representing the menu items.
        selected_index (int): The index of the currently selected menu item.
    """

    def __init__(self, app):
        """
        Initializes the Menu class with the given application instance.

        Args:
            app (App): The main application instance.
        """
        self.app = app
        self.menu_items = [
            {"text": "Start Game"},
            {"text": "Settings"},
            {"text": "Quit"}
        ]
        self.selected_index = 0

    def draw(self):
        """
        Draws the main menu on the screen.
        """
        self.app.display.fill(colors.DarkGray)
        for index, item in enumerate(self.menu_items):
            color = colors.White if index != self.selected_index else colors.Green
            text_surface = self.app.font.render(item["text"], True, color)
            tx = (self.app.size[0] - text_surface.get_width()) // 2
            ty = 200 + index * 50
            self.app.display.blit(text_surface, (tx, ty))