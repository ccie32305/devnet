
# DEVASC Study Notes

Study notes which let me pass the DEVASC exam on 24th of Feb and made me DevNet 500
![DevNet 500](https://raw.githubusercontent.com/ccie32305/devnet/master/img/CiscoDevNet500.png "Devnet")

## 1.0 Software Development and Design - 15%

### 1.1 Compare data formats (XML, JSON, and YAML) 

```
XML:
<?xml version="1.0" encoding="UTF-8" ?>
	<device>
		<name>CCIE3235-Router-1</name>
		<interfaces>
			<name>Gi0/0</name>
			<ip>192.168.1.1/24</ip>
			<enabled>true</enabled>
		</interfaces>
		<interfaces>
			<name>Gi0/1</name>
			<ip>192.168.2.1/24</ip>
			<enabled>true</enabled>
		</interfaces>
	</device>
	
JSON:
{
	"device": {
		"name": "CCIE3235-Router-1",
		"interfaces": [
			{
				"name": "Gi0/0",
				"ip": "192.168.1.1/24",
				"enabled": true
			},
			{
				"name": "Gi0/1",
				"ip": "192.168.2.1/24",
				"enabled": true
			}
		]
	}
}
YAML:
device: 
    name: CCIE3235-Router-1
    interfaces:
       - name: Gi0/0 
         ip: 192.168.1.1/24
         enabled: True
       - name: Gi0/1
         ip: 192.168.2.1/24
         enabled: True
```

## 1.2 Describe parsing of common data format (XML, JSON, and YAML) to Python data structures
```
XML:
>>> xmltodict.parse(x)['device']['name']
u'CCIE3235-Router-1'
>>>
JSON:
>>> import json
>>> json.loads(j)['device']['interfaces'][0]['ip']
u'192.168.1.1/24'
>>>
YAML:
>>> import yaml
>>> yaml.load(y)['device']['name']		//yaml.safe_load available for more security (injection)
'CCIE3235-Router-1'
>>>
```
## 1.3 Describe the concepts of test-driven development
> write tests before coding (higher test coverage), improved code relevance, Limit work in process (WIP), improves maintainability

## 1.4 Compare software development methods (agile, lean, and waterfall)
>Waterfall : Defined stages, good when there are no changes->requirements are crystal clear, testing at the end

>Agile : Requirement,Design,Implement,Test,Delivery in one sprint (approx. 1-3 weeks), faster, less planning, frequent feedback from customer

>Lean/Kanban : Similar to Agile, reduces work in progress (no multitasking), oriented on the task, fast delivery

## 1.5 Explain the benefits of organizing code into methods / functions, classes, and modules

> methods/functions : breakdown code into less complex and more readable code, reduce repeatable/redundant code, easier troubleshooting

> Classes : represent attributes (e.g. human -> name, gender, eyecolor)

> Modules : separation of functions to allow for import into other projects for reuse

## 1.6 Identify the advantages of common design patterns (MVC and Observer)
> MVC: Separate functions of components in a application, Model : e.g. data structure, Controller e.g. interacts with data and view (user UI), View: user interface

> Observer: The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. (https://en.wikipedia.org/wiki/Observer_pattern)

## 1.7 Explain the advantages of version control

> Time travel (go back in time to earlier state), Logging and diffs (see what changed), required for CI/CD (basis for automation testing/delivery/integration), consistency, multiple branches/concurrent development
> 
### 1.8 Utilize common version control operations with Git
#### 1.8.a Clone
```
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
```
#### 1.8.b Add/remove
```
ccie@vm:~/git_example/devnet# git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
ccie@vm:~/git_example/devnet# echo "Hello" > New_file
ccie@vm:~/git_example/devnet# git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        New_file

nothing added to commit but untracked files present (use "git add" to track)
ccie@vm:~/git_example/devnet# git add New_file
ccie@vm:~/git_example/devnet# git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   New_file

ccie@vm:~/git_example/devnet# git reset HEAD New_file
ccie@vm:~/git_example/devnet# git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        New_file

nothing added to commit but untracked files present (use "git add" to track)
ccie@vm:~/git_example/devnet#
```
#### 1.8.c Commit
```
Git commit -m “my first commit” (add to local repository)
```
#### 1.8.d Push / Pull
```
Git push (upload to remote repository)
ccie@vm:~/git_example/devnet# git push
…
Git pull (download from remote repository)
ccie@vm:~/git_example/devnet# git pull
Already up-to-date.
ccie@vm:~/git_example/devnet#
```
### 1.8.e Branch
```
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
  (use "git reset HEAD <file>..." to unstage)

        new file:   new_feature

ccie@vm:~/git_example/devnet# git commit -m "New feature added in new_feature                                                                                                                                                              branch"
[new_feature f7136f2] New feature added in new_feature branch
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 new_feature
ccie@vm:~/git_example/devnet#
```
### 1.8.f Merge and handle conflicts
```
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
```
## 2.0 Understanding and Using APIs - 20%
### 2.1 Construct a REST API request to accomplish a task given API documentation
```python
[ccie@vm ~]$ curl http://api.icndb.com/jokes/random
{ "type": "success", "value": { "id": 166, "joke": "Chuck Norris doesn't play god. Playing is for children.", "categories": [] } }
[ccie@vm ~]$
```
### 2.2 Describe common usage patterns related to webhooks
> user-defined HTTP callbacks (e.g. webhooks can be used by APIs to give feedback to a definied “webhook” endpoint. For example used for chatbots)
### 2.3 Identify the constraints when consuming APIs
> Uniform interface : a resource should only have one URI

>Client-server : client application and server application must be able to evolve separately

>Stateless : no client context shall be stored on the server between requests

>Cacheable : caching should be used when possible

>Layered system : decouple API store of data and authentication
### 2.4 Explain common HTTP response codes associated with REST APIs
>200 OK, 204 No content, 301 Moved Permanently, 304 Not Modified, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 500 Internal Server Error, 501 Not implemented, 503 Service unavailable, 504 Gateway Timeout
### 2.5 Troubleshoot a problem given the HTTP response code, request and API documentation
```html
e.g. resource not found
GET /resource
HTTP/1.1 404 Not Found
Date: Sun, 18 Oct 1901 10:36:20 GMT
Server: Apache/1.2.14 (WinNT)
Content-Length: 230
Connection: Closed
Content-Type: text/html; charset=iso-8859-1

<html>
<body>
<h1>404</h1>
</body>
</html>
```
### 2.6 Identify the parts of an HTTP response (response code, headers, body)
```html
HTTP/1.1 404 Not Found				<= reponse code 404
Date: Sun, 18 Oct 1901 10:36:20 GMT		<= Header Start
Server: Apache/1.2.14 (WinNT)
Content-Length: 230
Connection: Closed
Content-Type: text/html; charset=iso-8859-1	<= Header Stop
						<= Body Start
<html>
<body>
<h1>404</h1>
</body>
</html>						<= Body Stop
```
### 2.7 Utilize common API authentication mechanisms: basic, custom token, and API keys
```
Basic : Username / Password authentication (e.g. DNA Center Token)
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
headers = {'Content-Type': 'application/json'}
auth = ('devnetuser', 'Cisco123!')
Token : Token usually retrieved via Basic Auth API Request (e.g DNA Center)
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
headers = {'Content-Type': 'application/json', 'X-Auth-Token': dna_token}
dna_devices = requests.get(url,headers=headers)
API Keys : Token provided by application / GUI / dashboard (e.g. Webex Teams)
headers = {"Authorization":"Bearer " + webex_token}
cisco_webex_teams_rooms = requests.get("https://api.ciscospark.com/v1/rooms", headers=headers)
```
### 2.8 Compare common API styles (REST, RPC, synchronous, and asynchronous)
>Synchronous: If an API call is synchronous, it means that code execution will block (or wait) for the API call to return before continuing. ... Asynchronous calls do not block (or wait) for the API call to return from the server. RPC. We are sending a message, and that might end up storing something in the database to keep a history, which might be another RPC call with possibly the same field names — who knows?

>REST. We are creating a message resource in the user’s messages collection. We can see a history of these easily by doing a GET on the same URL, and the message will be sent in the background.

### 2.9 Construct a Python script that calls a REST API using the requests library
```python
>>> import requests

>>> print(requests.get("http://api.icndb.com/jokes/random").json())

{'type': 'success', 'value': {'id': 62, 'joke': "Some people like to eat frogs' legs. Chuck Norris likes to eat lizard legs. Hence, snakes.", 'categories': []}}

>>>
```
## 3.0 Cisco Platforms and Development - 15%
### 3.1 Construct a Python script that uses a Cisco SDK given SDK documentation
```python
#SDK should simplify interaction with the given product with given functions/methods
>>> import dnacentersdk
>>> dnac = api.DNACenterAPI(base_url="https://dna.com,username="user",password=”pass)
>>> print(dnac.devices.get_device_list())
>
```
## 3.2 Describe the capabilities of Cisco network management platforms and APIs (Meraki, Cisco DNA Center, ACI, Cisco SD-WAN, and NSO)
> Meraki : Cloud-based network infrastructure, List Organizations, List Networks, List Devices, etc… (See API Doc)
Cisco DNA : Design, Policy, Provision, Assurance system for enterprise networks, List Devices, Add Devices etc. (See API Doc)

> ACI : data center fabric controlled by APIC (Cisco Application Policy Infrastructure Controller (APIC) providing central management, policy enforcements via EPGs and contracts, multisite, automated fabric provisioning capabilities, list EPGs (endpoint groups), list devices, list contracts, list application policies (See API Doc)
> 
> Cisco SD-WAN : Optimize WAN link usage taking application metrics into account, centrally managed with control/data plane separation, vManage is central component with REST API capabilities, List sites, List devices, modify WAN policies, (See API Doc)
> 
> NSO : Model-driven platform for automating network orechstration to simplify lifecycle management for hybrid networks,  Device Turnup, SDWAN/NFV Orchestration, ACL Management, QoS Management, Config Audit, OS Upgrades

### 3.3 Describe the capabilities of Cisco compute management platforms and APIs (UCS Manager, UCS Director, and Intersight)
>UCS Manager : managing cisco computing hardware (rack servers, blades, hyperflex etc.) – central management for server policies (RPC XML API)

> UCS Director : management/orchestration system for data centers including 3rd party systems like loadbalancers, vmware, storage etc. , (REST API)

> Intersight : SaaS compute management system (REST API)

### 3.4 Describe the capabilities of Cisco collaboration platforms and APIs (Webex Teams, Webex devices, Cisco Unified Communication Manager including AXL and UDS interfaces, and Finesse)
> Webex Teams : unified communication platform (chat, precense etc.) (REST API)

>Webex devices : Smartboards, video boards (REST xAPI)

>Cisco Unified Communication Manager (AXL, UDS,Finesse) : Call logic, PBX UDS uses REST API, AXL uses XML/SOAP, Finesse (Call Center call routing capability) uses REST AP(XML) and Javascript API

### 3.5 Describe the capabilities of Cisco security platforms and APIs (Firepower, Umbrella, AMP, ISE, and ThreatGrid)
> Firepower : next-generation firewall and IPS with centralized management (

> Umbrella : secure DNS for protection of roaming clients or networks (REST API)

> AMP : advanced malware protection for endpoints or networks (appliance firepower) (REST API)

> ISE : authentication and authorization server (REST API)

> ThreatGrid : malware sandboxing (REST API)

### 3.6 Describe the device level APIs and dynamic interfaces for IOS XE and NX-OS
> IOS-XE: REST API, NETCONF, RESTCONF

> NX-OS: NX-API CLI, NX-API REST, NETCONF, RESTCONF, Chef, Puppet
### 3.7 Identify the appropriate DevNet resource for a given scenario (Sandbox, Code Exchange, support, forums, Learning Labs, and API documentation)
>Sandbox : great to test scripts in a non productive environment

> Code Exchange : discover, learn, build and collaboration on curated GitHub projects to jumpstart own development, also good to get inspired

> Support forums : Engage with DevNet and community experts on technology-specific questions

> Learning Labs : learn more about network programmability

> API documentation : documentation about availability, usage, authentication to consume APIs
### 3.8 Apply concepts of model driven programmability (YANG, RESTCONF, and NETCONF) in a Cisco environment
> e.g. standard formats for interfaces to allow for management of different devices from different vendors
### 3.9 Construct code to perform a specific operation based on a set of requirements and given API reference documentation such as these:
#### 3.9.a Obtain a list of network devices by using Meraki, Cisco DNA Center, ACI, Cisco SD-WAN, or NSO
```python
>import requests
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
```
### 3.9.b Manage spaces, participants, and messages in Webex Teams
```python
>import os
import requests
webex_token = os.getenv('WEBEX_TOKEN')
headers = {"Authorization":"Bearer " + webex_token}
cisco_webex_teams_rooms = requests.get("https://api.ciscospark.com/v1/rooms", headers=headers)
for items in cisco_webex_teams_rooms.json()['items']:
   print(items['title'] + "," + items['id'])

message =  {"toPersonEmail":"toanyuser@cisco.com","text":"This is automated REST API generated message, that could have been send from anywhere Greetz CCIE 32305"}
send_message_cisco_webex = requests.post("https://api.ciscospark.com/v1/messages",json=message,headers=headers)
```

## 4.0 Application Deployment and Security - 15%
### 4.1 Describe benefits of edge computing
> Distribution of applications, Latency towards the user (performance), filter data locally reduce bandwidth usage, IoT use cases

### 4.2 Identify attributes of different application deployment models (private cloud, public cloud, hybrid cloud, and edge)

> private cloud : private compute service operated and installed usually by own organization where scale is limited by CAPEX expense (CAPEX model)

> Public cloud : compute service where cloud provider makes shared resources available to public internet with pay-as-you-go consume model, (almost) infinite scale, multi-tenancy and rich automation capabilities (OPEX model)

> Hybrid cloud : combined usage of public and private cloud

> Edge computing : compute ressources close to the consuming end devices, use cases in IoT space## Contributing
Feedback is always welcome

### 4.3 Identify the attributes of these application deployment types
4.3.a Virtual machines

> lower performance as bare metal because of shared ressources, abstraction of hardware

4.3.b Bare metal

> Legacy applications, more CPU usage

4.3.c Containers

> lower performance as virtual machines, shared OS, decouple programming dependencies

### 4.4 Describe components for a CI/CD pipeline in application deployments
> 1. Version control (e.g. git), 2. Continious integration (e.g. compile, validate, code review, unit testing integration testing), 3. Continious delivery (e.g. deploying the build application to test servers, performing UAT), 4. Continuous deploymen (e.g. deploying tested app on production)


### 4.5 Construct a Python unit test
```python
>>> import unittest
>>> class Test(unittest.TestCase):
...    def test_string_concentate(self):
...       self.assertEqual("a"+"b","ab")
...
>>> unittest.main()
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
(env) ccie@vm:~#
```
### 4.6 Interpret contents of a Dockerfile
```bash
#Basis for Docker images
#Dockerfile
FROM busybox
ENV foo /bar
WORKDIR ${foo}   # WORKDIR /bar
ADD . $foo       # ADD . /bar
COPY \$foo /quux # COPY $foo /quux
$ docker build . –tag ccie32305-docker-image
```

### 4.7 Utilize Docker images in local developer environment
```bash
ccie@vm:~# docker image ls | grep hello-world
hello-world latest fce289e99eb9 1 months ago 1.84kB
ccie@vm:~# docker run hello-world
```
### 4.8 Identify application security issues related to secret protection, encryption (storage and transport), and data handling
> secret protection : unhashed, unencrypted use of passwords within application, weak authentication of API calls, encryption : unencrypted delivery of content with HTTP, unencrypted storage of DB data, unhashed secrets, data handling : missing integrity checks on provided data

### 4.9 Explain how firewall, DNS, load balancers, and reverse proxy in application deployment
> firewall : can block in front of application to only allow HTTP/HTTPS traffic

>DNS : resolution from name to IP, also used for load balancing and intelligent web traffic routing (famous service is Route53)

>Load balancers : health checks on HTTP backends and balancing of HTTP requests to application backends.

>Reverse proxy : terminates HTTP connection and forwards to application backends. Can also facilitate SSL termination and web security features

### 4.10 Describe top OWASP threats (such as XSS, SQL injections, and CSRF)

> Injection : Injection flaws, such as SQL, NoSQL, OS, and LDAP injection, occur when untrusted data is sent to an interpreter as part of a command or query

>Broken Auth : unhashed passwords, reused session

>Sensitive Data Exposure : no encryption

>XML External Entities : mailicious code within XML <data>/etc/secrets</data>

>Broken Access Control : access ressources that are not allowed by user with no priviliges

>Security Misconfiguration : default configs admin-admin

>Cross-Site Scripting XSS : inject code that are executed by user

>Insecure Deserialization : change data in transit , integrity checking with hashing

>Using components with known vulnerabilities : Windows 7

>Insufficient logging & monitoring : Have you been hacked ? You might just don’t now.

  

> CSRF : Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious web site, email, blog, instant message, or program causes a user’s web browser to perform an unwanted action on a trusted site when the user is authenticated. A CSRF attack works because browser requests automatically include any credentials associated with the site, such as the user’s session cookie, IP address, etc. Therefore, if the user is authenticated to the site, the site cannot distinguish between the forged or legitimate request sent by the victim. We would need a token/identifier that is not accessible to attacker and would not be sent along (like cookies) with forged requests that attacker initiates / mitigate with Referer-Header

### 4.11 Utilize Bash commands (file management, directory navigation, and environmental variables)
> cd, dir, ls, pwd, echo „hello world”, echo “hello world” > make_new_file, echo “append hello” >> make_new_file, ls -all, man ls, cp, mv, rm, rm -rf, rmdir, export, export MYSECRET=SecurePassword, set, env, source env/bin/activate, deactivate

### 4.12 Identify the principles of DevOps practices
> Purpose : know what to build, business purpose,

>People : #NoSilos, unite through failure (learing by doing failures), team is responsible for the whole process

>Process : CI/CD example of DevOps process, Quality at the source (early automated testing), incremental improvements, early customer feedback

>Tools :, from development to integration and operation, automation

## 5.0 Infrastructure and Automation - 20%

### 5.1 Describe the value of model driven programmability for infrastructure automation
> CLI/Parser based automation could be consumed by humans easily, model driven programmability allows for standardized interfaces and configuration of network devices even with different vendors as the standardized models are easier to understand by programs or machines because of their structured data and formats.

## 5.2 Compare controller-level to device-level management
> controller-level management can abstract the interaction with “southbound” devices by providing a standard “northbound” API for network programmability. Device-level management can be consumed in case the devices provide a standard API (e.g. IOS XE, NX-OS)

## 5.3 Describe the use and roles of network simulation and test tools (such as VIRL and pyATS)
> VIRL : Virtual Internet Routing Lab – simulation of network components like routers, switches

>pyATS : testing and parsing framework for network programmability

## 5.4 Describe the components and benefits of CI/CD pipeline in infrastructure automation
> 1. Tests (Linting, Unit, System, Acceptance), 2. Manual (Continious Delivery) / Automatic deploy (Continous deployment)

## 5.5 Describe principles of infrastructure as code
> State declaration, abstraction, version control, idempotent (can be executed many times and not make unnecessary changes after the inital setup = declarative state)

## 5.6 Describe the capabilities of automation tools such as Ansible, Puppet, Chef, and Cisco NSO

> Ansible : agentless configuration and automation tool written in Python which can configure network devices to a defined state using playbooks written in YAML format

>Puppet : client-server(master)/agent-based configuration tool written in Ruby, defines desired state in manifests

>Chef : client server based configuration management tool written in Ruby using receipes to bring devices into desired state

>Cisco NSO : network orchestration tool abstract network device configuration with model-driven configuration/programmability

## 5.7 Identify the workflow being automated by a Python script that uses Cisco APIs including ACI, Meraki, Cisco DNA Center, or RESTCONF
>e.g. DevNet Ressources for example
## 5.8 Identify the workflow being automated by an Ansible playbook (management packages, user management related to services, basic service configuration, and start/stop)
>e.g. DevNet Ressources for example
## 5.9 Identify the workflow being automated by a bash script (such as file management, app install, user management, directory navigation)
>e.g. DevNet Ressources for example
## 5.10 Interpret the results of a RESTCONF or NETCONF query
>e.g. DevNet Ressources for example
## 5.11 Interpret basic YANG models
>e.g. DevNet Ressources for example
## 5.12 Interpret a unified diff
 >e.g. DevNet Ressources for example
## 5.13 Describe the principles and benefits of a code review process
> Format intendation, proper names, share knowledge, find bugs, check code is understandable, ensure code does what it supposed to do,collaborate on design,evolve application code, Not reviewing something that can be automated

## 5.14 Interpret sequence diagram that includes API calls
>e.g. DevNet Ressources for example

# 6.0 Network Fundamentals - 15%
### 6.1 Describe the purpose and usage of MAC addresses and VLANs
> MACs are used for physical addressing of network devices within a VLAN which provides logical virtualization of physical switches

## 6.2 Describe the purpose and usage of IP addresses, routes, subnet mask / prefix, and gateways
> IP addresses are used to identify systems in a network which are divided in networks where the boundaries are defined by their prefix and subnetmask and which are interconnected with gateways called routers
## 6.3 Describe the function of common networking components (such as switches, routers, firewalls, and load balancers)
> switches : forwards network packets on OSI layer 2, provides connectivity within LANs

> Routers : interconnect or “route” packets between subnets

> Firewalls : permit or deny traffic based on IP or TCP/UDP ports

> Load balancers : load share traffic for specific services towards different servers. Use case fault tolerance, performance, maintenance

## 6.4 Interpret a basic network topology diagram with elements such as switches, routers, firewalls, load balancers, and port values
> Just think of the most beautiful Visio that you’ve drawed

## 6.5 Describe the function of management, data, and control planes in a network device
> management : component to interact with management systems (e.g. CLI/SNMP)

>Data plane : ensures forwarding of the traffic (e.g. FIB)

>Control plane : ensures forwarding information distribution and convergence (e.g. OSPF)


## 6.6 Describe the functionality of these IP Services: DHCP, DNS, NAT, SNMP, NTP
> DHCP : Dynamic Host Configuration Protocol - IP address assignment (UDP/68), DNS : Domain Name System : Name<>IP address resolution (UDP/TCP 53), NAT: Network Address Translation, SNMP(UDP/TCP/161) Simple Network Management Protocol, NTP Network Time Protocol (UDP/TCP/123)

## 6.7 Recognize common protocol port values (such as, SSH, Telnet, HTTP, HTTPS, and NETCONF)
> SSH : 22, Telnet : 23, HTTP : 80, HTTPS : 443, NETCONF : 830
## 6.8 Identify cause of application connectivity issues (NAT problem, Transport Port blocked, proxy, and VPN)
> NAT problem : e.g. private IP tries to talk to public IP without NAT/PAT => no connection

>Transpor Port blocked : e.g. firewall blocks port 80 to web application server => no connection

>Proxy : e.g. Reverse proxy forwards traffic to a wrong web server backend => no connection

>VPN : e.g. due to VPN header involved MTU (Maximum transmission unit) is reached, traffic is dropped => no connection

## 6.9 Explain the impacts of network constraints on applications
> Latency : can result in slower application performance

>Packet loss : can result in slower application performance or even breaking the application

>Jitter : high jitter can result in broken application, especially visibile in real time communication like VoIP

>convergence : failure and reconvergence of the network can lead to performance or application interference

>routing issues : result in broken connectivity to applications

>ACL/firewall/packet filters : result in broken connectivity to applications

## Tips & Tricks
- Youtube and other online/video training vendors are very helpful
-  Watch videos with 1,5x speed to safe time
-  Use Python >3.6 to use easier string concatenation  
  ```
>>> another_variable = "DevNet"
>>> my_string = f"{another variable} rocks !!!"
>>> my_string
'DevNet rocks !!!'
>>>
>
```
- Get inspired by browsing through other Github projects

## Additional resources
- [Python for network engineers](https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2017/pdf/BRKSDN-1009.pdf)
- [YANG Data Modelling and NETCONF](https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2019/pdf/BRKNMS-2032.pdf)
- [Device APIs: The Force Awakens](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2016/pdf/BRKSDN-1119.pdf)
- [A Model-driven Approach to Software Defined Networks with Yang, NETCONF/RESTCONF](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2015/pdf/BRKSDN-1903.pdf)
- [DEVNET 1122 - Integrating Cisco Collaboration into Web Apps](https://www.youtube.com/watch?v=J_RUA5cZhwQ)
- [Introduction to Data Models and Cisco's NextGen Device Level APIs - DEVNET-1082](https://ciscolive.cisco.com/on-demand-library/?search=DEVNET-1082#/)
- [Introduction to RESTConf](https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2016/pdf/DEVNET-1081.pdf)
- [Using Cisco NSO With tail-f](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2016/pdf/LTRSPG-2515.pdf)
- [Is your Network working ?](https://www.youtube.com/watch?v=LbxfHWrujHc)
- [PyATS](https://www.youtube.com/watch?v=LxiBHPMves8&feature=emb_rel_end)
- [NSO](https://www.youtube.com/watch?v=-QZfxASrZXw&feature=emb_rel_end)
- [Python Skills and Techniques for network engineers Part 1](https://www.youtube.com/watch?v=VUTl8YdNtwE)
- [Cisco Intersight API with Postman](https://www.youtube.com/watch?v=LVs2TmuMI84)
- [ACI Cobra SDK](https://cobra.readthedocs.io/en/latest/install.html)
- [Arya, the (A)PIC (R)est p(Y)thon (A)dapter, assists with generating a Python Script using the Cobra libraries](https://github.com/datacenter/arya)
- [Cisco Umbrella API](https://www.youtube.com/watch?v=-hm3UbRsbRs&feature=youtu.be)
- [Cisco ISE API ](https://www.youtube.com/watch?v=CXYMAjsl52E)
- [Learn docker in 12 minutes](https://www.youtube.com/watch?v=YFl2mCHdv24)
- [Building a NetDevOps CI/CD Pipeline](https://www.youtube.com/watch?v=LinGy8DGIJ8)


## Contribution
Donate via Bitcoin -> 39Cb6RpuAoqWMSMXGT859PtHjDNTJpDKMp
![btc](https://raw.githubusercontent.com/ccie32305/devnet/master/img/btc.png "BTC")

 or 

[Twitter](https://twitter.com/ccie32305/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
