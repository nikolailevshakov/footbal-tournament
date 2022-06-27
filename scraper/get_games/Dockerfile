FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3.9 python3.9-dev

WORKDIR /usr/src/get_games
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
RUN chmod +x geckodriver
RUN rm geckodriver-v0.24.0-linux64.tar.gz

CMD [ "python", "main.py" ]
EXPOSE 5000