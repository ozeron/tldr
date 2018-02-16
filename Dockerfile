FROM ubuntu:16.04

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app

RUN apt-get -qq update && apt-get -qq -y install python3-pip
RUN pip3 install --upgrade pip

COPY requirments.txt /app/

RUN pip3 install -r requirments.txt --quiet
RUN python3 -c "import nltk; nltk.download('punkt')"
RUN python3 -c "import nltk; nltk.download('stopwords')"

ENV FLASK_APP app

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "8000"]
