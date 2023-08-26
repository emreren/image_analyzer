
import re
from image_analyzer.enums import DataTypes
from config import settings


async def find_plate(text: str) -> list[dict[str, str] | None]:
    plate_pattern = re.compile(settings.REGEX_PATTERNS.plate)
    unique_plates = set()
    for number in plate_pattern.findall(text):
        unique_plates.add(number.replace(" ", ""))
    values = [
        {
            "value": number.replace(" ", ""),
            "type": DataTypes.PLATE.value,
        }
        for number in unique_plates
    ]

    return values
