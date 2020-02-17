#!/usr/bin/python3
'''
Code snippet for SDWAN API Call
'''
import requests
requests.packages.urllib3.disable_warnings()
login_creds = {"j_username":"devnetuser","j_password":"Cisco123!"}
api_path = "https://sandboxsdwan.cisco.com:8443"
sess = requests.session()
auth_resp = sess.post(api_path+"/j_security_check", data=login_creds, verify=False)
result = sess.get(api_path+"/dataservice/device")
result.json()
for device in result.json()['data']:
   print("Device-Name:" + device['host-name'] + " - " + device['system-ip'])

