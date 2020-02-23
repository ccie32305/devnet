#!/usr/bin/python3
'''
Tests with Meraki DevNet Sandbox
'''
import requests
from pprint import pprint
# DevNet Sandbox API Key
headers = {"X-Cisco-Meraki-API-Key": "093b24e85df15a3e66f1fc359f4c48493eaa1b73"}
# Get first organization (no check on name or loop through organization for simplicity)
organization = requests.get("https://api.meraki.com/api/v0/organizations/",headers=headers).json()[0]['id']
# Get second network because no active clients on first one during test (no check on name or loop through organization for simplicity)
network = requests.get("https://api.meraki.com/api/v0/organizations/{}/networks".format(organization),headers=headers).json()[1]['id']
# Print clients
pprint(requests.get("https://api.meraki.com/api/v0/networks/{}/clients".format(network),headers=headers).json())

