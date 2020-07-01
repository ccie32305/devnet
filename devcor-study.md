# DEVCOR Study Notes
Study notes which let me pass the DEVASC exam

# 1.0 Software Development and Design
### 1.1 Describe distributed applications related to the concepts of front-end, back-end, and load balancing
* Review https://www.clariontech.com/blog/cloud-computing-architecture-what-is-front-end-and-back-end

### 1.2 Evaluate an application design considering scalability and modularity
* Review monolithic, SOA, microservices architectures

### 1.3 Evaluate an application design considering high-availability and resiliency (including onpremises, hybrid, and cloud)
* Review https://www.getfilecloud.com/blog/an-introduction-to-high-availability-architecture/

### 1.4 Evaluate an application design considering latency and rate limiting
* Review https://devops.com/how-to-minimize-latency-and-its-impact-on-ux/

### 1.5 Evaluate an application design and implementation considering maintainability
* Review https://labs.sogeti.com/software-maintainability-in-the-cloud-era/

### 1.6 Evaluate an application design and implementation considering observability
* Observability is achieved when data is made available from within the system that you wish to monitor. Monitoring is the actual task of collecting and displaying this data

### 1.7 Diagnose problems with an application given logs related to an event
* Review https://developer.cisco.com/docs/control-center/#!rest-api-troubleshooting-checklist

