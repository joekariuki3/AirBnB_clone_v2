# AirBnB clone — Web framework (Flask)

Small Flask app rendering simple pages and HBNB listings using Jinja templates and the shared models/storage layer.

## Run locally

```bash
export HBNB_TYPE_STORAGE=file   # or db with proper env vars
python3 100-hbnb.py
# visit http://127.0.0.1:5000/hbnb
```

Key routes for learning:

- `/` — Hello HBNB!
- `/c/<text>` and `/python/<text>` — dynamic text
- `/number/<n>` — int validation
- `/states`, `/cities_by_states` — list states/cities
- `/hbnb_filters`, `/hbnb` — render data-driven pages

Templates are in `templates/`, CSS in `static/styles/`.

See `../docs/STORAGE.md` for storage engine configuration.
AirBnB clone - Web framework
