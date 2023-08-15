import re
import validators
from image_analyzer.enums import DataTypes


async def find_domain(text: str) -> list[dict[str, str] | None]:
    domain_pattern = re.compile(r'\b(?:https?://)?(?:www\.)?([A-Za-z0-9.-]+)\b')
    unique_domains = set()
    for number in domain_pattern.findall(text):
        unique_domains.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.DOMAIN.value,
        }
        for number in unique_domains
        if validators.domain(number)
    ]

    return values

