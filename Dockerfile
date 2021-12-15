FROM python:3.8-slim-buster
WORKDIR /usr/app/src
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "./main.py"]