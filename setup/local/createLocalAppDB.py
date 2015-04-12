import rethinkdb as rethinkdb

#establish connection to local server
connection = rethinkdb.connect("localhost", 28015).repl()
#create database
rethinkdb.db_create("bluetooth_node").run()
#create tables
rethinkdb.db("bluetooth_node").table_create("bluetooth_devices").run(connection)
rethinkdb.db("bluetooth_node").table_create("bluetooth_connections").run(connection)