# LazyAdmin
Wordpress Admin User Attack

DISCLAIMER: All the scripts should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.

Usage: python3 lazyadmin.py

Will ask for wordpress site, must input with the http:/https:

Lazy admin checks with if the admin user is listed on the site wordpress api, if the admin user is found will open a chrome browser and will try to login using the "admin" password, if the admin user doesnt exist, will reply on the cli "No admin user found"

Please note if the admin user is found but the login attempt fails, youll have to close the browser.

Requirements: Chromedriver

Enjoy!
