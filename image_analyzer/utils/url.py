
import re
import validators
from image_analyzer.enums import DataTypes
from config import settings


async def find_url(text: str) -> list[dict[str, str] | None]:
    url_pattern = re.compile(settings.REGEX_PATTERNS.url)
    urls = [tuple(j for j in i if j)[-1] for i in url_pattern.findall(text)]
    unique_urls = set()
    for number in urls:
        unique_urls.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.URL.value,
        }
        for number in unique_urls
        if validators.url(number)
    ]
    return values