### 1.8 Evaluate choice of database types with respect to application requirements (such as relational, document, graph, columnar, and Time Series)
* relational : e.g. MySQL, fixed field structure based on schema, (ACID : atomic (do all or none) - consistent (valid before and after) - isolation (no one sees half complete tasks) - durable (when it's done it stays done)), CRUD (Create, Read, Update, Delete) with SQL language, joins etc. 
* document : e.g. MongoDB , fields can be easily added, no fixed schema, NoSQL, arguments : speed,scaling, cost graph : e.g. Neo4j, used for network diagram representation, twitter 
* columnar : e.g. MariaDB data aggregation from many records 
* time series : e.g. InfluxDB, telemetry data, monitoring and performance logging, IoT 
* NewSQL : e.q. take from RDBMS : relational model and SQL queries, take from NoSQL : performance, scaling, distribution
### 1.9 Explain architectural patterns (monolithic, services oriented, microservices, and event driven)
* Monolithic : scaling only possible with additional CPU,memory ressources,the software’s parts are unified and all its functions are managed in one place
* Service Oriented : service-oriented architecture (SOA) is a software architecture style that refers to an application composed of discrete and loosely coupled software agents that perform a required function
* Microservices : seperate in losely coupled services, allows horizontal scaling and replacement of services
* Event driven : In an event-driven application, there is generally a main loop that listens for events, and then triggers a callback function when one of those events is detected Event notification: Decouple sender and receiver  Event-carried state transfer: This pattern shows up when you want to update clients of a system in such a way that they don't need to contact the source system in order to do further work Event-Sourcing : rebuilt the actual state out of event logs, like git can rebuild code from all the commits CQRS : The Command and Query Responsibility Segregation (CQRS) pattern separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security. The flexibility created by migrating to CQRS allows a system to better evolve over time and prevents update commands from causing merge conflicts at the domain level.

### 1.10 Utilize advanced version control operations with Git
#### 1.10.a Merge a branch
* create a new branch named "feature_x" and switch to it using
git checkout -b feature_x
switch back to master
git checkout master
and delete the branch again
git branch -d feature_x
a branch is not available to others unless you push the branch to your remote repository
git push origin <branch>
update & merge_x000D_
to update your local repository to the newest commit, execute_x000D_
git pull_x000D_
in your working directory to fetch and merge remote changes._x000D_
to merge another branch into your active branch (e.g. master), use_x000D_
git merge <branch>_x000D_
in both cases git tries to auto-merge changes. Unfortunately, this is not always possible and results in conflicts. You are responsible to merge those conflicts manually by editing the files shown by git. After changing, you need to mark them as merged with_x000D_
git add <filename>_x000D_
before merging changes, you can also preview them by using_x000D_
git diff <source_branch> <target_branch>
#### 1.10.b Resolve conflicts
* See https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line
#### 1.10.c git reset
* "use git reset HEAD <file>..." to unstage / opposite of git add
#### 1.10.d git checkout
* use "git checkout -- <file>..." to discard changes in working directory / file modified but not added/commited etc.
#### 1.10.e git revert
* Revert a commit with a new commit to undo the changes to keep history intact
```
root@vm49:~/devnet# git revert ab698a5ffe147ca66f785a42e7e86a7cc0e40403
root@vm49:~/devnet# git log --stat
commit 83e34a24b86254d5a6d81c812ada28a8283f2c72
Author: Phil <ccie32305@github.com>
Date:   Mon Jun 29 18:34:17 2020 +0200

    Revert "Prepare for DEVCOR"

    This reverts commit ab698a5ffe147ca66f785a42e7e86a7cc0e40403.

 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit ab698a5ffe147ca66f785a42e7e86a7cc0e40403
Author: Phil <ccie32305@github.com>
Date:   Mon Jun 29 18:33:18 2020 +0200

    Prepare for DEVCOR

 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)


root@vm49:~/devnet# git reflog
83e34a2 HEAD@{0}: revert: Revert "Prepare for DEVCOR"
ab698a5 HEAD@{1}: commit: Prepare for DEVCOR
866d760 HEAD@{2}: pull: Merge made by the 'recursive' strategy.
1403af3 HEAD@{3}: commit: Added images
077368f HEAD@{4}: pull: Fast-forward
be13be1 HEAD@{5}: commit: Added Meraki example to list all clients of a network
68037eb HEAD@{6}: commit: API Snippets with Cisco Webex Teams
acf0a1c HEAD@{7}: commit: ACI Snippet added
90f5aec HEAD@{8}: commit: Added SD WAN test snippet
0cbef7a HEAD@{9}: commit: Another useful commit
11dacfe HEAD@{10}: commit: New file for commit
f27442e HEAD@{11}: commit: Adjusted README
d592d1a HEAD@{12}: pull: Fast-forward
06ac533 HEAD@{13}: checkout: moving from newcomment to master
d592d1a HEAD@{14}: checkout: moving from d592d1a44e427b6b18343174a45d4a4090e7882f to newcomment
d592d1a HEAD@{15}: merge newcomment: Fast-forward
06ac533 HEAD@{16}: checkout: moving from newcomment to origin/master
d592d1a HEAD@{17}: commit: New branch
06ac533 HEAD@{18}: checkout: moving from master to newcomment
06ac533 HEAD@{19}: commit: First DNA Center request
8cc5f69 HEAD@{20}: pull: Fast-forward
c4ce745 HEAD@{21}: commit: Start Devnet Repo
b88a75a HEAD@{22}: clone: from https://github.com/ccie32305/devnet.git
root@vm49:~/devnet#
```
### 1.11 Explain the concepts of release packaging and dependency management
MISSING

### 1.12 Construct a sequence diagram that includes API calls
* See https://developers.google.com/pay/passes/guides/overview/about/typical-api-flow?hl=de

## 2.0 Using APIs

### 2.1 Implement robust REST API error handling for time outs and rate limits

* unrecoverable error handling : e.g. HTTP reply 404 / 500 / etc
* rate limits : e.g. HTTP reply 429
* timeout : e.g. timout of requets
```
try:
    req = requests.request('GET', 'https://www.cisco.com',timeout=(1,1))_x000D_
    print(req)_x000D_
except requests.ReadTimeout:_x000D_
    print("READ TIME OUT")
pagination : API results in batches or "pages" where you browse with prev/next (for example Meraki or Cisco Prime APIs)
```

### 2.2 Implement control flow of consumer code for unrecoverable REST API errors
```
if resp.status_code <> 200:
    print ('Let's do some control flow of consumer code for unrecoverable REST API errors here :)')
else:
    print ('All Good')
```

### 2.3 Identify ways to optimize API usage through HTTP cache controls
* HTP Caching : Cache-control public with max-age or expires, Cache-control private 
* Cache-control no-store, Cache-control absent (heuristic-based caching)
* CDN : goal is to provide high availability and performance by distributing the service spatially relative to end users

### 2.4 Construct an application that consumes a REST API that supports pagination
```
e.g.
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=0>; rel=first, _x000D_
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=146>; rel=prev, _x000D_
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=0>; rel=last
```

### 2.5 Describe the steps in the OAuth2 three-legged authorization code grant flow

* Three-legged OAuth authorization gets its name because in involves three different parties to get you an access token: your application, the ORCID OAuth service, and the user
* Components : Protected Resource server  (HTTP API), Client (requesting application) , resource owner (the user), authorization server

* Client Application -> Authorization Request -> Resource Owner
Resource Owner <- Authorization and consent -> Authorization Server
Resource Owner -> Authorization Grant -> Client Application
Client Application -> Authorization Grant -> Authoriuzation Server
Authorization Server -> Access Token -> Client Application
Client Application -> Request -> Protected Resource server 
Authorization Server <- Trust -> Protected Resource server

* HTTP Flow :
1) Authorization Request : https://auth.com/authorize?response_type=code&client_id=1hfasd8h0&redirect_uri=https://client.example.com/callback&state=xyz
2) Authorization Response : https://client.example.com/callback?code=sdoifho3hz08h&state=xyz
3) Token Request : POST /token Host: server.example.com Content-Type: application/x-www-form-urlencoded, Authorization: Basic hroweihosidhfosidhf, grant_type=authorization_code&code=sdoifho3hz08h&client_id=1hfasd8h0&client_secret=qweoipwqpe
4) Token Response : HTTP 200 OK, Conten-Type : application/ json, { "access_token" : "abcde", "token_type": "Bearer", "expires_in" : 3600 }

