var noble = require('noble'); 

noble.on('stateChange', function(state) {
  if (state === 'poweredOn') {
    noble.startScanning(['D059E485ED4C'], false);
  } else {
    noble.stopScanning();
  }
});

noble.on('discover', function(peripheral) {
  console.log('peripheral discovered (' + peripheral.uuid+ '):');
});