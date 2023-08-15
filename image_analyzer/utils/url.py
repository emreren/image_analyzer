import re
import validators
from image_analyzer.enums import DataTypes


async def find_url(text: str) -> list[dict[str, str] | None]:
    url_pattern = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
    urls = [tuple(j for j in i if j)[-1] for i in url_pattern.findall(text)]
    values = [
        {
            "value": number,
            "type": DataTypes.URL.value,
        }
        for number in urls
        if validators.url(number)
    ]
    return values

