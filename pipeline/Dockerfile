FROM python:3.12-slim

WORKDIR /app

RUN pip install pandas pyarrow

COPY main.py pipeline.py ./

ENTRYPOINT ["python", "pipeline.py"]
CMD ["1"]
