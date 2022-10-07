FROM alpine:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk update && apk upgrade 

RUN apk add nano python3 py3-pip py3-wheel python3-dev libnfnetlink-dev libnetfilter_conntrack-dev libnetfilter_queue curl iptables

RUN pip3 install scapy NetfilterQueue flashtext

CMD ["python3", "testcase_2.py"]