## 3.0 Cisco Platforms
### 3.1 Construct API requests to implement chatops with Webex Teams API

1) Create Bot via https://developer.webex.com/my-apps/new/bot
2) Save access token : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxjYzIxYzIzZDk5ODJiYTFlYTctNWYy_PF84_consumer
3) Add contact in Webex Teams : devcor@webex.bot
4) Python
```
import requests
import time
processedmessage = ""
headers = {'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxjYzIxYzIzZDk5ODJiYTFlYTctNWYy_PF84_consumer'}
roomid = requests.get("https://webexapis.com/v1/rooms",headers=headers).json()['items'][0]['id']
while True:
   lastmessage = requests.get("https://webexapis.com/v1/messages?roomId=" + roomid,headers=headers).json()['items'][0]['text']
   lastlastmessage = requests.get("https://webexapis.com/v1/messages?roomId=" + roomid,headers=headers).json()['items'][1]['text'] 
   print("Lastmessage:" + lastmessage + "\n")
   if lastmessage != processedmessage and lastlastmessage != processedmessage:
      requests.post("https://webexapis.com/v1/messages",headers=headers,data={"roomId":roomid,"text":"Yes i will process your request, "+ lastmessage})
      print("Processedmessage:" + processedmessage + "\n")
      print("Lastmessage:" + lastmessage + "\n")
      processedmessage = lastmessage
   time.sleep(1)
```

### 3.2 Construct API requests to create and delete objects using Firepower device management (FDM)
```
// Get token 
headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
payload = {
  "grant_type": "password",
  "username": "admin",
  "password": "Cisco1234"
}
token = requests.post(
        f"https://10.10.20.65/api/fdm/v5/fdm/token",
        headers=headers,
        json=payload,
        verify=False,
    ).json()['access_token']

// List object
headers['Authorization'] = "Bearer " + token
list = requests.get(
        f"https://10.10.20.65/api/fdm/v5/object/networks",
       headers=headers,
        verify=False,
    )

// Create object
new_object = {
  "name": "CCIE32305",
  "description": "CCIE32305-rocks",
  "subType": "HOST",
  "value": "192.168.3.254",
  "dnsResolution": "IPV4_ONLY",
  "type": "networkobject"
}

create = requests.post(
        f"https://10.10.20.65/api/fdm/v5/object/networks",
       headers=headers,
json=new_object,
        verify=False,
    )


//Delete object
delete = requests.delete(
        f"https://10.10.20.65/api/fdm/v5/object/networks/{create.json()['id']}",
       headers=headers,
json=new_object,
        verify=False,
    )
```
### 3.3 Construct API requests using the Meraki platform to accomplish these tasks
#### 3.3.a Use Meraki Dashboard APIs to enable an SSID
```
>>> HEADERS = {'X-Cisco-Meraki-API-Key': '482e288015b0df6e955b0397febaf45cfd9d788c'}
>>> requests.get("https://api.meraki.com/api/v0/organizations/739153288842183042/networks/L_739153288842204423/ssids/1",headers=HEADERS).json()
{'authMode': 'open', 'perClientBandwidthLimitUp': 0, 'ipAssignmentMode': 'NAT mode', 'bandSelection': 'Dual band operation', 'minBitrate': 11, 'splashPage': 'None', 'number': 1, 'perClientBandwidthLimitDown': 0, 'availableOnAllAps': True, 'enabled': True, 'visible': True, 'ssidAdminAccessible': False, 'name': 'Test', 'availabilityTags': []}
>>> DATA = {'enabled': 'False'}
>>> requests.put("https://api.meraki.com/api/v0/organizations/739153288842183042/networks/L_739153288842204423/ssids/1",headers=HEADERS,data=DATA).json()
{'authMode': 'open', 'perClientBandwidthLimitUp': 0, 'ipAssignmentMode': 'NAT mode', 'bandSelection': 'Dual band operation', 'minBitrate': 11, 'splashPage': 'None', 'number': 1, 'perClientBandwidthLimitDown': 0, 'availableOnAllAps': True, 'enabled': False, 'visible': True, 'ssidAdminAccessible': False, 'name': 'Test', 'availabilityTags': []}
>>> requests.get("https://api.meraki.com/api/v0/organizations/739153288842183042/networks/L_739153288842204423/ssids/1",headers=HEADERS).json()
{'authMode': 'open', 'perClientBandwidthLimitUp': 0, 'ipAssignmentMode': 'NAT mode', 'bandSelection': 'Dual band operation', 'minBitrate': 11, 'splashPage': 'None', 'number': 1, 'perClientBandwidthLimitDown': 0, 'availableOnAllAps': True, 'enabled': False, 'visible': True, 'ssidAdminAccessible': False, 'name': 'Test', 'availabilityTags': []}
>>> DATA = {'name': 'Changed_By_API'}
>>> requests.put("https://api.meraki.com/api/v0/organizations/739153288842183042/networks/L_739153288842204423/ssids/1",headers=HEADERS,data=DATA).json()
{'authMode': 'open', 'perClientBandwidthLimitUp': 0, 'ipAssignmentMode': 'NAT mode', 'bandSelection': 'Dual band operation', 'minBitrate': 11, 'splashPage': 'None', 'number': 1, 'perClientBandwidthLimitDown': 0, 'availableOnAllAps': True, 'enabled': False, 'visible': False, 'ssidAdminAccessible': False, 'name': 'Changed_By_API', 'availabilityTags': []}
>>>
```
#### 3.3.b Use Meraki location APIs to retrieve location data
1) Write python flask webserver (meraki.py)
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
2) Run python flask app on port 5000 (python meraki.py)
3) Publish the app with ngrok  (./ngrok http -inspect=false 5000)
4) Add the URL under Network-wide settings -> General -> Location and scanning Post URLS and validate (e.g. https://001412ab8d35.ngrok.io/)
5) Wait for Location Data incoming

