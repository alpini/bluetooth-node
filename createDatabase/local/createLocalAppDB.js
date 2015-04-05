//Node.js version
var rethinkdb = require('rethinkdb');

//establish connection
//callback: create bluetooth_node database
var connection = null;
rethinkdb.connect( {host: 'localhost', port: 28015}, function(err, conn) {
    if (err) throw err;
    connection = conn;
    //create bluetooth_node database
    //calback: create tables
    rethinkdb.dbCreate('bluetooth_node').run(connection, function(err, result) {
        if (err) throw err;
        rethinkdb.db('bluetooth_node').tableCreate('bluetooth_devices').run(connection, function(err, result) {
            if (err) throw err;
            console.log(JSON.stringify(result, null, 2));
        });
        rethinkdb.db('bluetooth_node').tableCreate('bluetooth_connections').run(connection, function(err, result) {
            if (err) throw err;
            console.log(JSON.stringify(result, null, 2));
        });
    });
});