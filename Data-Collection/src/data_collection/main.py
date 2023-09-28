from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd
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


@app.command(name="download", help="Download latest Realtime Solar Wind Data from NOAA SWPC API")
def download_data():
    # Store max 100 files
    data_dir = pystow.utils.get_base("data_collection")
    num_files = len(list(data_dir.glob("*.json")))
    if num_files > 100:
        files = sorted(list(data_dir.glob("*.json")))
        for f in files[:-100]:
            f.unlink()
    Path("data").mkdir(exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M")
    data = stow.ensure_json(url=data_url, force=True, name=f"noaa_rswd_{timestamp}.json")
    new_data = pd.DataFrame(data)
    try:
        curr_data = pd.DataFrame(pd.read_pickle("data/noaa_rswd.pkl"))
    except FileNotFoundError:
        curr_data = pd.DataFrame()
    df = pd.concat([curr_data, new_data]).drop_duplicates()
    df.to_pickle("data/noaa_rswd.pkl")


@app.command(name="load", help="Load aggregated local data")
def load_data():
    df = pd.read_pickle("data/noaa_rswd.pkl")
    df.to_csv("data/noaa_rswd.csv")  # for debug purposes
    return df


@app.command(name="run", help="Download and load data from the NOAA SWPC API")
def run():
    download_data()
    load_data()
