# typer-cli-template
Template for simple CLI with typer

## Install UV
Refer [uv official documentation](https://docs.astral.sh/uv/) for more detail:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Create a UV application
Application are the default target for ```uv init```, but can also be specified with the ```--app``` flag and ```--package``` flag:
```
uv init --app --package --python python3.11 tcli
cd tcli
```

Install typer:
```
uv add typer
```

Install pytest with coverage as development dependency:
```
uv add --dev pytest pytest-cov pyyaml lark
```

Run pytest:
```
uv run pytest
uv run pytest -v 
```

Run pytest with coverage:
```
uv run pytest --cov=tcli
uv run pytest --cov=tcli --cov-report=term-missing
```

Run tcli in uv virtual env:
```
uv run tcli
```

Install tcli systemwide:
```
uv tool install . -e
```

Uninstall tcli:
```
uv tool uninstall . -e
```



BrainStorm

tcli start doc
tcli stop doc

tcli start omniverse --ros2 --name omni
tcli stop omniverse

tcli start isaacsim --ros2 --name isaac_sim
tcli stop isaacsim

tcli start isaaclab --ros2 --cloudxr --name isaac_lab
tcli stop isaaclab