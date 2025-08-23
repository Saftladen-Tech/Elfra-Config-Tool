FROM python:3.12.4-alpine

WORKDIR /ElfraConfigtool

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 5555

CMD ["python", "run.py"]