#### 3.4 Construct API calls to retrieve data from Intersight
1) Start Intersight DevNet Sanbox
2) Add UCSE to Intersight
3) Generate API Key and secret in Intersight
4) Save API secret in "intersight.key" file
5) git clone https://github.com/movinalot/intersight-rest-api
6) pip install six
7) pip install cryptography
8) Python
```
>>> import requests
>>> from intersight_auth import IntersightAuth
>>> AUTH = IntersightAuth(api_key_id='5ee796ae7564612d330029e7/5ee796ae7564612d330029f4/5ee7a69d7564612d30871000',secret_key_filename='intersight.key')
>>> r = requests.get("https://www.intersight.com/api/v1/compute/PhysicalSummaries",auth=AUTH)
>>> r.json()['Results'][0]['Name']
'UCSPE-10-10-20-40-9'
>>>
```
### 3.5 Construct a Python script using the UCS APIs to provision a new UCS server given a template
1)Connect to DevNet Sandbox via VPN and to CentOS via SSH
2)pip install ucsmsdk
3)Python
```
>>> from ucsmsdk.ucshandle import UcsHandle
>>> handle = UcsHandle("10.10.20.40", "ucspe", "ucspe")
>>> handle.login()
True
>>> handle.ucs
'UCSPE-10-10-20-40'
>>> handle.ip
'10.10.20.40'
>>> handle.add_mo(LsServer(parent_mo_or_dn="org-root", name="sp_demo"))
>>> handle.commit()
```
Not a 100% correct but could not find better tutorials/examples

### 3.6 Construct a Python script using the Cisco DNA center APIs to retrieve and display wireless health information
```
import requests
import time
token = requests.post("https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token",auth=('devnetuser','Cisco123!')).json()['Token']
clienthealth = requests.get("http://sandboxdnac.cisco.com/dna/intent/api/v1/client-detail",params={'macAddress' : '00:1E:13:A5:B9:40','timestamp' : round(time.time() * 1000)},headers={"X-Auth-Token": token})
print(clienthealth.json()['detail']['clientConnection'])
```
### 3.7 Describe the capabilities of AppDynamics when instrumenting an application
* Agent-based application performance management tool
* Anomaly detection (against baseline application performance)
* improves observability
* infos for different departments like biz,dev and ops
* Architecture with central controller (UI) and decentral app and database agent

### 3.8 Describe steps to build a custom dashboard to present data collected from Cisco APIs
* Subscribe to telemetry data via NETCONF MDT subscription  or grab data via other Cisco APIs ->  Add data to Elastisearch tool or InfluxDB -> Visualize data with Kibana / Grafana
* DevNet example : CLI or YANG -> gRPC Dial-Out -> telegraf -> InfluxDB -> Grafana
* ELK Stack = Elasticsearch (apache Lucene based search engine open source Java) / Logstash (tool for collecting & monitoring logs for remote machines, data pipeline for elasticsearch) / Kibana (data visualization)

