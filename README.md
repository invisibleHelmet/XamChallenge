Deployment of PayPal Pizza App
==============================

Overview
--------

This is my deployment of the [PayPal Pizza App](https://github.com/paypal/rest-api-sample-app-php/blob/master/README.md) and configuration of the server's firewall. I used Python to automate the deployment and iptables to control network traffic. The script is written for deployment on a basic install of the [Ubuntu 14.04 LTS AMD 64 Server Image](http://releases.ubuntu.com/14.04/). The network traffic is controlled by setting rules in iptables. 

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

To automate deployment of the application, I first downloaded a .iso of Ubuntu 14.04 LTS Server and installed it in Virtual Box. I chose a bare bones install with no additional features. I went through the process of installing it myself and saved all of the steps I needed to take.  I then made sure my script would bypass any additional user interaction that was required. The MySQL server is configured to have the default username and password for the purpose of this exercise.

Firewall Configuration
----------------------

To configure the firewall I used iptables to set rules for allowed traffic.  I created a rule for each bullet point outlined in the challenge statement.  I then set a rule to block all other traffic to the server. I tested each rule to make sure it was functioning as planned.  Since the server has no extra features installed, services like ssh and rdp are not running.  While port scanning the server it shows that ssh, rdp and https are closed because there is no application bound to their ports. However, TCP traffic in the valid IP ranges to these ports is still excepted.
