import requests

import pandas as pd

data_url = "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json"
local_data = "data/noaa_rswd.pkl"


def test_noaa_data_is_accessible():
    r = requests.get(data_url)
    assert r.status_code == 200
    assert len(r.json()) > 0

def test_local_data():
    df = pd.read_pickle(local_data)
    assert len(df) > 0