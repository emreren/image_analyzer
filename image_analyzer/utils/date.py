
import re
import dateparser
from image_analyzer.enums import DataTypes
from config import settings


async def find_date(text: str) -> list[dict[str, str] | None]:
    date_pattern = re.compile(settings.REGEX_PATTERNS.date)
    unique_dates = set()
    for number in date_pattern.findall(text):
        unique_dates.add(number.replace(" ", "").replace(".", "/").replace("-", "/"))
    values = [
        {
            "value": str(dateparser.parse(number)),
            "type": DataTypes.DATE.value,
        }
        for number in unique_dates
        if dateparser.parse(number)
    ]

    return values


