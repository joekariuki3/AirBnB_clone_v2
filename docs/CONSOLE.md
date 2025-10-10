# Console (hbnb CLI)

The console provides an interactive shell to manage models and data using the selected storage engine.

Start the console:

```bash
./console.py
# or
+python3 console.py
```

Prompt: `(hbnb)`

## Commands

- `help` — list commands or help for a command
- `quit` or `EOF` — exit the console
- `create <Class> [key=value ...]` — create an instance
  - Typed values supported: ints, floats, quoted strings; underscores become spaces
  - Example: `create User email="foo@bar" password="secret" first_name="Ada" last_name="Lovelace"`
- `show <Class> <id>` — show one instance
- `destroy <Class> <id>` — delete one instance
- `all [Class]` — list all instances, optionally filtered by class
- `count <Class>` — count instances for a class
- `update <Class> <id> <attr> <value>` — set an attribute, casts known numeric fields
- `update <Class> <id> <dict>` — bulk update using a JSON-like dict

## Dot notation

You can also use an alternative syntax:

- `<Class>.all()`
- `<Class>.count()`
- `<Class>.show("<id>")`
- `<Class>.destroy("<id>")`
- `<Class>.update("<id>", {"name": "NY"})`

## Supported classes

`BaseModel`, `User`, `State`, `City`, `Place`, `Amenity`, `Review`

## Examples

```text
(hbnb) create State name="California"
22d7e6bb-c2b7-4a9a-a0f0-15b6f59a1f12
(hbnb) show State 22d7e6bb-c2b7-4a9a-a0f0-15b6f59a1f12
[State] (22d7e6bb-c2b7-4a9a-a0f0-15b6f59a1f12) { ... }
(hbnb) State.update("22d7e6bb-c2b7-4a9a-a0f0-15b6f59a1f12", {"name": "CA"})
(hbnb) State.all()
["[State] (22d7e6bb-...) { 'name': 'CA', ... }"]
```
