# ENAUTO Study Notes
## 10% 1.0 Network Programmability Foundation
### 1.1 Utilize common version control operations with git (add, clone, push, commit, diff, branching, merging conflict)
```
>clone
ccie@vm:~/git_example# git clone https://github.com/ccie32305/devnet.git (Download remote repository) 
Klone nach 'devnet'... 
remote: Enumerating objects: 35, done. 
remote: Counting objects: 100% (35/35), done. 
remote: Compressing objects: 100% (28/28), done. 
remote: Total 35 (delta 9), reused 21 (delta 1), pack-reused 0 
Entpacke Objekte: 100% (35/35), Fertig. 
Prüfe Konnektivität... Fertig. 
ccie@vm:~/git_example# ls 
devnet 
ccie@vm:~/git_example# 
 
>add/remove 
ccie@vm:~/git_example/devnet# git status 
On branch master 
Your branch is up-to-date with 'origin/master'. 
nothing to commit, working directory clean 
ccie@vm:~/git_example/devnet# echo ""Hello"" > New_file 
ccie@vm:~/git_example/devnet# git status 
On branch master 
Your branch is up-to-date with 'origin/master'. 
Untracked files: 
  (use ""git add <file>..."" to include in what will be committed) 
 
        New_file 
 
nothing added to commit but untracked files present (use ""git add"" to track) 
ccie@vm:~/git_example/devnet# git add New_file 
ccie@vm:~/git_example/devnet# git status 
On branch master 
Your branch is up-to-date with 'origin/master'. 
Changes to be committed: 
  (use ""git reset HEAD <file>..."" to unstage) 
 
        new file:   New_file 
 
ccie@vm:~/git_example/devnet# git reset HEAD New_file 
ccie@vm:~/git_example/devnet# git status 
On branch master 
Your branch is up-to-date with 'origin/master'. 
Untracked files: 
  (use ""git add <file>..."" to include in what will be committed) 
 
        New_file 
 
nothing added to commit but untracked files present (use ""git add"" to track) 
ccie@vm:~/git_example/devnet# 
 
>commit 
Git commit -m “my first commit” (add to local repository) 
>push/pull
Git push (upload to remote repository) 
ccie@vm:~/git_example/devnet# git push 
… 
Git pull (download from remote repository) 
ccie@vm:~/git_example/devnet# git pull 
Already up-to-date. 
ccie@vm:~/git_example/devnet# 
>branch
ccie@vm:~/git_example/devnet# git branch 
* master 
ccie@vm:~/git_example/devnet# git checkout -b new_feature 
Switched to a new branch 'new_feature' 
ccie@vm:~/git_example/devnet# git branch 
  master 
* new_feature 
ccie@vm:~/git_example/devnet# 
ccie@vm:~/git_example/devnet# vi new_feature 
ccie@vm:~/git_example/devnet# git add new_feature 
ccie@vm:~/git_example/devnet# git status 
On branch new_feature 
Changes to be committed: 
  (use ""git reset HEAD <file>..."" to unstage) 
 
        new file:   new_feature 
 
ccie@vm:~/git_example/devnet# git commit -m ""New feature added in new_feature                                                                                                                                                              branch"" 
[new_feature f7136f2] New feature added in new_feature branch 
 1 file changed, 0 insertions(+), 0 deletions(-) 
 create mode 100644 new_feature 
ccie@vm:~/git_example/devnet# 
>merge
ccie@vm:~/git_example/devnet# git checkout -m master 
Switched to branch 'master' 
Your branch is up-to-date with 'origin/master'. 
ccie@vm:~/git_example/devnet# git merge new_feature 
Updating 68037eb..f7136f2 
Fast-forward 
 new_feature | 0 
 1 file changed, 0 insertions(+), 0 deletions(-) 
 create mode 100644 new_feature 
ccie@vm:~/git_example/devnet# 
>diff 
ccie@vm:~/git_example/devnet# git log | grep commit 
commit 92c2e79f508e8e363f3edb0e282ba856449681e7 
commit 68037eb7bc2e9d61d32d7fa4bdee1165deb21dd7 
…. 
ccie@vm:~/git_example/devnet# git diff 92c2e 68037eb 
diff --git a/New_File b/New_File 
deleted file mode 100644 
index bc8660a..0000000 
--- a/New_File 
+++ /dev/null 
@@ -1 +0,0 @@ 
-New File 
ccie@vm:~/git_example/devnet# 
```
### 1.2 Describe characteristics of API styles (REST and RPC)
>REST:REST is best described to work with the resources (e.g. user item in database)
>RPC:RPC is basically used to communicate across the different modules to serve user requests (e.g. SAP function)"
### 1.3 Describe the challenges encountered and patterns used when consuming APIs synchronously and asynchronously
>Synchronous API calls provide feedback immediately but might block the progamm while it executes ,asynchronous calls are sometimes queued and result might be retrieved with a callback function
### 1.4 Interpret Python scripts containing data types, functions, classes, conditions, and looping
> See https://realpython.com/python-data-types/
### 1.5 Describe the benefits of Python virtual environments
>Dependency for modules ensured, consistency of python version,workspace isloation
### 1.6 Explain the benefits of using network configuration tools such as Ansible and Puppet for automating IOS XE platforms
> idempodent configuration, no human error, auditable configuration changes, history when used with version control

