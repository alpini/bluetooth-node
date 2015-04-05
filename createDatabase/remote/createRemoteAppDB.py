import rethinkdb as rethinkdb

#establish connection to remote server
#for Compose, ensure that startRemote.sh has already been executed
connection = rethinkdb.connect("127.0.0.2", 28015).repl()
#create database
rethinkdb.db_create("bluetooth_node").run()
#create tables
rethinkdb.db("bluetooth_node").table_create("bluetooth_devices").run(connection)
rethinkdb.db("bluetooth_node").table_create("bluetooth_connections").run(connection)