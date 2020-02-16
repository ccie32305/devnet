#!/usr/bin/python3
'''
Tests with DNAC DevNet Sandbox
'''
import requests
import json
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
headers = {'Content-Type': 'application/json'}
auth = ('devnetuser', 'Cisco123!')
dna_request = requests.post(url,auth=auth,headers=headers)
dna_token = json.loads(dna_request.text)['Token']
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
headers = {'Content-Type': 'application/json', 'X-Auth-Token': dna_token}
dna_devices = requests.get(url,headers=headers)
print(dna_devices.text)
