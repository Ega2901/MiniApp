FROM python:3.11

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libmariadb-dev

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    mv ~/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install

COPY . /app

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]