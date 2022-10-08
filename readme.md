FOR testcase_2 !

[![Python CI](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml/badge.svg)](https://github.com/ruslanakhmett/test_cases/actions/workflows/ci.yml)

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
By connecting to the container, you can execute 'curl http://ptsv2.com' and see the result.


Run without docker:
1. Copy testcase_2.py on your Linux host
2. Run apt install -y nano python3 python3-pip python3-dev libnfnetlink-dev libnetfilter-queue-dev curl iptables
3. Run pip3 install scapy NetfilterQueue flashtext
4. Run python3 testcase_2.py and run curl http://ptsv2.com on second terminal.



####################################

ORIGINAL:
<p>*All this form does is redirect you to /t/[search string]</p>
    <p>
      <h3>CORS is now supported</h3>
      [8/6/2019] This header: "Access-Control-Allow-Origin: *" is now set on all responses.</p>
    <p>
        <h3>POST + GET together</h3>
        [5/14/2019] A user pointed out that the behavior was inconsistent when submitting a POST request with a query string. 
        This is a weird case because <a href="https://www.w3.org/TR/html4/interact/forms.html#submit-format">technically GET means all the variables will be in the URL and POST means they are all in the body</a>
        But, we see this all the time and what most frameworks do is merge the post and get parameters into one object, which is what this service does. So you will see both together. If you wish
        to view the post body seperately from the get parameters you may configure the toilet to dump the post body first. In which case the stream will be consumed and only the get
        parameters will be parsed.

######################################

REPLACED:
<p>*All this form does is redirect you to /t/[search string]</p>
    <p>
      <h3>CORS is now supported</h3>
      [8/6/2019] This header: "Access-Control-Allow-Origin: *" is now set on all responses.</p>
    <p>
        <h3>POST + !_!_!_! !_!_!_!</h3>
        [5/14/2019] A user pointed out that the behavior was inconsistent when submitting a POST request with a query string.
        This is a weird case because <a href="https://www.w3.org/TR/html4/interact/forms.html#submit-format">technically !_!_!_! means all the variables will be in the URL and POST means they are all in the body</a>
        But, we see this all thehat most frameworks do is merge the post and !_!_!_! !_!_!_! into one object, which is what this service does. So you will see both !_!_!_!. If you wish
        to view the post body seperately from the !_!_!_! !_!_!_! you may configure the toilet to dump the post body first. In which case the stream will be consumed and only the !_!_!_!
        !_!_!_! will be parsed.