## 4.0 Application Deployment and Security
### 4.1 Diagnose a CI/CD pipeline failure (such as missing dependency, incompatible versions of components, and failed tests)
* missing dependency - e.g. failed import of python modules, failed installation of requirements / pip freeze, failed build/compile
* incompatible versions of components - e.g. updated APIs, incompatible python2/python3 formatting
* failed tests - e.g. unittests failure, linting test failures

### 4.2 Integrate an application into a prebuilt CD environment leveraging Docker and Kubernetes
See https://docs.docker.com/docker-for-mac/kubernetes/#:~:text=The%20Kubernetes%20server%20runs%20within,not%20affect%20your%20other%20workloads.

### 4.3 Describe the benefits of continuous testing and static code analysis in a CI pipeline
* static code analysis : provides insight into code without executing it, executes quickly, can automate maintaining code, finding securtiy issues or bugs, code styling analysis, security linting (password leaks), error detection, UML diagram creation, duplicate code detection, complexity analysis, comment styling analysis, unused code analysis, framework best practices analysis . Tools -> Prospector, Bandit, PyLint

### 4.4 Utilize Docker to containerize an application
```
root@ccie32305:~/devnet/docker-hello-world# cat docker-flask-hello-world.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
     return 'Hello, World!'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
root@ccie32305:~/devnet/docker-hello-world# cat Dockerfile
FROM python
COPY . /app
WORKDIR /app
RUN pip install flask
CMD python /app/docker-flask-hello-world.py
EXPOSE 5000/tcp
root@ccie32305:~/devnet/docker-hello-world# docker build . -t ccie32305
Sending build context to Docker daemon  4.096kB
Step 1/6 : FROM python
 ---> 7f5b6ccd03e9
Step 2/6 : COPY . /app
 ---> Using cache
 ---> 27bed2894ee8
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> 4d13cc237530
Step 4/6 : RUN pip install flask
 ---> Using cache
 ---> fc8f705edf8e
Step 5/6 : CMD python /app/docker-flask-hello-world.py
 ---> Using cache
 ---> ce771b5b266d
Step 6/6 : EXPOSE 5000/tcp
 ---> Using cache
 ---> 8f53ed36bdc3
Successfully built 8f53ed36bdc3
Successfully tagged ccie32305:latest
root@ccie32305:~/devnet/docker-hello-world# docker run -P -d ccie32305
5ba6078f11c16e0a3deb84b9fe0661191576f6d0e3f2c14d3b76d1d7c2ba8c82
root@ccie32305:~/devnet/docker-hello-world# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
5ba6078f11c1        ccie32305           "/bin/sh -c 'python …"   2 seconds ago       Up 1 second         0.0.0.0:32771->5000/tcp   blissful_hermann
root@ccie32305:~/devnet/docker-hello-world# telnet 127.0.0.1 32771
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
GET /

Hello, World!Connection closed by foreign host.
root@ccie32305:~/devnet/docker-hello-world# docker kill 5ba6078
5ba6078
root@ccie32305:~/devnet/docker-hello-world#
```
### 4.5 Describe the tenets of the "12-factor app"
*  Codebase : one single codebase for an app, multiple deploys like prod,staging,dev
* dependencies :twelve-factor app never relies on implicit existence of system-wide packages
* config : config is everything that is likely to vary between deploys, no store of config in app code 
* backing services : code for a twelve-factor app makes no distinction between local and third party services
* Build,release,run : Strictly separate build and run stages
* processes : Twelve-factor processes are stateless and share-nothing. Any data that needs to persist must be stored in a stateful backing service, typically a database.Sticky sessions are a violation of twelve-factor and should never be used or relied upon. 
* Port binding : The twelve-factor app is completely self-contained and does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port.
* Concurrency : enables scale out of a twelve factor app, e.g. HHTTP requests handeled by web process.1.2.3.4, background tasks by worker process.1.2.3.4..... 
* Disposability : stateless, easy on/off switch,twelve-factor app’s processes are disposable, meaning they can be started or stopped at a moment’s notice. This facilitates fast elastic scaling, rapid deployment of code or config changes, and robustness of production deploys.
* dev/prod parity : twelve-factor app is designed for continuous deployment by keeping the gap between development and production small, Backing services, such as the app’s database, queueing system, or cache, is one area where dev/prod parity is important.
* logs : Logs provide visibility into the behavior of a running app
* admin processes: One-off admin processes should be run in an identical environment as the regular long-running processes of the app. They run against a release, using the same codebase and config as any process run against that release. Admin code must ship with application code to avoid synchronization issues.

### 4.6 Describe an effective logging strategy for an application
```
import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Not a logging strategy but CCIE32305 rocks")
```

