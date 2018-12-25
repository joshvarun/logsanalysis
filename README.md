# Logs Analysis

This is a project for Udacity's Full Stack Web Developer Nanodegree.

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Prerequisites
1. [Vagrant](https://www.vagrantup.com)
2. [Python](https://www.python.org/downloads/)
3. [VirtualBox](https://www.virtualbox.org)

## Installation & Setup

1. Install [Vagrant](https://www.vagrantup.com) and [VirtualBox](https://www.virtualbox.org)
2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download [data file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) - `newsdata.sql`


## Usage

### Launching the Virtual Machine:

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded `fullstack-nanodegree-vm` repository using command:
  ```bash
$ vagrant up
```
Note: This might take some time depending on the speed of your internet connection. It downloads a linux vm from the internet.
2. Then Log into this using command:
```bash  
$ vagrant ssh
```
Change directory `/vagrant` and look around with `ls`.

### Setting up the database
1. Use the following command to load the database into local memory
```bash
psql -d news -f newsdata.sql
```
The newsdata.sql will populate the db as required for this project.

Feel free to use ```\dt``` or ```\d table``` to find more information on the tables.

2. Connect to the database
```bash
psql -d news 
```

#### Creating Views

1. article_view

```bash
CREATE VIEW AS SELECT title, authors.name, count(*) AS views FROM articles, authors, log WHERE
 articles.author = authors.id AND log.path LIKE CONCAT(‘%’,articles.slug) GROUP BY articles.title,authors.name
 ORDER BY views DESC;
```

2. error_view
```bash
CREATE VIEW error_view AS SELECT date(time),round(100.0*sum(case log.status  '200 OK' 
  then 0 else 1 end)/count(log.status),2) AS "Error Rate" FROM log GROUP BY date(time) 
  ORDER BY "Error Rate" DESC;
```

### Running the code
From the `/vagrant` directory run the following command:

```bash
python log_analysis.py
```
