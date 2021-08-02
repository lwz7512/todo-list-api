# Creating a basic REST api with Tornado

in-memory version and mysql version service implementation. switch through `__use_db` flag in `app.py`

## Install

```
pip3 install -r requirements.txt
```

## Execute sql

log in mysql through client, then:

```
mysql> CREATE DATABASE todos;
mysql> USE todos;
mysql> CREATE TABLE todolist (id INT NOT NULL, name VARCHAR(100) NOT NULL, status INT NOT NULL DEFAULT 0, PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## Start server

```
python3 app.py
```

### List comprehension

```py
# result = list(filter(lambda item: item['id'] == int(id), items))
result = [item for item in items if item['id'] == int(id)]
```

## SQL Queries