### 4.7 Explain data privacy concerns related to storage and transmission of data
* user have rights on how their data is processed, privacy notes can tell the user how companies handle their data, personal data can be subject to legal requirements and are not allowed to be consumed

### 4.8 Identify the secret storage approach relevant to a given scenario
* Config files : easiest to implement, might expose user/pass
* Environment : store username passwords in environment variables / easy to implement / no rotation of credentials
* API Keys : revocation of access possible / no exposure of username/passwords / different API keys for different privileges
* secret management tools : e.g. Hashicorp Vault, Azure Key Vault, AWS KMS - auditable, more secure, rotation of secrets possible, secrets lifecycle, versioning, possiblity for short lifed secrets
* HSM : hardware based key management system

### 4.9 Configure application specific SSL certificates
```
e.g. self-signed certificate
openssl genrsa -des3 -passout pass:x -out server.pass.key 2048
...
openssl rsa -passin pass:x -in server.pass.key -out server.key
writing RSA key
rm server.pass.key
openssl req -new -key server.key -out server.csr
...
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
...
A challenge password []:
...
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
```
### 4.10 Implement mitigation strategies for OWASP threats (such as XSS, CSRF, and SQL injection)
* XSS : Escape, validate and sanitize user inpt, encode and identify output responses, use ORM, never simply reflect untrusted data
* CSRF : crafted attacker requests, Defences : Use HTTP Header, Flask-WTF adds CSRF-support, random CSRF-Token, valid reqests don't originate externally
* SQL injection : whitelist input data, separate the query from the input data, segment accounts for admin and public (apply least priviliges)
* Broken authenticaion and session management : auth coockie, session or credential theft, use HTTPs, expire sessions, allow stron passwords, implement login rate limiting and lockouts
* Insecure Direct Object References : pulling data where the attacker should not have access to, http://www.bank.com/account?id=12345, don't expose internal keys, explicit about who can access resources, incrementing integers are enumerable, natural keys are discoverable
* Security misconfiguration : out of date software, unecessary ports,services, account privileges, default accounts passwords, error handling exposing information, security settings not set secure, 
* Defences : turn off features, least privilege model, ensure production ready configuration
* Sensitive data exposure : insufficient use of SSL, bad crypto, other exposure (URLs,logs,browser autocomplete), Defences : reduce window of storage, cannot lose what you don't have, HTTPS everywhere, hashing of passwords
* Missing function level access control : UI shows navigation to unauthorised function, server side authentication or authorisation checks missing, checks rely on information from the attacker, system or diagnostics accessible without proper authorisation, Defences : use roles and apply membership, check for forced browsing /admin, test unprivileged roles (including POST requests async calls and capture and replay priviliged requests)
* Using components with known vulnerabilities : exploitation of vulnerable components : Defences : keep track of components and versions, monitor CVEs impacting the components, use framework package management, monitor new releases
* Unvalidated redirects and forwards : Inject redirects to vulnerable websites, Defences : whitelist redirect URLS, pass an ID to redirect instead o URL, check the referrer


### 4.11 Describe how end-to-end encryption principles apply to APIs
* SSL : Digital certificates, data confidentiality and integriy, end-to-end-encryption
* Prevent injects or replay attacks

## 5.0 Infrastructure and Automation
### 5.1 Explain considerations of model-driven telemetry (including data consumption and data storage)
* Dial-in (dynamically initated by manager / manager reestablishes if session breaks) / dial-out  (statically configured on device, device reestablishes if session breaks) - no polling in MDT
* On-Change - When events are published on-change as an event occurs, like when the OSPF neighbour changes.pow  
* Periodic - When events are published at a pre-defined time-based interval, like every 30 seconds.

### 5.2 Utilize RESTCONF to configure a network device including interfaces, static routes, and VLANs (IOS XE only)
GET data/ietf-routing/static
HTTP 200 OK { json-data }
POST data/ietf-routing/static {JSON}
HTTP 201 CREATED