## 10% 2.0 Automate APIs and Protocols
### 2.1 Identify the JSON instance based on a YANG model
```
"container ip {
	list vrf {
		description
		""Configure an IP VPN Routing/Forwarding
		instance"";
	leaf name {
		type string;
	}
	leaf rd {
		description
		""Specify Route Distinguisher"";
		type rd-type;
		}	
	}
}
```
###2.2 Identify the XML instance based on a YANG model
```
<ip>
	<vrf>
		<name>vrf_red</name>
			<rd>65000:1</rd>
	</vrf>
	<vrf>
		<name>vrf_green</name>
		<rd>65000:2</rd>
	</vrf>
</ip>
```
### 2.3 Interpret a YANG module tree generated per RFC8340
```
     module: ietf-network-instance
       +--rw network-instances
          +--rw network-instance* [name]
             +--rw name           string
             +--rw enabled?       boolean
             +--rw description?   string
             +--rw (ni-type)?
             +--rw (root-type)
                +--:(vrf-root)
                |  +--mp vrf-root"
```
### 2.4 Compare functionality, benefits, and uses of OpenConfig, IETF, and native YANG models
">Openconfig : operator-led YANG Models, models structure not aligned with the IETF,  pro:modules stay consistent - few github comitters, con: YANG modules change on regular basis
> IETF : defines common YANG modules for standard topics like interfaces,qos,ipv4,ipv6....
> Native : vendor-specific YANG models, different for each vendor"
### 2.5 Compare functionality, benefits, and uses of NETCONF and RESTCONF
">NETCONF better fit for distributed domain (routers and switches)
>RESTCONF better fit for 1:1 domain (controller north-bound API)
>https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2019/pdf/BRKNMS-2032.pdf"

