"""Password calculator module."""

from pass_checkers import (
    is_very_long,
    has_digits,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
    has_not_only_symbols,
)


def calculate_password_strength(password):
    """Return password score."""
    score = 0
    check_levels = (
        is_very_long,
        has_digits,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
        has_not_only_symbols,
    )

    for check_level in check_levels:
        if check_level(password):
            score += 1
    return score
