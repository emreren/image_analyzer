import re
import validators
from image_analyzer.enums import DataTypes


async def find_email(text: str) -> list[dict[str, str] | None]:
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    values = [
        {
            "value": number,
            "type": DataTypes.EMAIL.value,
        }
        for number in email_pattern.findall(text)
        if validators.email(number)
    ]

    return values




