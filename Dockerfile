FROM python:2.7

RUN mkdir -p /app
COPY main.py /app/main.py

ENTRYPOINT ["python"]
CMD ["/app/main.py"]
