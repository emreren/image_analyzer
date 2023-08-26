
import re
from image_analyzer.enums import DataTypes
from config import settings


async def find_phone_number(text: str) -> list[dict[str, str] | None]:
    phone_pattern = re.compile(settings.REGEX_PATTERNS.phone_number)
    phones = [tuple(j for j in i if j)[-1] for i in phone_pattern.findall(text)]
    unique_phones = set()
    for number in phones:
        unique_phones.add(number.replace("(", "").replace(")", ""))
    values = [
        {
            "value": number.replace("(", "").replace(")", ""),
            "type": DataTypes.PHONE_NUMBER.value,
        }
        for number in unique_phones
        if 9 < len(number) < 14
    ]

    return values
