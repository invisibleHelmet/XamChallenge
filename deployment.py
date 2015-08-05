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

#print "Changing directory......."
#if not osCall("cd /var/www/html"): print("Changed directory.")

print "Cloning git repository......."
if not osCall("sudo git clone https://github.com/paypal/rest-api-sample-app-php.git /var/www/html"): print("Clone successful.")

print "Changing application root directory permissions......."
if not osCall("sudo chmod 777 /var/www/html"): print("permission change successful.")

#print "Switching directory......."
#if not osCall("cd rest-api-sample-app-php"): print("Switched directory.")

print "Installing Composer......."
if not osCall("cd /var/www/html && sudo curl -sS https://getcomposer.org/installer | php"): print("Installed Composer.")

print "Updating Packages......."
if not osCall("sudo apt-get -y update"): print("Packages updated.")

print "Reinstalling curl......."
if not osCall("sudo apt-get -y install php5-curl"): print("Installation successful.")

print "Calling Composer update......."
if not osCall("sudo php /var/www/html/composer.phar update"): print("Update successful.")

print "Logging into mysql......."
if not osCall("mysql --host=localhost --user=root --password=root"): print("Logged in.")

print "Creating database for application......."
if not osCall("CREATE DATABASE paypal_pizza_app;"): print("Database created.")

print "Exit mysql......."
if not osCall("CREATE DATABASE paypal_pizza_app;"): print("Exited.")

print "Generating Tables in database......."
if not osCall("php /var/www/html/install/create_tables.php"): print("Tables created.")