### 5.3 Construct a workflow to configure network parameters with:
#### 5.3.a Ansible playbook
```
Ansible components 
> Modules : written in python , typically copied to remote hosts and run by the Ansible tool. Ansible modules are referenced as tasks in Ansible playbooks or using CLI arguments in the Ansible ad-hoc CLI tool
> Inventory files : contain the hosts operated by Ansible
> Playbooks : are written in YAML and contain Ansible (DSL) domain specific language
> Configuration files : control how the tool runs
> variables : ........

root@vm49:~# ansible-playbook helloworld.yml

---
# This playbook prints a simple debug message
- name: Echo 
  hosts: 127.0.0.1
  connection: local

  tasks:
  - name: Print debug message
    debug:
      msg: Hello, world!

######################################
[ccie32305@ccie32305 dev]$ cat ansible.cfg
[defaults]
gathering = explicit
inventory = inv.yml
[ccie32305@ccie32305 dev]$ cat group_vars/routers.yml
---
ansible_network_os: "ios"
ansible_user: "tacacs-admin"
ansible_password: "password"
[ccie32305@ccie32305 dev]$ cat inv.yml
---
all:
   children:
      routers:
        hosts:
          R991:
          R001:
          R101:
          R001:
[ccie32305@ccie32305 dev]$ cat test.yml
---
- hosts: routers
  gather_facts: no
  connection: local

  vars_prompt:
  - name: "mgmt_username"
    prompt: "Username"
    private: no
  - name: "mgmt_password"
    prompt: "Password"

  tasks:

  - name: SYS | Define provider
    set_fact:
      provider:
        host: "{{ inventory_hostname }}"
        username: "{{ mgmt_username }}"
        password: "{{ mgmt_password }}"

  - name: IOS | Show clock
    ios_command:
      provider: "{{ provider }}"
      commands:
        - show clock
    register: clock

  - debug: msg="{{ clock.stdout }}"
[ccie32305@ccie32305 dev]$ ansible-playbook test.yml
Username: ccie32305
Password:

PLAY [routers] ******************************************************************************************************************************************************************************************************************************

TASK [SYS | Define provider] ****************************************************************************************************************************************************************************************************************
ok: [R991]
ok: [R001]
ok: [R101]
ok: [R001]

TASK [IOS | Show clock] *********************************************************************************************************************************************************************************************************************
ok: [R001]
ok: [R991]
ok: [R001]
ok: [R101]

TASK [debug] ********************************************************************************************************************************************************************************************************************************
ok: [R991] => {
    "msg": [
        "16:23:02.481 MESZ Mon Jun 29 2020"
    ]
}
ok: [R001] => {
    "msg": [
        "16:23:02.723 MESZ Mon Jun 29 2020"
    ]
}
ok: [R001] => {
    "msg": [
        "16:23:02.320 MESZ Mon Jun 29 2020"
    ]
}
ok: [R101] => {
    "msg": [
        "16:48:27.033 MESZ Mon Jun 29 2020"
    ]
}

PLAY RECAP **********************************************************************************************************************************************************************************************************************************
R001                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
R001             : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
R991                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
R101             : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

[ccie32305@ccie32305 dev]$
```
#### 5.3.b Puppet manifest
```
root@ccie32305:~# cat helloworld.pp
file { '/tmp/hello.txt':
  ensure  => file,
  content => "hello, world\n",
}
root@ccie32305:~# puppet apply helloworld.pp
Notice: Compiled catalog for ccie32305.lab in environment production in 0.10 seconds
Notice: Finished catalog run in 0.02 seconds
root@ccie32305:~# cat /tmp/hello.txt
hello, world
root@ccie32305:~#
########################################################
The Puppet topic seems to be a mysteria to me. Did not get it working nor find any "simple" tutorial . Also out of the Pluralsight course wasn't able to make an easy example
root@vm49:~# cat /etc/puppet/manifests/node.pp
node 'nxossandbox' {
   include ciscopuppet::proxy
   include device_manager::devices

   device_manager {'sbx-nxos-mgmt.cisco.com':
   type         => 'cisco_nexus',
        credentials     => {
          host                  => 'sbx-nxos-mgmt.cisco.com',
          port                  => 443,
          user                  => 'admin',
          password              => 'Admin_1234!',
          transport             => 'https',
        },
        include_module => false,
   }
}
root@vm49:~# cat cisco.pp
node 'nxossandbox' {
   cisco_vlan { '171':
        ensure  =>      'present',
        shutdown =>     'false',
        state   =>      'active',
        vlan_name       => 'DATA',
        }
}
root@vm49:~# puppet apply cisco.pp
Error: Could not find default node or by name with 'ccie32305.fritz.box, ccie32305.lab, ccie32305' on node ccie32305.lab
Error: Could not find default node or by name with 'ccie32305.fritz.box, ccie32305.lab, ccie32305' on node ccie32305.lab
root@vm49:~# puppet device -v
Info: starting applying configuration to sbx-nxos-mgmt.cisco.com at
Error: Could not run: cannot load such file -- puppet/util/network_device//device
root@vm49:~#


```
### 5.4 Identify a configuration management solution to achieve technical and business requirements

* Configuration management tools help manage infrastructure at scale. Consider the challenges of managing large data centers: 
* Python : Easy repeatable tasks
* Paramiko : SSH connection handler for Python
* Netmiko: network-specific SSH connection handler (uses Paramiko)
* NAPALM: NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.     (uses Netmiko)
* Nornir : Task execution engine supporting well-integrated inventory/variable management, concurrency, and reporting features
* Ansible : YAML based automation frmework (written in python), agentless , leverages SSH
* Puppet : agent-based automation framework, pull, custom language
* Chef : agent-based automation framework, Ruby based, Pull model
* Salt : agent and agentless automation framework, YAML based, pull and push model

