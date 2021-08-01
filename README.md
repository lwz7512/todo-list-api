# Creating a basic REST api with Tornado

in-memory version and mysql version service implementation. switch through `__use_db` flag in `app.py`

## Install

```
pip3 install -r requirements.txt
python3 app.py
```

### List comprehension

```py
# result = list(filter(lambda item: item['id'] == int(id), items))
result = [item for item in items if item['id'] == int(id)]
```

## SQL Queries
