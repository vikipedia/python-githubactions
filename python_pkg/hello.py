import typer

app = typer.Typer()


@app.command()
def hello(name):
    print("Hello", name, "!")


if __name__ == '__main__':
    app()
