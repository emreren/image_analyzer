from fastapi import FastAPI, UploadFile, Request, status, HTTPException
from fastapi.responses import JSONResponse
from image_analyzer.analyzer import read_content, find_sensitive_data


class WrongFileFormatException(Exception):
    pass


app = FastAPI()
IMAGE_TYPES = {"image/jpeg", "image/apng", "image/avif", "image/gif", "image/png", "image/svg", "image/xml", "image/webp"}


@app.exception_handler(WrongFileFormatException)
async def unicorn_exception_handler(_request: Request, _exc: WrongFileFormatException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"status": "bad request. wrong file format."},
    )


@app.post("/analyze/")
async def analyze_image(file: UploadFile):
    if file.content_type not in IMAGE_TYPES:
        raise WrongFileFormatException(file.filename)
    content = await read_content(await file.read())
    if not content:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
    findings = await find_sensitive_data(content)
    return {
        "content": content,
        "status": "successful",
        "findings": findings
    }
