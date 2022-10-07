FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN apt update && apt upgrade 

RUN apt install -y nano python3 python3-pip python3-dev libnfnetlink-dev libnetfilter-queue-dev curl iptables

RUN pip3 install scapy NetfilterQueue flashtext

CMD ["python3", "testcase_2.py"]