# -*- coding: utf-8 -*-
# Original Code by Jorge Gomes for VOST Portugal

# -----------------------------------------------
#                  LIBRARIES
# -----------------------------------------------


# Import Core Libraries 
import pandas as pd
import numpy as np
import plotly.express as px

# Import Dash and Dash Bootstrap Components
import dash
import dash_daq as daq
from dash import Input, Output, dcc, html, dash_table
import dash_bootstrap_components as dbc

# Import Layout Python Scripts
import layout
import brand




# -----------------------------------------------
#              APP STARTS HERE
# -----------------------------------------------


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title='CONFIRM - SK4U',update_title=None,
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
	)

server = app.server

# -----------------------------------------------
#              APP LAYOUT DESIGN
# -----------------------------------------------

app.layout = dbc.Container(
	
		layout.header_row,
		brand.logos,
	 
	
    fluid=True,
) # END CONTAINER AND LAYOUT 


# -------------------------------------------------------------------------------------
# --------------------------------  START THE APP -------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == "__main__":
	app.run_server(host='0.0.0.0', debug=True)