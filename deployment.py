import subprocess
import os

#Open log file for writing.
log = open('log.txt','w')

#Function for executing system calls.
#Returns 0 if successful or writes error to log file and exits the script.
def osCall(command):
	retcode = subprocess.call(command, stdout=log, stderr=log, shell=True)
	if retcode == 0:
		return 0
	else:
		print 'Error in system call. Check log file.'
		log.close()
		exit()

#-------------------Application Deployment----------------------

print "------------Application Deploying------------"

#If git is not used to grab this script uncomment section.
#print "Installing git......."
#if not osCall("sudo apt-get install git"): print("Git installation was successful.")

#Updated packages.
print "Updating Packages......."
if not osCall("sudo apt-get -y update"): print("Packages updated.")

#Set mysql passwords in debconf-set-selections to bypass mysql setup screen.
print "Setting mysql password in debconf-set-selections......."
if not osCall("echo mysql-server mysql-server/root_password password root | sudo debconf-set-selections"): print("Set password.")
if not osCall("echo mysql-server mysql-server/root_password_again password root | sudo debconf-set-selections"): print("Set password again.")

#Install Apache, MySQL, and PHP.
print "Installing LAMP Stack......."
if not osCall("sudo apt-get -y install lamp-server^"): print("LAMP Stack installation was successful.")

#Clone the web app repository to the apache server.
print "Cloning git repository......."
if not osCall("sudo git clone https://github.com/paypal/rest-api-sample-app-php.git /var/www/html/rest-api-sample-app-php"): print("Clone successful.")

#Change permissions of the repository to avoid conflicts installing the app.
print "Changing application root directory permissions......."
if not osCall("sudo chmod 777 /var/www/html/rest-api-sample-app-php"): print("Permission change successful.")

#Install composer in the app repository.
print "Installing Composer......."
if not osCall("cd /var/www/html/rest-api-sample-app-php && sudo curl -sS https://getcomposer.org/installer | php"): print("Installed Composer.")

#Reinstall curl so composer runs correctly.
print "Reinstalling curl......."
if not osCall("sudo apt-get -y install php5-curl"): print("Installation successful.")

#Run composer update to install app.
print "Calling Composer update......."
if not osCall("cd /var/www/html/rest-api-sample-app-php/ && sudo php /var/www/html/rest-api-sample-app-php/composer.phar update"): print("Update successful.")

#Create a database for the app in the MySQL server with default username and password.
print "Logging into mysql and creating database......."
if not osCall("mysql --host=localhost --user=root --password=root -e 'CREATE DATABASE paypal_pizza_app;'"): print("Database created.")

#Exit MySQL.
print "Exit mysql......."
if not osCall("exit"): print("Exited.")

#Create the necessary tables for the web app.
print "Generating Tables in database......."
if not osCall("php /var/www/html/rest-api-sample-app-php/install/create_tables.php"): print("Tables created.")

#Reset permissions after web app is installed.
print "Resetting application root directory permissions......."
if not osCall("sudo chmod 755 /var/www/html/rest-api-sample-app-php"): print("Permission change successful.")

#-------------------Firewall Configuration----------------------

print "------------Configuring Firewall Settings------------"

#Open port 80 to all IP addresses.
print "Opening port 80 to all......."
if not osCall("sudo iptables -A INPUT -p tcp --destination-port 80 -j ACCEPT"): print("Port 80 opened to all.")

#Open port 443 to all IP addresses.
print "Opening port 443 to all......."
if not osCall("sudo iptables -A INPUT -p tcp --destination-port 443 -j ACCEPT"): print("Port 443 opened to all.")

#Accept ICMP packets from all.
print "Accept ICMP packets from all......."
if not osCall("sudo iptables -A INPUT -p icmp -j ACCEPT"): print("ICMP traffic allowed.")

#Allow ssh for ip range 10.0.0.0/8.
print "Open ssh for ip range 10.0.0.0/8......."
if not osCall("sudo iptables -A INPUT -p tcp -s 10.0.0.0/8 --destination-port 22 -j ACCEPT"): print("SSH traffic for IP range 10.0.0.0/8 allowed.")

#Allow ssh for ip range 192.168.0.0/16.
print "Open ssh for ip range 192.168.0.0/16......."
if not osCall("sudo iptables -A INPUT -p tcp -s 192.168.0.0/16 --destination-port 22 -j ACCEPT"): print("SSH traffic for IP range 192.168.0.0/16 allowed.")

#Allow ssh for ip range 172.0.0.0/8.
print "Open ssh for ip range 172.0.0.0/8......."
if not osCall("sudo iptables -A INPUT -p tcp -s 172.0.0.0/8 --destination-port 22 -j ACCEPT"): print("SSH traffic for IP range 172.0.0.0/8 allowed.")

#Allow rdp for ip range 10.0.0.0/8.
print "Open rdp for ip range 10.0.0.0/8......."
if not osCall("sudo iptables -A INPUT -p tcp -s 10.0.0.0/8 --destination-port 3389 -j ACCEPT"): print("RDP traffic for IP range 10.0.0.0/8 allowed.")

#Allow rdp for ip range 192.168.0.0/16.
print "Open rdp for ip range 192.168.0.0/16......."
if not osCall("sudo iptables -A INPUT -p tcp -s 192.168.0.0/16 --destination-port 3389 -j ACCEPT"): print("RDP traffic for IP range 192.168.0.0/16 allowed.")

#Allow rdp for ip range 172.0.0.0/8.
print "Open rdp for ip range 172.0.0.0/8......."
if not osCall("sudo iptables -A INPUT -p tcp -s 172.0.0.0/8 --destination-port 3389 -j ACCEPT"): print("RDP traffic for IP range 172.0.0.0/8 allowed.")

#Drop all other packets
print "Closing all other ports......"
if not osCall("sudo iptables -P INPUT DROP"): print("Rest of INPUT chain closed.")
if not osCall("sudo iptables -P FORWARD DROP"): print("Rest of FORWARD chain closed.")
print "All other ports closed."

#Save the firewall configurations so when the server is rebooted they will be reinstated.
print "Saving current firewall rules..........."
if not osCall("iptables-save > /root/dsl.fw"): print("Saved current firewall rules.")
print"Writing /sbin/iptables-restore < /root/dsl.fw to /etc/rc.local"
if not osCall("echo '/sbin/iptables-restore < /root/dsl.fw' | cat - /etc/rc.local > temp && mv temp /etc/rc.local"): print("Saved to /etc/rc.local")
print "Firewall rules saved for next reboot."

print "Web application deployed with firewall rules."

#close log file
log.close()