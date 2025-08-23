FROM python:3.12.4-alpine

WORKDIR /ElfraConfigtool

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5555

CMD ["python", "run.py"]