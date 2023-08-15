import re
from image_analyzer.enums import DataTypes


async def find_plate(text: str) -> list[dict[str, str] | None]:
    plate_pattern = re.compile(r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b')
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
