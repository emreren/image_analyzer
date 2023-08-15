import re
from image_analyzer.enums import DataTypes


async def find_combo_list(text: str) -> list[dict[str, str] | None]:
    combo_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b:[A-Za-z0-9]+|\b[A-Za-z0-9]+:[A-Za-z0-9]+\b')
    values = [
        {
            "value": number,
            "type": DataTypes.COMBO_LIST.value,
        }
        for number in combo_pattern.findall(text)
    ]
    return values
