from .question import Question
import random

class colors:
    """
    The `colors` class defines a set of color constants used in the application.

    Attributes:
        Red (tuple): RGB value for red color.
        Green (tuple): RGB value for green color.
        Blue (tuple): RGB value for blue color.
        White (tuple): RGB value for white color.
        Black (tuple): RGB value for black color.
        Yellow (tuple): RGB value for yellow color.
        Cyan (tuple): RGB value for cyan color.
        Magenta (tuple): RGB value for magenta color.
        Gray (tuple): RGB value for gray color.
        Orange (tuple): RGB value for orange color.
        Purple (tuple): RGB value for purple color.
        Brown (tuple): RGB value for brown color.
        Pink (tuple): RGB value for pink color.
        LightGray (tuple): RGB value for light gray color.
        DarkGray (tuple): RGB value for dark gray color.
    """
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Yellow = (255, 255, 0)
    Cyan = (0, 255, 255)
    Magenta = (255, 0, 255)
    Gray = (128, 128, 128)
    Orange = (255, 165, 0)
    Purple = (128, 0, 128)
    Brown = (165, 42, 42)
    Pink = (255, 192, 203)
    LightGray = (211, 211, 211)
    DarkGray = (30, 31, 34)

def api_request(openai, messages, level) -> Question:
    """
    Fetches a quiz question from the OpenAI API and returns a `Question` object.

    Args:
        openai: The OpenAI API client.
        messages (list): The list of messages to send to the API.
        level (int): The difficulty level of the question.

    Returns:
        Question: An instance of the `Question` class containing the fetched quiz question.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            temperature=random.uniform(0.5, 0.7),
            messages=messages
        )
        messages.append(
            {
                "role": "assistant",
                "content": response.choices[0].message.content.split('\n')[0]
            })
    except Exception as e:
        return None
        print(f"An error occurred: {e}")
    messages.append(
        {
            "role": "user",
            "content": f"Generate a single quiz question of level {level}."
        })
    content = response.choices[0].message.content
    return Question(content, level)