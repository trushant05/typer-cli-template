import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Awesome tcli 
    """

@app.command()
def omni():
    """
    Play with Omniverse 
    """
    typer.echo("Will use for omniverse")

@app.command()
def isaacsim():
    """
    Play with Isaac Sim 
    """
    typer.echo("Will use for isaac sim")