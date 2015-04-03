Credits
=======
<b>Implemented by</b>: <a href="https://github.com/exoentropy/">@exoentropy</a>, <a href="https://github.com/callentrail/">@callentrail</a>
<b>Inspired by</b>: <a href="">ConocoPhillips Innovation Challenge 2015</a>

Design
======
The purpose of this project is to track Bluetooth devices using <code>n</code> number of Raspberry Pi nodes. Each node will scan for designated Bluetooth addresses and report back to a RethinkDB server and Node.js web server. The AngularJS web application allows users a means of tracking the real-time location information and device management.

Tools Used
==========
<b>Hardware</b>: <a href="http://www.raspberrypi.org/products/raspberry-pi-2-model-b/">Raspberry Pi 2 Model B</a>, USB Wi-Fi adapter, USB Bluetooth adapter, SD card<br>
<b>Software</b>: <a href="http://www.raspberrypi.org/help/noobs-setup/">Raspbian OS (NOOBS)</a>, <a href="https://nodejs.org/">Node.js (0.12.1)</a>, <a href="https://angularjs.org/">AngularJS (1.3.15), <a href="http://rethinkdb.com/">RethinkDB (1.16.3), <a href="http://expressjs.com/">Express (4.12.3)</a>, <a href="http://www.bluez.org/">BlueZ (4.x)</a>

Initial Setup
=============
The Raspberry Pi itself is relatively easy to set up, but installing software on it can be challenge. The Raspberry Pi uses an ARM processor, so any binaries you use must be compiled for the ARM ISA. Relying solely on the Raspbian repository proved to be futile because it generally only contained older versions of key software that led to incompatability issues. Since Intel and AMD chips are much more common, I found myself compiling from source code.

For example, to compile and install Node.js use the following commands:
<code>cd /usr/src</code>
<code>sudo wget http://nodejs.org/dist/v0.12.1/node-v0.12.1.tar.gz</code>
<code>sudo tar xvzf node-v0.12.1.tar.gz</code>
<code>sudo ./configure</code>
<code>sudo make</code>
<code>sudo make install</code>

This is a long process that can take up to several hours depending on version and your hardware specs. Because of this, I opted to delegate as little functionality as possible to the Raspberry Pi nodes, to reduce my dependencies.
