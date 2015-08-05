import subprocess
import os

f = open('log.txt','w')

def osCall(command):
	retcode = subprocess.call(command, stdout=f, stderr=f, shell=True)
	if retcode == 0:
		return 0
	else:
		print 'Error in system call. Check log file.'
		f.close()
		exit()

print "Installing git......."
if not osCall("sudo apt-get install git"): print("Git installation was successful.")

print "Setting mysql password in debconf-set-selections......."
if not osCall("echo mysql-server mysql-server/root_password password root | sudo debconf-set-selections"): print("Set password.")
if not osCall("echo mysql-server mysql-server/root_password_again password root | sudo debconf-set-selections"): print("Set password again.")

print "Installing LAMP Stack......."
if not osCall("sudo apt-get -y install lamp-server^"): print("LAMP Stack installation was successful.")

print "Cloning git repository......."
if not osCall("sudo git clone https://github.com/paypal/rest-api-sample-app-php.git /var/www/html/rest-api-sample-app-php"): print("Clone successful.")

print "Changing application root directory permissions......."
if not osCall("sudo chmod 777 /var/www/html/rest-api-sample-app-php"): print("permission change successful.")

print "Installing Composer......."
if not osCall("cd /var/www/html/rest-api-sample-app-php && sudo curl -sS https://getcomposer.org/installer | php"): print("Installed Composer.")

print "Updating Packages......."
if not osCall("sudo apt-get -y update"): print("Packages updated.")

print "Reinstalling curl......."
if not osCall("sudo apt-get -y install php5-curl"): print("Installation successful.")

print "Calling Composer update......."
if not osCall("sudo php /var/www/html/rest-api-sample-app-php/composer.phar update"): print("Update successful.")

print "Logging into mysql and creating database......."
if not osCall("mysql --host=localhost --user=root --password=root -e 'CREATE DATABASE paypal_pizza_app;'"): print("Database created.")

print "Exit mysql......."
if not osCall("exit"): print("Exited.")

print "Generating Tables in database......."
if not osCall("php /var/www/html/rest-api-sample-app-php/install/create_tables.php"): print("Tables created.")

