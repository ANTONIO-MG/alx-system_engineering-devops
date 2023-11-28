This repo deals with Ngnix Server configurations and explains and executes the following concepts:

What is the main role of a web server
What is a child process
Why web servers usually have a parent process and child processes
What are the main HTTP requests

the files on the directory have the following functions:

0-transfer_file:
Bash script that transfers a file from our client to a server:
Accepts 4 parameters
The path to the file to be transferred
The IP of the server we want to transfer the file to
The username scp connects with
The path to the SSH private key that scp uses
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
scp must transfer the file to the user home directory ~/

1-install_nginx_web_server:
Installs  nginx on  web-01 server
Nginx should be listening on port 80
return a page that contains the string Hello World!
Bash script that configures a new Ubuntu machine to respect above requirements

2-setup_a_domain_name:
register a gomain

3-redirection:
Configure  Nginx server so that /redirect_me is redirecting to another page.
The redirection must be a “301 Moved Permanently”
Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements

4-not_found_page_404:
Configure Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.
