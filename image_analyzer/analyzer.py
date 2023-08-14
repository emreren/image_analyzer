from io import BytesIO
from image_analyzer.utils.phone_number import find_phone_number
from image_analyzer.utils.id_number import find_id_number
from PIL import Image
import pytesseract


async def read_content(file):
    image = Image.open(BytesIO(file))

    extracted_text = pytesseract.image_to_string(image)

    return extracted_text


async def find_sensitive_data(text: str) -> list[dict[str, str] | None]:
    findings = []
    findings.extend(await find_phone_number(text))
    findings.extend(await find_id_number(text))
    return findings
