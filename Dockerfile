FROM python:3.8-alpine

COPY ctrlmaniac /ctrlmaniac

CMD ["python", "-m", "ctrlmaniac.rps"]