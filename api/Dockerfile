FROM python:3.8-slim AS base
WORKDIR /app
RUN adduser -u 5678 --disabled-password --gecos "" shorturl && chown -R shorturl .
USER shorturl
COPY requirements/base.txt requirements/base.txt
RUN python -m pip install -r requirements/base.txt

FROM base AS test
COPY requirements/test.txt requirements/test.txt
RUN python -m pip install -r requirements/test.txt
COPY test test
COPY app app
ARG DATABASE_TYPE=memory
ARG DATABASE_HOST=localhost
ARG DATABASE_PORT=6379
ENV DATABASE_TYPE ${DATABASE_TYPE}
ENV DATABASE_HOST ${DATABASE_HOST}
ENV DATABASE_PORT ${DATABASE_PORT}
RUN ["python", "-m", "pytest"]

FROM base AS development
EXPOSE 8000
COPY requirements/dev.txt requirements/dev.txt
RUN python -m pip install -r requirements/dev.txt
COPY app app
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

FROM base AS production
EXPOSE 8000
COPY requirements/prod.txt requirements/prod.txt
RUN python -m pip install -r requirements/prod.txt
COPY app app
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
