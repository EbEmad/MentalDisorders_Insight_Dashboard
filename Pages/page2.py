import dash
from dash import html, dcc, Dash, Input, Output, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import pathlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import plotly.graph_objects as go

# construct a path that points to the data
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df1 = pd.read_csv(DATA_PATH.joinpath("mental disorders.csv"))
anxiety_age = pd.read_csv(DATA_PATH.joinpath("anxiety-disorders-prevalence-by-age.csv"))
anxiety_sex = pd.read_csv(DATA_PATH.joinpath("anxiety-disorders-prevalence-gender.csv"))
bipolar_age = pd.read_csv(DATA_PATH.joinpath("bipolar-disorders-prevalence-by-age.csv"))
bipolar_sex = pd.read_csv(DATA_PATH.joinpath("bipolar-disorders-prevalence-gender.csv"))
depressive_age = pd.read_csv(DATA_PATH.joinpath("depressive-disorders-prevalence-by-age.csv"))
depressive_sex = pd.read_csv(DATA_PATH.joinpath("depressive-disorders-prevalence-gender.csv"))
schizo_age = pd.read_csv(DATA_PATH.joinpath("schizophrenia-prevalence-by-age.csv"))
schizo_sex = pd.read_csv(DATA_PATH.joinpath("schizophrenia-prevalence-gender.csv"))

years=df1['year']