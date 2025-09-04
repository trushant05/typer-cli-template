# typer-cli-template
Template for simple CLI with typer

## Install UV
Refer [uv official documentation](https://docs.astral.sh/uv/) for more detail:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Create virtual env
Initialize ``.venv`` virtual env:
```
uv venv
```
 
Install dependency in virtual env:
```
uv pip install -r requirements.txt
```

Activate ```.venv``` virtual env:
```
source .venv/bin/activate
```

Deactivate ```.venv``` virtual env:
```
deactivate
```

## Compile (lock) your requirements
Use following command to lock version of dependency:
```
uv pip compile requirements.in -o requirements.txt
```
Note: The above step is to be done outside virtual environment.
