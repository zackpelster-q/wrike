class KindWarning(RuntimeWarning):
    """Printed when the returned kind does not meet the expected

    Args:
        RuntimeWarning (varies): categorize as a runtime warning
    """

    pass


class GreaterThanOneWarning(RuntimeWarning):
    """Printed when the returned data list of dicts from a result
    is greater than 1

    Args:
        RuntimeWarning (varies): categorize as a runtime warning
    """

    pass


class ZeroWarning(RuntimeWarning):
    """Printed when the returned data list of dicts from a result
    is empty

    Args:
        RuntimeWarning (varies): categorize as a runtime warning
    """

    pass


class DataCappedWarning(RuntimeWarning):
    """Printed when the returned data list of dicts from a result
    is at the max that the API would return

    Args:
        RuntimeWarning (varies): categorize as a runtime warning
    """

    pass
