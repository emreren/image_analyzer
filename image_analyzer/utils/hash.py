
import re
import validators
from image_analyzer.enums import DataTypes
from config import settings


async def find_hash(text: str) -> list[dict[str, str] | None]:
    hash_pattern = re.compile(settings.REGEX_PATTERNS.hash)
    unique_hashes = set()
    for number in hash_pattern.findall(text):
        unique_hashes.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.HASH.value,
        }
        for number in unique_hashes
        if validators.sha1(number) or validators.sha256(number) or validators.sha512(number) or validators.md5(number)
    ]
    return values
