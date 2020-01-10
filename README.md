Wordpress Role
==============

Configures a Wordpress server based on Fedora with CustomOS settings:

- Downloads latest Wordpress version.
- Extracts Wordpress files in /var/www/html/customapp and uses it as Apache HTTPD root path.
- Sets up a mariadb database and a custom user for Wordpress use.

Requirements
------------

A Fedora system.

Role Variables
--------------

mariadb_root_password: "insecure"
mariadb_wordpress_user_password: "insecure"

Static variables like packages list or configuration file settings
can be found in vars/ directory.

Dependencies
------------

This role has iac_ansible-role-server, iac_ansible-role-apache and iac_ansible-role-mariadb as dependencies. All of theabove are configured in ansible-galaxy .requirements file.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: iac_ansible-role-wordpress }
```

License
-------

GPL3

Author Information
--------------

