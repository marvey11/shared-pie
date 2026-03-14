from decimal import Decimal


def clean_decimal(number_str: str) -> Decimal:
    return Decimal(number_str)
