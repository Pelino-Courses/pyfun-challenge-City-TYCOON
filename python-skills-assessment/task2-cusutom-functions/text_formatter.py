def format_text(text: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str:
    """
    Format text with optional prefix, suffix, capitalization, and truncation.

    Parameters:
    - text (str): The base text to format.
    - prefix (str): Optional prefix to add.
    - suffix (str): Optional suffix to add.
    - capitalize (bool): Capitalize the first letter if True.
    - max_length (int): Maximum allowed length of the final string.

    Returns:
    - str: Formatted text.

    Raises:
    - TypeError: If input types are incorrect.
    - ValueError: If max_length is negative.

    Example:
    >>> format_text("hello", prefix=">>", suffix="<<", capitalize=True, max_length=10)
    '>>Hello<<'
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(prefix, str) or not isinstance(suffix, str):
        raise TypeError("Prefix and suffix must be strings.")
    if not isinstance(capitalize, bool):
        raise TypeError("Capitalize must be a boolean.")
    if max_length is not None and (not isinstance(max_length, int) or max_length < 0):
        raise ValueError("max_length must be a non-negative integer.")

    result = f"{prefix}{text}{suffix}"
    if capitalize:
        result = result.capitalize()
    if max_length is not None:
        result = result[:max_length]
    return result
