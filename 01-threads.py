#!/usr/bin/python3
'''
Code snippet to speed up parralel requests
'''
import threading
import time

exitFlag = 0
devices = ['Switch001','Switch002','Switch003','Switch004']
class CLI_Command_Thread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      time.sleep(5)
      print ("Execute CLI command on" + self.name)
      print ("Exiting " + self.name)

jobs = list()
# Create new threads
for device in devices:
   jobs.append(CLI_Command_Thread(1, device, 1))

# Start new Threads
for job in jobs:
    job.start()

print ("Exiting Main Thread")


