
import re
import validators
from image_analyzer.enums import DataTypes
from config import settings


async def find_email(text: str) -> list[dict[str, str] | None]:
    email_pattern = re.compile(settings.REGEX_PATTERNS.email)
    unique_emails = set()
    for number in email_pattern.findall(text):
        unique_emails.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.EMAIL.value,
        }
        for number in unique_emails
        if validators.email(number)
    ]

    return values




