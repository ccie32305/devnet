#!/usr/bin/python3
'''
Code snippet for ACI API Call
'''
import requests
requests.packages.urllib3.disable_warnings()
url = "https://sandboxapicdc.cisco.com/api"
body = {"aaaUser": {"attributes": {"name":"admin","pwd":"ciscopsdt"}}}
r = requests.post(url + "/aaaLogin.json",json=body,verify=False)
auth = r.json()
headers = {"Cookie":"APIC-Cookie="+auth["imdata"][0]["aaaLogin"]["attributes"]["token"]}
epg = requests.get(url + "/class/fvAEPg.json", headers=headers, verify=False)
print(epg.json())
