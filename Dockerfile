FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
	&& rm -rf /root/.cache/
	

COPY . .

ENTRYPOINT ["python3", "main.py"]
