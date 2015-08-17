import sys
import requests
from BeautifulSoup import BeautifulSoup
data = {
	'mode':'191',
	'username':sys.argv[1],
	'password':sys.argv[2],
	'a':'1439199700564',
	'producttype':'0'
	}
send=requests.post('http://172.50.1.1:8090/login.xml',data=data).text
soup = BeautifulSoup(send)
print(soup.message.string)