import re
from image_analyzer.enums import DataTypes


async def find_cc_number(text: str) -> list[dict[str, str] | None]:
    cc_pattern_1 = re.compile(r"\b(?:\d{4}-){3}\d{4}\b")
    cc_pattern_2 = re.compile(r"\b(?:\d{4}\s){3}\d{4}\b")
    cc_pattern_3 = re.compile(r"\b\d{16}\b")

    patterns = [cc_pattern_1, cc_pattern_2, cc_pattern_3]

    found_credit_cards = []

    for pattern in patterns:
        matches = pattern.findall(text)
        matches = [match.replace("-", "").replace(" ", "") for match in matches]
        found_credit_cards.extend(matches)

    unique_credit_cards = set()
    for number in found_credit_cards:
        unique_credit_cards.add(number)

    values = [
        {
            "value": number,
            "type": DataTypes.CREDIT_CARD_NUMBER.value,
        }
        for number in unique_credit_cards
        if await is_valid_cc(number)
    ]

    return values


async def is_valid_cc(card_number: str) -> bool:
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    return checkSum % 10 == 0