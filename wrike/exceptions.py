class WrikeException(Exception):
    """Raised for Wrike specific errors

    Args:
        Exception (varies): pass through what to throw
    """

    pass


class KindException(ValueError):
    """Raised for when the returned kind does not meet the expected

    Args:
        ValueError (varies): categorize as a value error
    """

    pass
