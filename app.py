import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import os

# main_path = r'c:\data\A414405\Desktop\my_veren\TMS_badkuip_test'

# def read_tms_files(path):
#     for file in os.listdir(path):
#         csv_path = os.path.join(main_path, file)
#         df_csv = pd.read_csv(csv_path)

#     return df_csv

# read_tms_files(main_path)

# Load data
df = pd.read_csv('c:\data\A414405\Desktop\Python Microsoft Visual Studio\Dash_test\data\stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

#Initialiseer the application
app = dash.Dash(__name__)

#define de app
app.layout=html.Div(
    children=[
        html.Div(className='row',
            children=[
                html.Div(className='four columns div-user-controls'),
                html.Div(className='eight columns div-for-charts bg-grey'),
                html.H2('Dash - STOCK PRICES'),
                html.P('''Visualising time series with Plotly - Dash'''),
                html.P('''Pick one or more stocks from the dropdown below.'''),
                dcc.Graph(id='timeseries',
                    config={'displayModeBar': False},
                    animate=True,
                    figure=px.line(df,
                                    x='Date',
                                    y='value',
                                    color='stock',
                                    template='plotly_dark').update_layout(
                                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )

            ]
        )
    ]
)

#Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# print('check the colors')