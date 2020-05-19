FROM python:3.8-slim as poetry
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt

FROM python:3.8-slim
COPY --from=poetry requirements.txt ./
COPY server.py weather.py ./
RUN pip install -r requirements.txt
ENV FLASK_APP=server.py
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ]
