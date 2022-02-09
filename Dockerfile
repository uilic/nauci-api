FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -y install libcurl4 curl

ARG REQUIREMENTS_FILE=./requirements.txt
ARG BUILD_DEPS="build-essential libcurl4-openssl-dev libssl-dev libffi-dev libpq-dev"

# libpq5 needed in the event that we have to compile postgres from source
ARG RUNTIME_DEPS="libpq5"

COPY "${REQUIREMENTS_FILE}" "${REQUIREMENTS_FILE}"

RUN apt update && apt -y install ${RUNTIME_DEPS} ${BUILD_DEPS} \
    && pip install --no-cache-dir -U pip wheel setuptools \
    && pip install --no-cache-dir -r "${REQUIREMENTS_FILE}" \
    && apt -y purge ${BUILD_DEPS} && apt -y autoremove \
    && rm -rf /var/lib/apt/lists/*

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]