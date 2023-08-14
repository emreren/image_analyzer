import re
from image_analyzer.enums import DataTypes


async def find_phone_number(text: str) -> list[dict[str, str] | None]:
    phone_pattern = re.compile(r'\b(?:\+\d{1,3}\s?)?(?:\(\d{1,4}\)\s?)?(?:\d{3,}\s?-?)?\d{3,}[-\s]?\d{2,}\b')
    values = [
        {
            "value": number,
            "type": DataTypes.PHONE_NUMBER.value,
        }
        for number in phone_pattern.findall(text)
    ]

    return values
