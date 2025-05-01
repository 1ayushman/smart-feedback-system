FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python3 -m textblob.download_corpora
EXPOSE 5000
CMD ["python", "app/app.py"]
