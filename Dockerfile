FROM python:3.11.2-alpine3.16 as base

FROM base as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt /requirements.txt

RUN python -m venv --upgrade-deps /venv \
    && /venv/bin/pip install -r requirements.txt

FROM base as final

ENV RUN_PRESTART=0

WORKDIR /app

COPY --from=builder /venv /venv

COPY ./docker/*.sh ./
RUN chmod +x *.sh

COPY ./heckin_chonker_bot /app/heckin_chonker_bot

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/app/start.sh"]
