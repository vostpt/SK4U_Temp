# -*- coding: utf-8 -*-
# Original Code by Jorge Gomes for VOST Portugal

# -----------------------------------------------
#                  LIBRARIES
# -----------------------------------------------

# Import Dash and Dash Bootstrap Components
import dash
import dash_daq as daq
from dash import Input, Output, dcc, html, dash_table
import dash_bootstrap_components as dbc

# -----------------------------------------------
#                  TOP ROW
# -----------------------------------------------

header_row = dbc.Row(
        		[
	        	dbc.Col(

	        		html.Hr(
	        			style={
	        			"borderWidth": "2vh",
	        			"width": "100%",
	        			"borderColor": "#0B4EA2",
	        			"opacity": "unset",
	        			}
	        			),
	        		width={"size": 3},
	        		),
	        	dbc.Col(
	        		html.Hr(
	        			style={
	        			"borderWidth": "2vh",
	        			"width": "100%",
	        			"borderColor": "#EE1C24",
	        			"opacity": "unset",
	        			}
	        			),
	        		width={"size": 3},
	        		),
	        	dbc.Col(
	        		html.Hr(
	        			style={
	        			"borderWidth": "2vh",
	        			"width": "100%",
	        			"borderColor": "#005BBB",
	        			"opacity": "unset",
	        			}
	        			),
	        		width={"size": 3},
	        		),
	        	dbc.Col(
	        		html.Hr(
	        			style={
	        			"borderWidth": "2vh",
	        			"width": "100%",
	        			"borderColor": "#FFD400",
	        			"opacity": "unset",
	        			}
	        			),
	        		width={"size": 3},
	        		),
	        	],
        	className="g-0",
    	),  # END OF FIRST ROW 