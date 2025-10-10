# Storage engines

This project supports two storage backends:

- FileStorage — JSON file persistence (default)
- DBStorage — MySQL database via SQLAlchemy ORM

Selection is controlled by environment variables.

## FileStorage (default)

- Module: `models/engine/file_storage.py`
- File location: `file.json` in project root
- No external services required

Use it by setting:

```bash
export HBNB_TYPE_STORAGE=file
```

## DBStorage (MySQL + SQLAlchemy)

- Module: `models/engine/db_storage.py`
- Requires a running MySQL server and a database/user
- SQLAlchemy manages sessions and model mapping

Environment variables required:

```bash
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
# Optional: set 'test' to drop all tables on engine init
export HBNB_ENV=dev
```

Initialize databases using the provided scripts:

```bash
mysql -u root -p < setup_mysql_dev.sql
mysql -u root -p < setup_mysql_test.sql
```

> Note: The DB engine is configured with `pool_pre_ping=True` for robust connections.

## Switching engines

The storage instance is created on import in `models/__init__.py` and `reload()` is called. To switch engines in an interactive session, restart the interpreter after changing env vars.

## Common pitfalls

- Missing `mysqlclient`: install system headers (Debian/Ubuntu `libmysqlclient-dev`) before `pip install mysqlclient`.
- Using Fabric 2 with Fabric 1-style scripts: install `fabric3` instead.
- Forgetting to export env vars in the same shell before running `console.py` or Flask apps.
