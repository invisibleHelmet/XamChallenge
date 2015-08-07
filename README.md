Deployment of PayPal Pizza App
==============================

Overview
--------

This is my deployment of the [PayPal Pizza App](https://github.com/paypal/rest-api-sample-app-php/blob/master/README.md) and configuration of the servers firewall. I use python to automate the deployment and iptables to control network traffic. The script is written for deployment on a basic install of the [Ubuntu 14.04 LTS AMD 64 Server Image](http://releases.ubuntu.com/14.04/). The network traffic is controled by setting rules in iptables. 

Pre-requisites
--------------

   *Git

	
Running the app
---------------

   * Copy the XamChallenge folder or clone the repository anywhere on your Ubuntu 14.04 LTS server.
   * Run 'sudo python deployment.py' from the XamChallenge directory.
   * The deployment and firewall configuration will run and create a log file of the installation details.
	
Deployment
----------


Firewall Configuration
----------------------

