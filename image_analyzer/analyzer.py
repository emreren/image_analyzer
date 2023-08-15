from io import BytesIO
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
from PIL import Image
import pytesseract


async def read_content(file):
    image = Image.open(BytesIO(file))

    extracted_text = pytesseract.image_to_string(image)

    return extracted_text.replace("\n", " ")


async def find_sensitive_data(text: str) -> list[dict[str, str] | None]:
    findings = []
    findings.extend(await find_phone_number(text))
    findings.extend(await find_id_number(text))
    findings.extend(await find_cc_number(text))
    findings.extend(await find_plate(text))
    findings.extend(await find_date(text))
    findings.extend(await find_email(text))
    findings.extend(await find_domain(text))
    findings.extend(await find_url(text))
    findings.extend(await find_hash(text))
    findings.extend(await find_combo_list(text))

    return findings
