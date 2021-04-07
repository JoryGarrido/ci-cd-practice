FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip=8.1.1-2ubuntu0.6 python-dev=2.7.12-1~16.04 python-setuptools=20.7.0-1 --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]