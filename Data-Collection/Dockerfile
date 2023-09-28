###############################################
# Base Image
###############################################

FROM python:3.11-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################

FROM python-base as builder-base

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
    curl build-essential apt-utils

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY . /opt/Data-Collection

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN curl -sSL https://install.python-poetry.org | python3 && \
    poetry self update 

###############################################
# Production Image
###############################################

FROM builder-base as production
WORKDIR /opt/Data-Collection

RUN poetry install

# CMD ["/opt/poetry/bin/poetry", "run", "uvicorn", "src.monarch_py.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["/opt/poetry/bin/poetry", "run", "data-collection", "run"]