## 20% 3.0 Network Device Programmability
### 3.1 Implement device management and monitoring using NetMiko
```
>>> from netmiko import ConnectHandler
>>> cisco = {
...    'device_type': 'cisco_ios',
...    'host': 'ios-xe-mgmt-latest.cisco.com',
...    'username': 'developer',
...    'password': 'C1sco12345',
...    'port': 8181
...    }
>>> net_connect = ConnectHandler(**cisco)
>>> output = net_connect.send_command(""show ip int brief"")
>>> output
'Interface              IP-Address      OK? Method Status                Protocol\nGigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      \nGigabitEthernet2       unassigned      YES NVRAM  administratively down down    \nGigabitEthernet3       unassigned      YES NVRAM  administratively down down    \nLoopback10             unassigned      YES unset  up                    up      '
>>>
```
### 3.2 Construct a Python script using ncclient that uses NETCONF to manage and monitor an IOS XE device
```
>>> with manager.connect(host='ios-xe-mgmt-latest.cisco.com', port=10000,
...                      username='developer', password='C1sco12345',hostkey_verify=False,
...                      device_params={'name':'iosxe'}) as m:
...     c = m.get_config(source='running').data_xml
...     print(c)
...
```
### 3.3 Configure device using RESTCONF API utilizing Python requests library
```
>>> requests.get(""https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface"",auth=('developer','C1sco12345'),verify=False).text
/root/env/lib/python3.7/site-packages/urllib3/connectionpool.py:988: InsecureRequestWarning: Unverified HTTPS request is being made to host 'ios-xe-mgmt-latest.cisco.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning,
'\n<interface xmlns=""http://cisco.com/ns/yang/Cisco-IOS-XE-native""  xmlns:ios=""http://cisco.com/ns/yang/Cisco-IOS-XE-native"">\n  <GigabitEthernet>\n    <name>1</name>\n    <description>MANAGEMENT INTERFACE - DON\'T TOUCH ME</description>\n    <ip>\n    <address>\n    <primary>\n      <address>10.10.20.48</address>\n      <mask>255.255.255.0</mask>\n    </primary>\n  </address>\n</ip>\n<mop>\n  <enabled>false</enabled>\n  <sysid>false</sysid>\n</mop>\n<negotiation xmlns=""http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet"">\n  <auto>true</auto>\n</negotiation>\n</GigabitEthernet>\n<GigabitEthernet>\n  <name>2</name>\n  <description>Network Interface</description>\n  <shutdown/>\n  <mop>\n    <enabled>false</enabled>\n    <sysid>false</sysid>\n  </mop>\n  <negotiation xmlns=""http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet"">\n    <auto>true</auto>\n  </negotiation>\n</GigabitEthernet>\n<GigabitEthernet>\n  <name>3</name>\n  <description>Network Interface</description>\n  <shutdown/>\n  <mop>\n    <enabled>false</enabled>\n    <sysid>false</sysid>\n  </mop>\n  <negotiation xmlns=""http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet"">\n    <auto>true</auto>\n  </negotiation>\n</GigabitEthernet>\n<Loopback>\n  <name>10</name>\n</Loopback>\n</interface>\n'
>>>
```
### 3.4 Utilize Ansible to configure an IOS XE device
>Review https://developer.cisco.com/learning/lab/ansible-overview/step/1
### 3.5 Configure a subscription for model driven telemetry on an IOS XE device (CLI, NETCONF,and RESTCONF)
>CLI:
```
Cat9300# show run | sec tel
telemetry ietf subscription 501
 encoding encode-kvgpb
 filter xpath /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds
 source-address 10.60.0.19
 source-vrf Mgmt-vrf
 stream yang-push
 update-policy periodic 500
 receiver ip address 10.12.252.224 57000 protocol grpc-tcp
 ```
