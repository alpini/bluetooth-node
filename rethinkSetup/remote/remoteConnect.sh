sudo ifconfig lo0 alias 127.0.0.2 up
sudo ifconfig lo0 alias 127.0.0.3 up
sudo ifconfig lo0 alias 127.0.0.4 up

echo "Home IP addresses configured..."

ssh -N compose@aws-us-east-1-portal.3.dblayer.com -p 10056 \
-L 127.0.0.2:28015:10.20.128.2:28015 \
-L 127.0.0.3:28015:10.20.128.3:28015 &

echo "Driver SSH tunnel configured..."

ssh -N compose@aws-us-east-1-portal.3.dblayer.com -p 10056 \
-L 127.0.0.2:8080:10.20.128.2:8080 \
-L 127.0.0.3:8080:10.20.128.3:8080 &

echo "Admin UI SSH tunnel configured..."