# Packaging and deployment (Fabric)

These scripts help package the `web_static/` directory and deploy it to remote servers.

> The scripts use Fabric 1 API. On Python 3, install `fabric3`.

## Files

- `2-do_deploy_web_static.py` — two functions: `do_pack()` and `do_deploy(path)`
- `3-deploy_web_static.py` — adds `deploy()` that calls both
- `100-clean_web_static.py` — adds `do_clean(number)` to keep last N archives locally and remotely

Each script defines `env.hosts = ["user@host", ...]`. Update these to your servers.

## Setup

```bash
pip install fabric3
# ensure passwordless SSH to your hosts
ssh-copy-id user@your-host
```

## Usage

```bash
# Pack current web_static/ into versions/<timestamped>.tgz
fab -f 3-deploy_web_static.py do_pack

# Deploy a specific archive to hosts
fab -f 2-do_deploy_web_static.py do_deploy:/absolute/path/to/archive.tgz

# One-shot pack+deploy
fab -f 3-deploy_web_static.py deploy

# Keep only the most recent archive (1) locally and remotely
fab -f 100-clean_web_static.py do_clean:1
```

## How it works

- Archives are stored under `versions/`
- Deploy extracts to `/data/web_static/releases/<name>/`
- A symlink `/data/web_static/current` is updated to point to the latest release
- Old releases are pruned by `do_clean`

## Troubleshooting

- Permission denied: ensure the remote user has rights to `/data/web_static` and uses `sudo` when needed.
- Missing `fabric` module: install `fabric3` (not `fabric>=2`).
- Wrong hosts: edit `env.hosts` in the scripts.