### 5.5 Describe how to host an application on a network device (including Catalyst 9000 and Cisco IOx-enabled devices)
```
1) Prepare cat 9k
conf t
iox
cat9k#show app-hosting list
No App found

 

cat9k#
2) Prepare docker container on linux box
docker pull mlabbe/iperf3
docker save mlabbe/iperf3:latest -o iperf3.tar
3) Upload container to cat9k
cat9k(config)#ip scp server enable
[root@devbox developer]# scp iperf3.tar developer@10.10.20.100:iperf3.tar
4) Run container
cat9k#        copy flash:/iperf3.tar usbflash1:
cat9k#app-hosting install appid iperf package usbflash1:iperf3.tar
Installing package 'usbflash1:iperf3.tar' for 'iperf'. Use 'show app-hosting list' for progress.

 

cat9k#show
*Jun 27 11:43:02.035: %IM-6-INSTALL_MSG: Switch 1 R0/0: ioxman: app-hosting: Install succeeded: iperf installed successfully Current state is DEPLOYEDap
cat9k#
cat9k(config)#app-hosting appid iperf
cat9k(config-app-hosting)#app
cat9k(config-app-hosting)#app-vn
cat9k(config-app-hosting)#app-vnic App
cat9k(config-app-hosting)#app-vnic AppGigEthernet vl
cat9k(config-app-hosting)#app-vnic AppGigEthernet vlan-access
cat9k(config-config-app-hosting-vlan-access)#vlan 4000 gu
cat9k(config-config-app-hosting-vlan-access)#vlan 4000 guest-interface 0
cat9k(config-config-app-hosting-vlan-access-ip)#guest-ipaddress 10.10.20.101 netmask 255.255.255.0
cat9k(config-config-app-hosting-vlan-access-ip)#end
cat9k#app-hosting activate appid iperf
iperf activated successfully
Current state is: ACTIVATED

 

cat9k#
cat9k#app-hosting start appid iperf
iperf started successfully
Current state is: RUNNING
cat9k#
cat9k#app-hosting connect appid iperf session
/ $ echo "CCIE32305 rocks"
CCIE32305 rocks
/ $
 ```
 
## Additional resources
- [1.9 Explain architectural patterns (monolithic, services oriented, microservices, and event driven)](https://rubygarage.org/blog/monolith-soa-microservices-serverless)
- [1.10 Utilize advanced version control operations with Git](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line)
- [2.5 Describe the steps in the OAuth2 three-legged authorization code grant flow](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow)
- [3.8 Describe steps to build a custom dashboard to present data collected from Cisco APIs](https://developer.cisco.com/meraki/build/dashboard-admin-app-demo/)
- [3.8 Describe steps to build a custom dashboard to present data collected from Cisco APIs](https://blogs.cisco.com/developer/dna-center-noc-dashboard)
- [4.4 Utilize Docker to containerize an application](https://nickjanetakis.com/blog/docker-tip-7-the-difference-between-run-and-cmd)
- [4.11 Describe how end-to-end encryption principles apply to API](https://medium.com/apis-and-digital-transformation/best-practices-for-building-secure-apis-2b4eb8071d41)
- [5.3.a Ansible playbook](https://codingbee.net/ansible/ansible-a-hello-world-playbook)
- [5.3.b Puppet manifest](https://forge.puppet.com/puppetlabs/ciscopuppet)


- [Leaving the CLI Stone Age: Automating with APIs](https://app.pluralsight.com/course-player?clipId=c621d8fd-4249-4143-ad4b-835b6091a55e)
- [Utilizing RESTCONF to Manage Device Configuration](https://app.pluralsight.com/course-player?clipId=11602f35-360e-4dfe-a6b3-7d6235118790)
- [Working with Cisco UCS Manager and Intersight APIs](https://app.pluralsight.com/course-player?clipId=879b0dc1-15fd-4b21-8a31-74e60da96c95)
- [Constructing Really Good Infrastructure as Code](https://app.pluralsight.com/course-player?clipId=9da1ac26-6553-42be-816d-f450c6332000)

## Contribution
Donate via Bitcoin -> 39Cb6RpuAoqWMSMXGT859PtHjDNTJpDKMp
![btc](https://raw.githubusercontent.com/ccie32305/devnet/master/img/btc.png "BTC")

 or 

[Twitter](https://twitter.com/ccie32305/)

## License
[MIT](https://choosealicense.com/licenses/mit/)














