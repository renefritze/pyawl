import pprint
import random
from decimal import Decimal
from datetime import datetime, timedelta

import pandas as pd
from copy import deepcopy

import shutil


def add(items, filename):
    prices = [item.price for item in items]
    cols = [item.id for item in items]
    new = pd.DataFrame([prices], index=[items[0].date], columns=cols)
    try:
        base = pd.read_pickle(filename)
        df = base.append(new)
    except FileNotFoundError:
        df = new
    df.to_pickle(filename)


def plot(filename, ax):
    df = pd.read_pickle(filename)
    pprint.pprint(df)
    df.astype(float).plot(ax=ax)
    # plt.show()


def fake_data(real_items):
    fakes = []
    for date in (datetime.now() - timedelta(days=i*365) for i in range(6)):
        items = [deepcopy(x) for x in real_items]
        for item in items:
            item.price *= Decimal(random.random()+1)
            item.date = date
        fakes.append(items)
    return fakes
