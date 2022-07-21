FROM python:3.9-slim
RUN apt-get update -y
ENV PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /workspace
COPY . .
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false
CMD ["/bin/bash", "scripts/start-dev.sh"]