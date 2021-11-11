from random import choice
import requests
from ipPool import selectIppage
# this is a test file to test whether ipPool is useful
def result(url,headers,port):
    proxy_support = {'http':'http://'+port,'https':'https://'+port,}
    response = requests.get(url, headers,proxies=proxy_support)
    print(response.text)

url = 'http://ip.tool.chinaz.com/'
headers = {
        'Host': "api.map.baidu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
iplist=selectIppage(3)
print("——————————————————————We get ipPool successfully——————————————————————————")
proxy = choice(iplist)
port =proxy[0]+":"+proxy[1]

result("http://ip.tool.chinaz.com/", headers, port)