>NETCONF:
```
<establish-subscription xmlns=""urn:ietf:params:xml:ns:yang:ietf-event-notifications"" 
xmlns:yp=""urn:ietf:params:xml:ns:yang:ietf-yang-push"">
    <stream>yp:yang-push</stream>
    <yp:xpath-filter>/cdp-ios-xe-oper:cdp-neighbor-details/cdp-neighbor-detail</yp:xpath-filter>
    <yp:dampening-period>0</yp:dampening-period>
</establish-subscription>
> RESTCONF:
URI:https://10.85.116.28:443/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data
Headers:
application/yang-data.collection+json, application/yang-data+json, application/yang-data.errors+json
Content-Type:
application/yang-data+json
BODY:
{
""mdt-config-data"": {
	""mdt-subscription"":[
	{
		""subscription-id"": ""102"",
		""base"": {
			""stream"": ""yang-push"",
			""encoding"": ""encode-kvgpb"",
                    ""period"": ""6000"",
			""xpath"": ""/memory-ios-xe-oper:memory-statistics/memory-statistic""
		}
        ""mdt-receivers"": {
            ""address"": ""10.22.23.48""
            ""port"": ""57555""
        }
	}
	]
}
}
```
### 3.6 Compare publication and subscription telemetry models
#### 3.6.a Periodic / cadence
>counters/measures
#### 3.6.b On-change
>state / configuration / identifieiers
### 3.7 Describe the benefits and usage of telemetry data in troubleshooting the network
>Push vs. pull model (inefficient), telemtry data is structured, open to standard big data tools
### 3.8 Describe Day 0 provisioning methods
#### 3.8.a iPXE
>Boot from network, DHCP+file, DHCP Option 60+61,next-server and bootfile,standard, os setup
#### 3.8.b PnP
>boot from device, DHCP+PnP protocol,No DHCP Options,Cisco proprietory, os setup + config apply
####3.8.c ZTP
>boot from device,  DHCP+file, DHCP Optin 60+61, DHCP Server option 67+150, standard,config apply

## 20% 4.0 Cisco DNA Center
### 4.1 Compare traditional versus software-defined networks
>centralized network provisioning vs. per-box mgmt
>control/data plane seperation vs. per-box decisions
>Northbound API access vs. per-box CLI/SNMP"

### 4.2 Describe the features and capabilities of Cisco DNA Center
>Secure access
>Simplified management
>Analytics capabilities
>Automation
> Central policy management
> API access : Northbound - Intent, Eastbound - Event Notification, Westbound - App integration, Southbound - Device interaction and multivendor/3rd party SDKs"
#### 4.2.a Network assurance APIs
> Network health
#### 4.2.b Intent APIs
>Authentication - Access Token Request
>Sites - Create sites, assign devices to them and get site health
>Topology - Get topology details and overall network health
>Devices - Manage network devices
>Clients - Get client (by MAC Address) health, status, and information
>Users - Obtain information about Users and associated connections and devices
>Issues - Obtain issue details, impacted hosts, and suggested actions for remediation
>Site Design - Design/provision NFV device to site/area/building/floor
>Network Settings - Manage Network Settings
>Software Image Management (SWIM) - Manage activation and distribution of software images
>Device Onboarding (PnP) - Zero-touch deployment of network devices
>Configuration Templates - Configure and manage CLI templates
>SDA - (BETA) Configure and manage SDA wired fabric border devices
>Non-Fabric Wireless - Configure and manage SSIDs, Wireless, and RF profiles in non-fabric wireless network
>Command Runner - Retrieve real-time device configuration and CLI keywords
>Network Discovery - Discover network devices and manage discovery jobs
>Path Trace - Network route and flow analysis
>File - Get configuration files by namespace and ID
>Task - Get information about asynchronous tasks
>Tag - Assign administrator-defined tags to network devices
>Application Policy - Create and manage applications, application sets, and application policies
>Event Management - Event based notification to external handlers
#### 4.2.c Multivendor support (3rd party SDKs)
> Review https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-platform-overview/multivendor-support-southbound
#### 4.2.d Events and notifications
> Review https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-platform-overview/integration-api-westbound
### 4.3 Implement Cisco DNA Center event outbound webhooks
> Review https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-platform-overview/events-and-notifications
### 4.4 Implement API requests for Cisco DNA Center to accomplish network management tasks
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text"
```
#### 4.4.a Intent APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/network-health"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text"
```
#### 4.4.b Command Runner APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
payload = {
        ""commands"": [
            ""show ip interface brief""
        ],
        ""deviceUuids"": [""de6477ad-22a2-4daa-9941-eb61cecefb34""]
    }
