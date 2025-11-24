<p align="center">
    <img src="web_static/images/logo.png" alt="HBNB Logo" width="140" />
</p>

# AirBnB clone v2

A minimal, clone of AirBnB built in Python. This version adds a pluggable storage layer (file or MySQL via SQLAlchemy), a command-line console to manage data, a small Flask web front-end, and Fabric scripts to package and deploy static content.

## Features

- Python models for core entities: `User`, `State`, `City`, `Place`, `Amenity`, `Review`
- Two storage engines:
  - FileStorage (JSON on disk)
  - DBStorage (MySQL + SQLAlchemy)
- Interactive console for CRUD and introspection
- Flask web UI with simple routes and Jinja templates
- Fabric scripts to package and deploy static web assets
- Unit tests for models and storage

## Repository structure

```
models/                 # Data models and storage engines
web_flask/              # Flask routes, templates, static assets
web_static/             # Pure static pages (HTML/CSS/images)
tests/                  # Unit tests
versions/               # Created by Fabric pack scripts
console.py              # Interactive CLI
setup_mysql_*.sql       # MySQL init scripts (dev/test)
2-do_deploy_web_static.py, 3-deploy_web_static.py, 100-clean_web_static.py
                                                # Packaging & deploy helpers (Fabric)
```

## Prerequisites

- Python 3.8+
- pip and virtualenv
- MySQL server (for DB storage)
- SQLAlchemy
- Fabric 1.x API for Python 3: install the `fabric3` package

> [!TIP]
> The Fabric scripts use the Fabric 1 API. On Python 3, prefer `fabric3` (not `fabric>=2`) for compatibility.

## Quick start

Clone and enter the project:

```bash
git clone https://github.com/joekariuki3/AirBnB_clone_v2.git
cd AirBnB_clone_v2
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt || pip install sqlalchemy mysqlclient fabric3
```

> [!IMPORTANT]
> If `mysqlclient` fails to install, ensure you have MySQL dev headers installed on your system (e.g., `libmysqlclient-dev` on Debian/Ubuntu).

## Configure storage

This project supports two storage backends, selected via environment variable:

- File storage (default)
- MySQL storage (DBStorage)

Make a copy of .env.example to .env

```bash
cp .env.example .env
```

Set variables in .env file before running anything:

```bash
# File storage (default)
HBNB_TYPE_STORAGE

# OR database storage
HBNB_TYPE_STORAGE
HBNB_MYSQL_USER
HBNB_MYSQL_PWD
HBNB_MYSQL_HOST
HBNB_MYSQL_DB
# Optional: mark test context to auto-drop tables on engine init
HBNB_ENV
```

See `docs/STORAGE.md` for more details.

## Set up MySQL (for DB storage)

Use the provided scripts to create users and databases:

```bash
# Development DB
mysql -u root -p < setup_mysql_dev.sql

# Test DB
mysql -u root -p < setup_mysql_test.sql
```

> [!NOTE]
> The scripts create users `hbnb_dev` and `hbnb_test` with limited privileges and matching databases.

## Use the console (CLI)

Start the interactive console:

```bash
./console.py
# or
python3 console.py
```

Common commands:

- `create <Class> [key=value ...]` — create an instance (supports typed parameters)
- `show <Class> <id>` — display an instance
- `destroy <Class> <id>` — delete an instance
- `all [Class]` — list instances
- `update <Class> <id> <attr> <value>` — update attribute

Advanced dot notation is also available, e.g. `User.all()`, `City.show("<id>")`, `State.update("<id>", {"name": "New Name"})`.

See `docs/CONSOLE.md` for complete command reference and examples.

## Run the web app (Flask)

The Flask app renders basic pages using data from the selected storage engine.

```bash
# Example: full HBNB page with filters
python3 -m web_flask.100-hbnb
# Visit http://127.0.0.1:5000/hbnb
```

Other routes included for learning purposes: `/`, `/c/<text>`, `/python/<text>`, `/number/<n>`, `/states`, `/cities_by_states`, `/hbnb_filters`.

> [!TIP]
> When using DB storage, the `/hbnb` and filter routes display live data from MySQL via SQLAlchemy models.

## Package and deploy static content (Fabric)

There are three helper scripts:

- `2-do_deploy_web_static.py` — package and deploy in two steps
- `3-deploy_web_static.py` — single `deploy()` that calls pack+deploy
- `100-clean_web_static.py` — add `do_clean(number)` to keep last N archives

Before running, edit the `env.hosts` list in the scripts to match your servers (user@host). Then:

```bash
# Create an archive of web_static/
fab -f 3-deploy_web_static.py do_pack

# Deploy a specific archive
fab -f 2-do_deploy_web_static.py do_deploy:/absolute/path/to/archive.tgz

# One-shot pack+deploy
fab -f 3-deploy_web_static.py deploy

# Keep only the latest archive locally and remotely
fab -f 100-clean_web_static.py do_clean:1
```

> [!WARNING]
> The host IPs in the repository are placeholders. Replace them with your own SSH targets and ensure key-based auth is configured.

## Testing

Run unit tests:

```bash
python3 -m unittest discover tests
```

## Troubleshooting

- Fabric errors on import: ensure you installed `fabric3` and not `fabric>=2`.
- MySQL connection errors: verify `HBNB_MYSQL_*` environment variables and that the target database exists.
- `mysqlclient` install issues: install system dependencies (e.g., `sudo apt-get install libmysqlclient-dev`).
- Console shows empty data with DB storage: did you set `HBNB_TYPE_STORAGE=db` and call `storage.reload()` (happens automatically on import)?

## Additional docs

- `docs/CONSOLE.md` — CLI command reference and examples
- `docs/STORAGE.md` — storage engines and environment configuration
- `docs/DEPLOY.md` — packaging and deployment with Fabric
