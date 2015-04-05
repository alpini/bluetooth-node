import rethinkdb as rethinkdb

#@to-do: update for dynamic host information
#establish connection
rethinkdb.connect("localhost", 28015).repl()
#create database
rethinkdb.db_create("bluetooth_node").run()
#create tables
rethinkdb.db("bluetooth_node").table_create("bluetooth_devices").run()
rethinkdb.db("bluetooth_node").table_create("bluetooth_connections").run()