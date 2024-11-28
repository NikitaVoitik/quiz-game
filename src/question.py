class Question:
    """
    The Question class represents a quiz question with multiple choices and a correct answer.

    Attributes:
        answer (str): The correct answer to the question.
        choices (list): A list of possible answer choices.
        text (str): The text of the question.
        level (int): The difficulty level of the question.
    """

    def __init__(self, question: str, level: int):
        """
        Initializes the Question class with the given question text and difficulty level.

        Args:
            question (str): The text of the question, including the answer choices.
            level (int): The difficulty level of the question.
        """
        self.answer = None
        self.choices = None
        self.text = None
        self.parse_question(question)
        self.level = level

    def parse_question(self, question):
        """
        Parses the question text to extract the question, answer choices, and the correct answer.

        Args:
            question (str): The text of the question, including the answer choices.
        """
        lines = question.strip().split("\n")
        text = lines[0]
        choices = []
        answer = None

        for line in lines[1:]:
            choice = line.strip()
            if "*" in choice:
                answer = choice.replace("*", "").strip()
            choices.append(choice.replace("*", "").strip())

        self.text = text
        self.choices = choices
        self.answer = answer