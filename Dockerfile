FROM python:3.12.4

WORKDIR /ElfraConfigtool

COPY package*.json ./

RUN npm install

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]