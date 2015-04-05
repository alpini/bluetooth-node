Credits
=======
<b>Implemented by</b>: <a href="https://github.com/exoentropy/">@exoentropy</a>, <a href="https://github.com/callentrail/">@callentrail</a><br>
<b>Inspired by</b>: ConocoPhillips Innovation Challenge 2015

Design
======
The purpose of this project is to track Bluetooth devices using <code>n</code> number of Raspberry Pi nodes. Each node will scan for designated Bluetooth addresses and report back to a RethinkDB server and Node.js web server. The AngularJS web application allows users a means of tracking the real-time location information and device management.

Tools Used
==========
<b>Hardware</b>: <a href="http://www.raspberrypi.org/products/raspberry-pi-2-model-b/">Raspberry Pi 2 Model B</a>, USB Wi-Fi adapter, USB Bluetooth adapter, 8GB SD card<br>
<b>Software</b>: <a href="http://www.raspberrypi.org/help/noobs-setup/">Raspbian OS (NOOBS)</a>, <a href="https://nodejs.org/">Node.js (0.12.1)</a>, <a href="https://angularjs.org/">AngularJS (1.3.15)</a>, <a href="http://rethinkdb.com/">RethinkDB (1.16.3)</a>, <a href="http://expressjs.com/">Express (4.12.3)</a>, <a href="http://www.bluez.org/">BlueZ (4.x)</a><br>
<b>Services</b>: Compose

Dependencies and Installation
=============================
The Raspberry Pi itself is relatively easy to set up, but installing software on it can be challenge. The Raspberry Pi uses an ARM processor, so any binaries you use must be compiled for the ARM ISA. Relying solely on the Raspbian repository proved to be futile because it generally only contained older versions of key software that led to incompatability issues. Since Intel and AMD chips are much more common, I found myself compiling from source code.

To compile and install Node.js use the following commands:<br>
<code>cd /usr/src</code><br>
<code>sudo wget http://nodejs.org/dist/v0.12.1/node-v0.12.1.tar.gz</code><br>
<code>sudo tar xvzf node-v0.12.1.tar.gz</code><br>
<code>sudo ./configure</code><br>
<code>sudo make</code><br>
<code>sudo make install</code><br>

To compile and install RethinkDB use the following commands:<br>
<code>sudo apt-get install g++ protobuf-compiler libprotobuf-dev libboost-dev curl m4 wget</code><br>
<code>cd /usr/src</code><br>
<code>sudo wget http://download.rethinkdb.com/dist/rethinkdb-1.16.3.tgz</code><br>
<code>sudo tar xf rethinkdb-1.16.3.tgz</code><br>
<code>cd rethinkdb-1.16.3</code><br>
<code>./configure --with-system-malloc --allow-fetch</code><br>
<code>sudo make</code><br>
<code>sudo make install</code><br>

<b>Note: if the make command fails, refer to <a href="https://github.com/rethinkdb/rethinkdb/issues/2193">this GitHub issue</a>.<br>

To install the RethinkDB drivers, use the following commands:<br>
<code>sudo npm install -g rethinkdbdash</code> for Node.js<br>
<code>sudo pip install rethinkdb</code> for Python

This is a long process that can take up to several hours depending on versions and your hardware specs. Because of this, I opted to delegate as little functionality as possible to the Raspberry Pi nodes to reduce the number dependencies.

RethinkDB Setup and Creating the Database
=========================================
<b>Local Setup</b>:<br>
On the machine to be used for the database server, start by running the command <code>rethinkdb</code> in the terminal. In a separate tab, navigate to the folder <code>~/bluetooth-node/setup</code>. For Node.js use the command <code>node setupRethink.js</code>, or for Python use the command <code>python setupRethink.py</code>. This creates a new database called <code>bluetooth_node</code> and the necessary tables. You can verify that the database and tables were created properly by navigating to <a href = "http://localhost:8080/#tables">http://localhost:8080/#tables</a> in your web browser while RethinkDB is running.

<b>Remote Setup</b>:<br>
This implementation uses a DaaS called <a href="http://compose.io">Compose</a> for remote RethinkDB hosting.