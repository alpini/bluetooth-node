#Python version
import os
import subprocess
import time
import datetime
import rethinkdb as rethinkdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

databaseConnection = rethinkdb.connect(host='127.0.0.2', port=28015)
#run indefinitely
while (True):
	#pull fresh list of devices
	devices = rethinkdb.db('bluetooth_node').table('bluetooth_devices').run(databaseConnection)
    for device in devices:
    	#poll for device on node server
        output = subprocess.check_output(['hcitool', 'name', device['device_address']])
        #if present, write timestamp to database
        if (output != ''):
            phoneName = output.split('\n')[0]
            exactTime = time.time()
            timeStamp = datetime.datetime.fromtimestamp(exactTime).strftime('%Y-%m-%d %H:%M:%S')
            rethinkdb.db('bluetooth_node').table('bluetooth_connections').insert({'bluetooth_address' : device['device_address'], 'phone_name' : phoneName, 'time_stamp' : timeStamp}).run(databaseConnection)
    time.sleep(1)