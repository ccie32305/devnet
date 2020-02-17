#!/usr/bin/python3
'''
Code snippet for Webex Teams
'''
import os
import requests
webex_token = os.getenv('WEBEX_TOKEN')
headers = {"Authorization":"Bearer " + webex_token}
cisco_webex_teams_rooms = requests.get("https://api.ciscospark.com/v1/rooms", headers=headers)
for items in cisco_webex_teams_rooms.json()['items']:
   print(items['title'] + "," + items['id'])

message =  {"toPersonEmail":"toanyuser@cisco.com","text":"This is automated REST API generated message, that could have been send from anywhere Greetz CCIE 32305"}
send_message_cisco_webex = requests.post("https://api.ciscospark.com/v1/messages",json=message,headers=headers)

