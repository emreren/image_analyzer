import redis.asyncio as redis
from fastapi import FastAPI, UploadFile, Request, status, HTTPException
from fastapi.responses import JSONResponse
from image_analyzer.analyzer import read_content, find_sensitive_data, get_hash_of_file
from image_analyzer.custom_expections import WrongFileFormatException
from config import settings
import json


app = FastAPI()
redis_client = redis.Redis(host="redis", port=6379, db=0)


@app.exception_handler(WrongFileFormatException)
async def unicorn_exception_handler(_request: Request, _exc: WrongFileFormatException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"status": "bad request. wrong file format."},
    )


@app.post("/analyze/")
async def analyze_image(file: UploadFile):
    # Check if the uploaded file is an image
    if file.content_type not in settings.IMAGE_TYPES.image_types:
        raise WrongFileFormatException(file.filename)

    # Read the content and calculate the hash of the file
    file_object = await file.read()
    image_hash = await get_hash_of_file(file_object)

    # Check if the result is cached in Redis
    if cached_result := await redis_client.get(image_hash):
        return json.loads(cached_result)

    # Read the content from the file object and if the content is empty, return a 204 No Content response
    content = await read_content(file_object)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )

    # Find sensitive data in the content
    findings = await find_sensitive_data(content)

    # Prepare the result JSON object
    result = {
        "content": content,
        "status": "successful",
        "findings": findings
    }

    # Cache the result in Redis
    await redis_client.set(image_hash, json.dumps(result))
    return result