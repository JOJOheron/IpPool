import re
import time
import requests

def getIpHTML(nextpageid):
        headers = {
            "Cookie": "statistics=d4f10de547cb9cf96c32dc2e2c1a7bd2; Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1636199618,1636199711,1636199722,1636199825; Hm_lpvt_8ccd0ef22095c2eebfe4cd6187dea829=1636199829",
            "Referer": "https://ip.ihuan.me/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
        respones = requests.get("https://ip.ihuan.me/address/5Lit5Zu9.html?page="+nextpageid, headers=headers)
        return respones.text

def getIpnextpageID(pageid):
   nextpageIDlist=re.findall('<\/li><li><a href="\?page=([\s\S]*?)">',getIpHTML(pageid))
   nextpageID=re.findall('([\s\S]*?)"aria-label="Next',nextpageIDlist[-1])[0]
   return (nextpageID)

def selectIppage(endtopage):
    pageid="b97827cc"
    iPpool=[]
    for i in range(endtopage):
        print("selecting page whose id is "+pageid+"......")
        ipHTML=getIpHTML(pageid)
        pageid=getIpnextpageID(pageid)
        ipset=re.findall('svg">([\s\S]*?)<\/td><\/tr>',ipHTML)
        for iplist in ipset:
            time.sleep(0.5)
            ip=re.findall('([\s\S]*?)<\/a><\/td><td>',iplist)[0]
            ipport=re.findall('<td>([\s\S]*?)<\/td>',iplist)[0]
            ipHttp=re.findall('<td>([\s\S]*?)<\/td>', iplist)[3]
            ipPost=re.findall('<td>([\s\S]*?)<\/td>', iplist)[4]
            ipinfo=[]
            if(check_proxy(ip, ipport)):
                ipinfo.append(ip)
                ipinfo.append(ipport)
                ipinfo.append(ipHttp)
                ipinfo.append(ipPost)
                iPpool.append(ipinfo)
    return (iPpool)

def check_proxy(ip, port):
    try:
        requests.adapters.DEFAULT_RETRIES = 3
        proxy = f"http://{ip}:{port}"
        res = requests.get(url="http://icanhazip.com/", timeout=3, proxies={"http": proxy})
        proxyIP = res.text[:-1]
        if (proxyIP == ip):
            return True
        else:
            return False
    except:
        return False


selectIppage(4)

