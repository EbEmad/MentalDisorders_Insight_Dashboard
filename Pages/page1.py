import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dash import html
from app import app

layout = html.Div([
    html.H1('Video Games Sales', style={"textAlign": "center"})
    ])