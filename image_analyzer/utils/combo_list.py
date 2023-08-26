
import re
from image_analyzer.enums import DataTypes
from config import settings


async def find_combo_list(text: str) -> list[dict[str, str] | None]:
    combo_list_pattern = re.compile(settings.REGEX_PATTERNS.combo_list)
    unique_combo_lists = set()
    for number in combo_list_pattern.findall(text):
        unique_combo_lists.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.COMBO_LIST.value,
        }
        for number in unique_combo_lists
    ]
    return values
