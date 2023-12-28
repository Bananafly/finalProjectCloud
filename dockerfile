# Use an official MySQL runtime as a parent image
FROM mysql:5.7

# Set the working directory in the container
WORKDIR /usr/src/mysql

# Download and add Sakila database scripts
ADD https://downloads.mysql.com/docs/sakila-db.tar.gz /usr/src/mysql
RUN tar -xzf sakila-db.tar.gz
RUN ls
# Copy the current directory contents into the container at /usr/src/mysql
COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 3306

# Import Sakila database on startup
COPY sakila-db/sakila-schema.sql /docker-entrypoint-initdb.d/
COPY sakila-db/sakila-data.sql /docker-entrypoint-initdb.d/

# Run mysql when the container launches
CMD ["mysqld"]