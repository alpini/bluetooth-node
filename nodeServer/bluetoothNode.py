#Python version
import os
import subprocess
import rethinkdb as rethinkdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

databaseConnection = rethinkdb.connect(host='127.0.0.2', port=28015)
devices = rethinkdb.db('bluetooth_node').table('bluetooth_devices').run(databaseConnection)
for device in devices:
    response = subprocess.call(["hcitool", "name", device.device_address])
    print response