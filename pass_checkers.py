"""Password checkers module."""


def is_very_long(password):
    """Return True if password is very long."""
    return len(password) >= 13


def has_digits(password):
    """Return True if password has at least one digit."""
    return any(char.isdigit() for char in password)


def has_letters(password):
    """Return True if password has at least one letter."""
    return any(not char.isdigit() for char in password)


def has_upper_letters(password):
    """Return True if password has at least one upper letter."""
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    """Return True if password has at least one lower letter."""
    return any(char.islower() for char in password)


def has_symbols(password):
    """Return True if password has at least one symbol."""
    return any(not char.isalnum() for char in password)


def has_not_only_symbols(password):
    """Return True if password has not only symbol."""
    return any(char.isalnum() for char in password)
