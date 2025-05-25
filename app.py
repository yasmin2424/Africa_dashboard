import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from youth_chart import get_youth_population_chart
from unemployment_chart import get_unemployment_chart

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sample video paths – update with actual local or hosted file paths
videos = [
    {"name": "Student 1 - Ghana", "src": "/assets/vid1.mp4"},
    {"name": "Student 2 - Kenya", "src": "/assets/video2.mp4"},
    {"name": "Student 3 - Uganda", "src": "/assets/video3.mp4"},
    {"name": "Lukman Lateef - Nigeria", "src": "/assets/lukman_clip.mp4"},
    {"name": "Student 5 - Ethiopia", "src": "/assets/video5.mp4"},
    {"name": "Student 6 - Ghana", "src": "/assets/video6.mp4"},
    {"name": "Student 7 - Kenya", "src": "/assets/video7.mp4"},
    {"name": "Student 8 - Uganda", "src": "/assets/video8.mp4"}
]

video_grid = dbc.Row([
    dbc.Col([
        html.H6(v["name"]),
        html.Video(src=v["src"], controls=True, width="100%", height="120px")
    ], width=3) for v in videos
])

app.layout = dbc.Container([
    html.H1("Africa Day Dashboard – What Africa Means to Us", className="my-4 text-center"),

    dcc.Tabs([
        dcc.Tab(label='1. Our Reflections (Videos)', children=[
            html.Br(),
            html.P("Each team member shares what Africa means to them.", className="lead"),
            video_grid
        ]),
        dcc.Tab(label='2. Cultural + Economic Strengths', children=[
            html.Br(),
            html.P("Africa’s greatest asset is its people, especially its youth. A young, dynamic population drives both cultural creativity and future economic power.", className="lead"),
            dcc.Graph(figure=get_youth_population_chart())
        ]),

        dcc.Tab(label='3. Shared Challenges', children=[
            html.Br(),
            dcc.Graph(figure=get_unemployment_chart())
        ]),
        dcc.Tab(label='4. Our Vision: African Youth Exchange', children=[
            html.Br(),
            html.Div("💡 Introduce AfriConnect idea here with infographics or mockup.")
        ]),
        dcc.Tab(label='5. Dream 2035', children=[
            html.Br(),
            html.Div("Word cloud, timeline, or summary vision from your team.")
        ])
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8080)
