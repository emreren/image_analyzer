
import re
from image_analyzer.enums import DataTypes
from config import settings


async def find_id_number(text: str) -> list[dict[str, str] | None]:
    id_number_pattern = re.compile(settings.REGEX_PATTERNS.id_number)
    unique_id_numbers = set()
    for number in id_number_pattern.findall(text):
        unique_id_numbers.add(number)
    values = [
        {
            "value": number,
            "type": DataTypes.ID_NUMBER.value,
        }
        for number in unique_id_numbers
        if await is_valid_id_number(number)
    ]

    return values


async def is_valid_id_number(number: str):

    if not len(number) == 11:
        return False

    if not number.isdigit():
        return False

    if int(number[0]) == 0:
        return False

    digits = [int(d) for d in str(number)]

    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False

    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False

    return True