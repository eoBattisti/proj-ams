# syntax=docker/dockerfile:1
FROM python:3.12-alpine as builder

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    COLUMN=80 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    VIRTUAL_ENV=/opt/venv \
    PATH="${VIRTUAL_ENV}/bin:$PATH"

WORKDIR /asm/

RUN --mount=type=cache,target=/var/cache/apk/,sharing=locked \
    apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    linux-headers \
    libffi-dev

COPY --from=ghcr.io/astral-sh/uv:0.6.9 /uv /uvx /bin/
COPY ./pyproject.toml .

RUN uv venv ${VIRTUAL_ENV} && \
    uv pip compile --all-extras pyproject.toml --output-file=requirements.txt && \
    uv pip install -r requirements.txt && \
    find /opt/venv -type d -name "__pycache__" -exec rm -rf {} + && \
    find /opt/venv -name "*.pyc" -delete && \
    find /opt/venv -name "*.pyo" -delete && \
    find /opt/venv -name "*.dist-info" -exec rm -rf {} + && \
    find /opt/venv -name "*.egg-info" -exec rm -rf {} + && \
    /opt/venv/bin/pip uninstall -y pip setuptools wheel || true && \
    apk del .build-deps

COPY . .

FROM python:3.12-alpine as final

ARG USERNAME=asm
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN --mount=type=cache,target=/var/cache/apk/,sharing=locked \
    apk add --no-cache \
    libpq \
    netcat-openbsd \
    postgresql-client \
    gettext \
    su-exec \
    && addgroup -g ${USER_GID} ${USERNAME} \
    && adduser -u ${USER_UID} -G ${USERNAME} -h /home/${USERNAME} -s /bin/sh -D ${USERNAME}

WORKDIR /home/${USERNAME}/asm/

COPY --from=builder --chown=${USERNAME}:${USERNAME} /opt/venv /opt/venv
COPY --from=builder --chown=${USERNAME}:${USERNAME} /asm /home/${USERNAME}/asm

USER ${USERNAME}

ENTRYPOINT ["./docker/entrypoint.sh"]
