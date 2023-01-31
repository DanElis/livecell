FROM ultralytics/ultralytics

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install python-multipart
RUN pip install environs

WORKDIR /backend
COPY . /backend

CMD ["python3.8", "main.py"]
