FROM python:3.6
COPY . /foodpanda
WORKDIR /foodpanda
RUN pip install -r requirements.txt
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl foodpanda" ]