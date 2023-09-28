from datetime import datetime
from pathlib import Path
import pickle
from typing import Optional

# from pandas import DataFrame
from pprint import pprint
import pystow
import typer

app = typer.Typer()
stow = pystow.module("data_collection")
data_url = "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json"


@app.callback(invoke_without_command=True)
def callback(version: Optional[bool] = typer.Option(None, "--version", is_eager=True)):
    if version:
        from data_collection import __version__

        typer.echo(f"data_collection version: {__version__}")
        raise typer.Exit()


@app.command(name="download", help="Download data from the NOAA SWPC API")
def download_data():
    Path("data").mkdir(exist_ok=True)
    dt = datetime.utcnow()
    timestamp = dt.strftime("%Y%m%d_%H%M")
    data = stow.ensure_json(url=data_url, force=True)
    pickle.dump(data, open(f"data/noaa_swpc_data_{timestamp}.pkl", "wb"))
    pickle.dump(data, open(f"data/noaa_swpc_data_latest.pkl", "wb"))
    typer.echo("Data downloaded successfully")


@app.command(name="load", help="Load data from the NOAA SWPC API")
def load_data():
    data = pickle.load(open("data/noaa_swpc_data.pkl", "rb"))
    typer.echo("Data loaded successfully")
    pprint(data)


@app.command(name="run", help="Download and load data from the NOAA SWPC API")
def run():
    download_data()
    load_data()
