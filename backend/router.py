import io

import numpy as np
from PIL import Image
from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi import responses
from ultralytics import YOLO

router = APIRouter(prefix="/predict")

detector = YOLO("best.pt")


class ResponseError(Exception):
    pass


@router.post("/segment_cells")
async def segment_cells(image: UploadFile = File(...)):
    img = Image.open(io.BytesIO(image.file.read())).convert('RGB')
    img = np.array(img)
    return predict(img)


def predict(img):
    results = detector(img)  # predict on an image
    return results


def response_content(content):
    try:
        response_stream = io.BytesIO(content)
        res = responses.StreamingResponse(
            response_stream,
            media_type="image/jpeg",
        )
    except Exception:
        raise ResponseError('[Error] Failed to send result')
    return res
