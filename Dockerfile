FROM python:3.9-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache curl linux-headers
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
