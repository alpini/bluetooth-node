//Node.js version
var rethinkdb = require('rethinkdb');

//open connection to database
//callback pulls a list of devices
var databaseConnection = null;
rethinkdb.connect({host: '127.0.0.2', port: 28015}, function(err, conn) {
    if (err) throw err;
    databaseConnection = conn;
    rethinkdb.db('bluetooth_node').table('bluetooth_devices').run(databaseConnection, function(err, cursor) {
        if (err) throw err;
        cursor.toArray(function(err, result) {
            if(err) throw err;
            var devices = result;
            //run indefinitely
            while (true) {
                //check changefeed
                rethinkdb.db('bluetooth_node').table('bluetooth_devices').changes().run(databaseConnection, function(err, cursor) {
                    console.log('here');
                    changeFeed = cursor;
                    changesFound = false;
                    for (var change in changeFeed) {
                        changesFound = true;
                    }
                    if (changesFound) {
                        rethinkdb.db('bluetooth_node').table('bluetooth_devices').run(databaseConnection, function(err, cursor) {
                            if (err) throw err;
                            cursor.toArray(function(err, result) {
                                if(err) throw err;
                                var devices = result;
                            });
                        });
                    }
                    for (var device in devices) {

                    }
                });
            }
        });
    });
});