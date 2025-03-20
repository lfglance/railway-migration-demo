FROM ghcr.io/astral-sh/uv:debian

RUN useradd -s /bin/bash -m rps

COPY . /srv/rps

RUN chown -R rps:rps /srv/rps

WORKDIR /srv/rps

RUN uv sync

ENTRYPOINT ["uv", "run"]