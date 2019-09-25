docker run --rm --name euco2-db -v euco2-dbdata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=supersecret -p 3306:3306 -d mariadb:latest
