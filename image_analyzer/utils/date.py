import re
import dateparser
from image_analyzer.enums import DataTypes


async def find_date(text: str) -> list[dict[str, str] | None]:
    date_pattern = re.compile(r'\b(?:\d{1,2}[./-]){2}\d{2,4}\b')
    unique_dates = set()
    for number in date_pattern.findall(text):
        unique_dates.add(number.replace(" ", "").replace(".", "/").replace("-", "/"))
    values = [
        {
            "value": str(dateparser.parse(number)),
            "type": DataTypes.DATE.value,
        }
        for number in unique_dates
        if await is_valid_date(number)
    ]

    return values


async def is_valid_date(text: str) -> bool:
    try:
        dateparser.parse(text)
        return True
    except:
        return False
