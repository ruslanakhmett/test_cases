FOR testcase_2 !

[![with_docker CI](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml/badge.svg)](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml)

Page for test(only http), example: http://octobersun.com

For clarity, I chose to replace this words: ["information", "support", "October",] for this "#######"

To run need docker on your machine.

Enter your terminal:
1. docker pull sccrsccr1/linux_shiffer:latest
2. docker run --name linux-sniffer --cap-add=NET_ADMIN -d linux-sniffer:latest
3. docker exec -it linux-sniffer bash
By connecting to the container, you can execute 'curl http://octobersun.com' and see the result.



####################################

ORIGINAL:

...
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>October Sun Business Solutions</title>
<style type="text/css">

<p class="style1">
<img alt="October Sun Business Solutions" longdesc="Providing Information Technology Services to Businesses" src="OSimages/os%20b.jpg" width="700" height="165" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p class="style2">simple information technology support for business</p>
<p class="style2">&nbsp;</p>
<p class="style2">780-975-5405</p>

...

######################################

PROCESSED:

...
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>####### Sun Business Solutions</title>
<style type="text/css">
.style1 {
	text-align: center;
}
.style2 {
	text-align: center;
	font-family: Arial, Helvetica, sans-serif;
	font-size: large;
}
</style>
</head>

<body style="color: #0000FF; background-color: #000000">

<p class="style1">
<img alt="####### Sun Business Solutions" longdesc="Providing ####### Technology Services to Businesses" src="OSimages/os%20b.jpg" width="700" height="165" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p class="style2">simple ####### technology ####### for business</p>
<p class="style2">&nbsp;</p>
<p class="style2">780-975-5405</p>

</body>

</html>
