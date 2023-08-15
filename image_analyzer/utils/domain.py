import re
import validators
from image_analyzer.enums import DataTypes


async def find_domain(text: str) -> list[dict[str, str] | None]:
    domain_pattern = re.compile(r'\b(?:https?://)?(?:www\.)?([A-Za-z0-9.-]+)\b')
    values = [
        {
            "value": number,
            "type": DataTypes.DOMAIN.value,
        }
        for number in domain_pattern.findall(text)
        if validators.domain(number)
    ]

    return values

