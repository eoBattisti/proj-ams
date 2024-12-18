FROM python:3.10-slim

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMN 80

ARG USERNAME=asm
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV HOME=/home/${USERNAME}

RUN apt update && apt upgrade -y

RUN apt -y install libpq-dev python3-dev gcc netcat-traditional make cron \
        postgresql postgresql-contrib build-essential gettext

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR ${HOME}/asm/

RUN mkdir -p /etc/sudoers.d/

RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
    echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    echo chmod 0440 /etc/sudoers.d/${USERNAME}

COPY . .

RUN bash ./docker/build.sh

USER ${USERNAME}

ENTRYPOINT [ "./docker/entrypoint.sh" ]