requests.post(""https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request"",auth=('devnetuser','Cisco123!'),data=json.dumps(payload),headers={'X-Auth-Token':token},verify=False).text
Not allowed on Sandbox but hey :)"
```
#### 4.4.c Site APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/site"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text"
```
#### 4.5 Implement API requests for Cisco DNA Center to accomplish network management tasks using these APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text"
```
#### 4.5.a Network discovery and device APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
>>> requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/discovery/count"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text
'{""response"":0,""version"":""1.0""}'
>>>
```
#### 4.5.b Template APIs (Apply a template)
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
# create project
request = {
  ""createTime"": 0,
  ""description"": ""string"",
  ""id"": ""string"",
  ""lastUpdateTime"": 0,
  ""name"": ""string"",
  ""tags"": [
    ""string""
  ],
  ""templates"": {}
}
requests.post(""https://sandboxdnac.cisco.com/dna/intent/api/v1/template-programmer/project"",data=json.loads(request),auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text
# Create template
request = {
  ""author"": ""string"",
  ""composite"": true,
  ""containingTemplates"": [
    {
      ""composite"": true,
      ""id"": ""string"",
      ""name"": ""string"",
      ""version"": ""string""
    }
  ],
  ""createTime"": 0,
  ""description"": ""string"",
  ""deviceTypes"": [
    {
      ""productFamily"": ""string"",
      ""productSeries"": ""string"",
      ""productType"": ""string""
    }
  ],
  ""failurePolicy"": ""ABORT_ON_ERROR"",
  ""id"": ""string"",
  ""lastUpdateTime"": 0,
  ""name"": ""string"",
  ""parentTemplateId"": ""string"",
  ""projectId"": ""string"",
  ""projectName"": ""string"",
  ""rollbackTemplateContent"": ""string"",
  ""rollbackTemplateParams"": [
    {
      ""binding"": ""string"",
      ""dataType"": ""STRING"",
      ""defaultValue"": ""string"",
      ""description"": ""string"",
      ""displayName"": ""string"",
      ""group"": ""string"",
      ""id"": ""string"",
      ""instructionText"": ""string"",
      ""key"": ""string"",
      ""notParam"": true,
      ""order"": 0,
      ""paramArray"": true,
      ""parameterName"": ""string"",
      ""provider"": ""string"",
      ""range"": [
        {
          ""id"": ""string"",
          ""maxValue"": 0,
          ""minValue"": 0
        }
      ],
      ""required"": true,
      ""selection"": {
        ""id"": ""string"",
        ""selectionType"": ""SINGLE_SELECT"",
        ""selectionValues"": {}
      }
    }
  ],
  ""softwareType"": ""string"",
  ""softwareVariant"": ""string"",
  ""softwareVersion"": ""string"",
  ""tags"": [
    ""string""
  ],
  ""templateContent"": ""string"",
  ""templateParams"": [
    {
      ""binding"": ""string"",
      ""dataType"": ""STRING"",
      ""defaultValue"": ""string"",
      ""description"": ""string"",
      ""displayName"": ""string"",
      ""group"": ""string"",
      ""id"": ""string"",
      ""instructionText"": ""string"",
      ""key"": ""string"",
      ""notParam"": true,
      ""order"": 0,
      ""paramArray"": true,
      ""parameterName"": ""string"",
      ""provider"": ""string"",
      ""range"": [
        {
          ""id"": ""string"",
          ""maxValue"": 0,
          ""minValue"": 0
        }
      ],
      ""required"": true,
      ""selection"": {
        ""id"": ""string"",
        ""selectionType"": ""SINGLE_SELECT"",
        ""selectionValues"": {}
      }
    }
  ],
  ""version"": ""string""
}
requests.post(""https://sandboxdnac.cisco.com/dna/intent/api/v1/template-programmer/project/{IdOutOfProjectCreation}/template"",data=json.loads(request),auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text
```
### 4.6 Troubleshoot Cisco DNA Center automation process using Intent APIs
```
token = requests.post(""https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"",auth=('devnetuser','Cisco123!'),verify=False).json()['Token']
requests.get(""https://sandboxdnac.cisco.com/dna/intent/api/v1/task"",auth=('devnetuser','Cisco123!'),headers={'X-Auth-Token':token},verify=False).text
```

## 20% 5.0 Cisco SD-WAN
### 5.1 Describe features and capabilities of Cisco SD-WAN vManage Certificate Management APIs
> Certificate Management - Managing certificates and security keys.
### 5.2 Implement a Python script to perform API requests for Cisco SD-WAN vManage Device Inventory APIs to retrieve and display data
```
import requests
requests.packages.urllib3.disable_warnings()
login_creds = {""j_username"":""devnetuser"",""j_password"":""Cisco123!""}
api_path = ""https://sandboxsdwan.cisco.com:8443""
sess = requests.session()
auth_resp = sess.post(api_path+""/j_security_check"", data=login_creds, verify=False)
result = sess.get(api_path+""/dataservice/device"")
result.json()
for device in result.json()['data']:
   print(""Device-Name:"" + device['host-name'] + "" - "" + device['system-ip'])"
```
### 5.3 Construct API requests for Cisco SD-WAN vManage Administration APIs
```
import requests
requests.packages.urllib3.disable_warnings()
login_creds = {""j_username"":""devnetuser"",""j_password"":""Cisco123!""}
api_path = ""https://sandboxsdwan.cisco.com:8443""
sess = requests.session()
auth_resp = sess.post(api_path+""/j_security_check"", data=login_creds, verify=False)
result = sess.get(api_path+""/dataservice/device"")
>>> result = sess.get(api_path+""/dataservice/admin/user"")
>>> result.text
'{""header"":{""generatedOn"":1598459636733,""viewKeys"":{""uniqueKey"":[],""preferenceKey"":""grid-AdminUser""},""columns"":[{""title"":""Name"",""property"":""description"",""hideable"":false,""dataType"":""string""},{""title"":""Username"",""property"":""userName"",""dataType"":""string""},{""title"":""User Groups"",""property"":""group"",""dataType"":""array""}],""fields"":[{""property"":""description"",""dataType"":""string""},{""property"":""userName"",""dataType"":""string""},{""property"":""group"",""dataType"":""array""}]},""data"":[{""userName"":""admin"",""group"":[]},{""userName"":""devnetuser"",""description"":""devnetuser"",""group"":[""sandbox""]}]}"
```
### 5.4 Implement a Python script to perform API requests for Cisco SD-WAN vManage Configuration >APIs to modify Cisco SD-WAN fabric configuration
>See https://developer.cisco.com/docs/sdwan/#!device-configuration
### 5.5 Construct API requests for Cisco SD-WAN vManage Monitoring APIs (Including real-time)
```
>>> result = sess.get(api_path+""/dataservice/device/omp/status"")
>>> result.text
'{""header"":{""generatedOn"":1598460228097},""data"":[{""type"":""omp"",""name"":""OMP"",""image"":""images/omp.png"",""count"":0,""detailView"":""dialog"",""detailsURL"":""/dataservice/device/omp/links"",""statusList"":[{""status"":""up"",""icon"":""images/connection/connection-network-up.png"",""color"":""b0e276"",""name"":""up"",""detailView"":""dialog"",""detailsURL"":""/dataservice/device/omp/links?state=up"",""count"":0},{""status"":""down"",""icon"":""images/connection/connection-network-down.png"",""color"":""fa7c7d"",""name"":""down"",""detailView"":""dialog"",""detailsURL"":""/dataservice/device/omp/links?state=down"",""count"":0}]}]}'
```
### 5.6 Troubleshoot a Cisco SD-WAN deployment using vManage APIs
```
>>> result = sess.get(api_path+""/dataservice/event/severity/summary"")
>>> result.text
'{""header"":{""generatedOn"":1598460498842,""viewKeys"":{""uniqueKey"":[],""preferenceKey"":""grid-DeviceEvent_histogram""},""columns"":[{""title"":""Event Time"",""property"":""entry_time"",""displayFormat"":""DD MMM YYYY h:mm:ss A z"",""inputFormat"":""unix-time"",""width"":200,""dataType"":""date""},{""title"":""Count"",""property"":""count"",""width"":150,""dataType"":""number""},{""title"":""Severity"",""property"":""severity_level"",""width"":150,""dataType"":""string""}],""fields"":[{""property"":""entry_time"",""dataType"":""date""},{""property"":""count"",""dataType"":""number""},{""property"":""severity_level"",""dataType"":""string""}],""chart"":{""xAxis"":[""entry_time""],""yAxis"":[""count""],""series"":[""severity_level""],""title"":""Events"",""xAxisLabel"":""Time"",""yAxisLabel"":""Count""}},""data"":[{""entry_time"":0,""count"":0.0,""severity_level"":""""}]}'
>>>
```
## 20% 6.0 Cisco Meraki
### 6.1 Describe features and capabilities of Cisco Meraki
>easy to install coud managed network gear
#### 6.1.a Location Scanning APIs
> send location data to webhooks abou locations data/observations (coordinates,ip,mac) / not configurable via API at this time (08/2020), validator required to authenticate
#### 6.1.b MV Sense APIs
> MV Sense Analytics for human count, live and history
#### 6.1.c External Captive Portal APIs
> Change/Update captive portal settings , provide external hosted captive portal on a own web server for customization
#### 6.1.d WebHook Alert APIs
>event driven alerts  / https://webhook.site/ is great for testing, API configurable, multiple receivers possible (e.g. configuration changes, rogue APs, VPN up down, network usage, gateway/repeater offline...)
#### 6.2 Create a network using Cisco Meraki APIs
```
# DevNet Sandbox API Key
headers = {""X-Cisco-Meraki-API-Key"": ""093b24e85df15a3e66f1fc359f4c48493eaa1b73""}
# Get first organization (no check on name or loop through organization for simplicity)
organization = requests.get(""https://api.meraki.com/api/v0/organizations/"",headers=headers).json()[0]['id']
>>> payload = { 'name': 'CCIE 32305 Network', 'organizationId': "" + organization + "", 'type': 'appliance'}
>>> requests.post(""https://api.meraki.com/api/v0/organizations/"" + organization + ""/networks"",data=payload,headers=headers)
<Response [403]>
>>> Unfortunately not allowed in Always-On DevNet Sandbox"
```
### 6.3 Configure a network using Cisco Meraki APIs
```
import requests
headers = {""X-Cisco-Meraki-API-Key"": ""093b24e85df15a3e66f1fc359f4c48493eaa1b73""}
# Get first organization (no check on name or loop through organization for simplicity)
organization = requests.get(""https://api.meraki.com/api/v1/organizations/"",headers=headers).json()[0]['id']
network = requests.get(""https://api.meraki.com/api/v1/organizations/"" + organization + ""/networks"",headers=headers).json()[0]['id']
payload = { 'name': 'CCIE 32305 Network (Updated)', 'organizationId': "" + organization + "", 'type': 'appliance'}
requests.put(""https://api.meraki.com/api/v1/networks/"" + network,data=payload,headers=headers)"
```
### 6.4 Implement a Python script for Cisco Meraki Alert WebHooks
```
from flask import Flask
from flask import request
app = Flask(__name__)
VALIDATOR = 'c8b77133f4bd2218df387186212a6e############'
@app.route('/', methods=['GET'])
def get():
    return VALIDATOR
@app.route('/', methods=['POST'])
def post():
    #do fancy stuff with posted data from Meraki
    print(request.json)

if __name__ == '__main__':
    app.run()
```
>Script opens a Webreceiver for Alert Webhooks , use ngrok to get a public HTTPS endpoint / can also be tested with https://webhook.site"
