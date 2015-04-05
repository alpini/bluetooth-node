#Python version
import rethinkdb as rethinkdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

#open connection to RethinkDB running on MacBook Pro
connection = rethinkdb.connect(host='localhost', port=28015)
devices = rethinkdb.db('bluetooth_node').table('bluetooth_devices').run(connection)
for device in devices:
    print device