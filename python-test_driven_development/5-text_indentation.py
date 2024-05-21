#!/usr/bin/python3
"""
Print text with two new lines after each '.', ':', and '?' character.
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', ':', and '?' character.

    Parameters:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello.

        How are you?

        I'm fine.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")
    last_space = False
    for c in text:
        if c in {'.', ':', '?'}:
            print(c)
            print()
            print()
            last_space = True
        elif last_space is True and c == ' ':
            last_space = False
            continue
        else:
            print(c, end="")
