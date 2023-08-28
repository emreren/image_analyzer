
from image_analyzer.utils.phone_number import find_phone_number
from image_analyzer.utils.id_number import find_id_number
from image_analyzer.utils.credit_card_number import find_cc_number
from image_analyzer.utils.plate import find_plate
from image_analyzer.utils.date import find_date
from image_analyzer.utils.email import find_email
from image_analyzer.utils.domain import find_domain
from image_analyzer.utils.url import find_url
from image_analyzer.utils.hash import find_hash
from image_analyzer.utils.combo_list import find_combo_list
import pytesseract
from PIL import Image
from io import BytesIO
import hashlib
import asyncio


async def get_hash_of_file(file: bytes) -> str:
    hash_value = hashlib.sha256(file).hexdigest()
    return hash_value


async def read_content(file) -> str:
    image = Image.open(BytesIO(file))
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text.replace("\n", " ")


async def find_sensitive_data(text: str) -> list[dict[str, str]]:
    tasks = [
        find_phone_number(text),
        find_id_number(text),
        find_cc_number(text),
        find_plate(text),
        find_date(text),
        find_email(text),
        find_domain(text),
        find_url(text),
        find_hash(text),
        find_combo_list(text),
    ]

    findings = []
    results = await asyncio.gather(*tasks)

    for result in results:
        if result is not None:
            findings.extend(result)

    return findings


