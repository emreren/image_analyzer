import re
from image_analyzer.enums import DataTypes


async def find_phone_number(text: str) -> list[dict[str, str] | None]:
    phone_pattern = re.compile(r'\b(\+90|0)?\s*(\(\d{3}\)[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}|\(\d{3}\)[\s-]*\d{3}[\s-]*\d{4}|\(\d{3}\)[\s-]*\d{7}|\d{3}[\s-]*\d{3}[\s-]*\d{4}|\d{3}[\s-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}|\d{12})\b')
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
