FROM python:3.7-alpine
COPY . /fos-data-scraping
WORKDIR /fos-data-engineer
RUN pip install -r requirements.txt
CMD ["python", "scraper.py"]