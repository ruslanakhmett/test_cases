FOR testcase_2 !

[![with_docker CI](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml/badge.svg)](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml)

Page for test(only http), example: http://octobersun.com

For clarity, I chose to replace this words: ["information", "support", "October",] for this "#######"

This script is recommended to run on Linux, it seems 
MacOS does not support the netfilterqueue library. 
I did not check it for Windows.

To run you need docker on your machine.

Enter your terminal:
1. docker pull sccrsccr1/ruslan_server:latest
2. docker run --cap-add=NET_ADMIN -d ruslan_server:latest
3. docker exec -it <id_container> bash
By connecting to the container, you can execute 'curl http://octobersun.com' and see the result.


Run without docker:
1. Copy testcase_2.py on your Linux host
2. Run apt install -y nano python3 python3-pip python3-dev libnfnetlink-dev libnetfilter-queue-dev curl iptables
3. Run pip3 install scapy NetfilterQueue flashtext
4. Run python3 testcase_2.py and run curl http://octobersun.com on second terminal.



####################################

ORIGINAL:


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>October Sun Business Solutions</title>
<style type="text/css">

<p class="style1">
<img alt="October Sun Business Solutions" longdesc="Providing Information Technology Services to Businesses" src="OSimages/os%20b.jpg" width="700" height="165" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p class="style2">simple information technology support for business</p>
<p class="style2">&nbsp;</p>
<p class="style2">780-975-5405</p>

</body>

</html>

######################################

REPLACED:

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>####### Sun Business Solutions</title>
<style type="text/css">

<p class="style1">
<img alt="####### Sun Business Solutions" longdesc="Providing ####### Technology Services to Businesses" src="OSimages/os%20b.jpg" width="700" height="165" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p class="style2">simple ####### technology ####### for business</p>
<p class="style2">&nbsp;</p>
<p class="style2">780-975-5405</p>

</body>

</html>