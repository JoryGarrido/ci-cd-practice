FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python-setuptools --no-install-recommends
RUN rm -rf /var/lib/apt/lists/*

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]