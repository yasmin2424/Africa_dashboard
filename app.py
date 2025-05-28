import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from youth_chart import get_youth_population_chart
from unemployment_chart import get_unemployment_chart
from literacy import get_literacy_chart

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# -------------------------
# Tab 1: Video Reflections
# -------------------------
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

# -------------------------
# Layout
# -------------------------
app.layout = dbc.Container([
    html.H1("Africa Day Dashboard – What Africa Means to Us", className="my-4 text-center"),

    dcc.Tabs([
        # Tab 1: Reflections
        dcc.Tab(label='1. Our Reflections (Videos)', children=[
            html.Br(),
            html.P("Each team member shares what Africa means to them.", className="lead"),
            video_grid
        ]),

        # Tab 2: Cultural + Economic Strengths
        dcc.Tab(label='2. Cultural + Economic Strengths', children=[
            html.Br(),
            html.P("Africa’s greatest asset is its people, especially its youth. A young, dynamic population drives both cultural creativity and future economic power.", className="lead"),
            dcc.Graph(figure=get_youth_population_chart())
        ]),

        # Tab 3: Shared Challenges
        dcc.Tab(label='3. Shared Challenges', children=[
            html.Br(),
            dcc.Graph(figure=get_literacy_chart()),
            dcc.Graph(figure=get_unemployment_chart())
        ]),

        # Tab 4: AfriPulse Vision
        dcc.Tab(label='4. Our Vision: AfriPulse – The African Data Observatory', children=[
            html.Br(),
            html.H4("📡 AfriPulse: The African Data Observatory", className="text-primary"),

            html.P("AfriPulse is a real-time, open dashboard platform that tracks Africa’s progress in education, health, climate, and innovation — powered by data from students, communities, and local governments."),

           html.Div("🛠️ AfriPulse Mockup Coming Soon", style={
                "width": "80%",
                "margin": "20px auto",
                "padding": "60px",
                "textAlign": "center",
                "fontSize": "20px",
                "color": "#888",
                "border": "2px dashed #ccc",
                "borderRadius": "10px",
                "backgroundColor": "#f9f9f9"
            }),

            html.H5("✨ Why AfriPulse?", className="mt-4"),
            html.Ul([
                html.Li("Crowdsources real-time data from students and communities."),
                html.Li("Dashboards built by African MDS students using open-source tools."),
                html.Li("Used by policymakers to make informed, community-centered decisions."),
            ]),

            dbc.Row([
                dbc.Col([
                    html.H6("📈 5,000+ Youth Contributors", className="text-success"),
                    html.P("Local data from schools, farms, clinics, and homes.")
                ], width=4),
                dbc.Col([
                    html.H6("🌍 12 Countries Active", className="text-success"),
                    html.P("Built by MDS students, powered by local voices.")
                ], width=4),
                dbc.Col([
                    html.H6("📊 30 Dashboards Deployed", className="text-success"),
                    html.P("From school attendance to rainfall tracking.")
                ], width=4),
            ], className="mt-4"),

            html.Blockquote("“Data used to be foreign. Now, it’s ours. We’re building the dashboards for Africa’s future.”", style={
                "font-style": "italic",
                "margin": "30px auto",
                "width": "80%",
                "color": "#444"
            })
        ]),

        # Tab 5: Dream 2035
        dcc.Tab(label='5. Dream 2035', children=[
            html.Br(),
            html.H4("🌟 Our Dream for Africa by 2035"),
            html.P("We imagine an Africa where every decision — from classrooms to capitals — is powered by data and the dreams of its youth."),

            html.Ul([
                html.Li("📚 All students equipped with digital and data tools."),
                html.Li("🗺️ Youth from all 54 countries connected through data exchanges."),
                html.Li("📈 Dashboards used by village leaders and presidents alike."),
            ]),

            html.Blockquote("“I dream of an Africa where data is not extracted — it's created, owned, and shared by Africans.” – Team MDS", style={
                "font-style": "italic",
                "color": "#555",
                "margin": "30px auto",
                "width": "80%"
            }),

            html.Img(src="/assets/dream2035_wordcloud.png", style={
                "width": "70%",
                "margin": "20px auto",
                "display": "block",
                "border": "1px solid #ccc"
            })
        ])
    ])
], fluid=True)

# -------------------------
# Run Server
# -------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8000)
