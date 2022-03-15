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
#                    LOGOS
# -----------------------------------------------


brand = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title='CONFIRM - SK4U',update_title=None,
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)


VOSTPT_LOGO =  brand.get_asset_url('VOSTPT_Logotype.png')
CONFIRM_LOGO = brand.get_asset_url('CONFIRM_Logotype.png')
PROJECT_LOGO = brand.get_asset_url('SK4U_Logotype.png')




logos = dbc.Row(
			[
			dbc.Col(html.Img(src=PROJECT_LOGO, height="50px"),width={"size": 1},), 	# PROJECT LOGO
			dbc.Col(html.Img(src=VOSTPT_LOGO, height="50px"),width={"size": 1},),   # VOSTPT LOGO - DO NOT REMOVE
			dbc.Col(                                                                # CREATE INTERMEDIATE WHITE SPACE COLUMN
				html.Hr(
					style={
					"borderWidth": "2vh",
					"width": "100%",
					"borderColor": "#FFFFFF",
					"opacity": "unset",
					}
					),
				width={"size": 9},
				),
			dbc.Col(html.Img(src=CONFIRM_LOGO, height="50px"),width={"size": 1},),  # CONFIRM LOGO - DO NOT REMOVE
			

			], 
			className="g-0",
	),  # END OF SECOND ROW 