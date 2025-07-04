# import dash
# from dash import dcc, html
# import dash_bootstrap_components as dbc
# from youth_chart import get_youth_population_chart
# from unemployment_chart import get_unemployment_chart
# from literacy import get_literacy_chart

# app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server

# # -------------------------
# # Layout
# # -------------------------
# app.layout = dbc.Container([
#     html.H1("Africa Day Dashboard – What Africa Means to Us", className="my-4 text-center"),

#     dcc.Tabs([
#         # Tab 1: Reflections (Videos with flags)
#         dcc.Tab(label='1. Our Reflections (Videos)', children=[
#             html.Br(),
#             html.Div([
#                  html.P( "This video combines reflections from each team member on what 🌟 Africa means to them.",
#             className="lead",
#             style={"textAlign": "center", "color": "white", "marginBottom": "40px"}
#         ),
#                 dbc.Row([
#                     # Left flags
#                     dbc.Col([
#                         html.Div([
#                             html.P("🇬🇭 Ghana", style={"fontSize": "60px"}),
#                             html.P("🇰🇪  Kenya", style={"fontSize": "70px"}),
#                             html.P("🇺🇬 Uganda", style={"fontSize": "80px"}),
#                         ], style={"textAlign": "center"})
#                     ], width=2),

#                     # Video
#                     dbc.Col([
#                         html.Video(
#                             src="/assets/team_reflections.MOV",
#                             controls=True,
#                             autoPlay=True,
#                             style={
#                                 "height": "65vh",
#                                 "margin": "auto",
#                                 "display": "block",
#                                 "borderRadius": "12px",
#                                 "boxShadow": "0 6px 20px rgba(0,0,0,0.25)"
#                             }
#                         ),
                        

#                     # Right flags
#                     dbc.Col([
#                         html.Div([
#                             html.P("🇳🇬 Nigeria", style={"fontSize": "60px"}),
#                             html.P("🇪🇹 Ethiopia", style={"fontSize": "70px"}),
#                             html.P("🇬🇭 Ghana" , style={"fontSize": "80px"}),
#                         ], style={"textAlign": "center"})
#                     ], width=1)
#                 ])
#             ], style={
#                 "backgroundColor": "#111",
#                 "padding": "60px 0",
#                 "textAlign": "center"
#             })
#         ]),

#         # Tab 2: Cultural + Economic Strengths
#         dcc.Tab(label='2. Cultural + Economic Strengths', children=[
#             html.Br(),
#             html.P("Africa’s greatest asset is its people, especially its youth. A young, dynamic population drives both cultural creativity and future economic power.", className="lead"),
#             dcc.Graph(figure=get_youth_population_chart())
#         ]),

#         # Tab 3: Shared Challenges
#         dcc.Tab(label='3. Shared Challenges', children=[
#             html.Br(),
#             dcc.Graph(figure=get_literacy_chart()),
#             dcc.Graph(figure=get_unemployment_chart())
#         ]),

#         # Tab 4: AfriPulse Vision
#         dcc.Tab(label='4. Our Vision: AfriPulse – The African Data Observatory', children=[
#             html.Br(),
#             html.H4("📡 AfriPulse: The African Data Observatory", className="text-primary"),

#             html.P("AfriPulse is a real-time, open dashboard platform that tracks Africa’s progress in education, health, climate, and innovation — powered by data from students, communities, and local governments."),

#             html.Div("🛠️ AfriPulse Mockup Coming Soon", style={
#                 "width": "80%",
#                 "margin": "20px auto",
#                 "padding": "60px",
#                 "textAlign": "center",
#                 "fontSize": "20px",
#                 "color": "#888",
#                 "border": "2px dashed #ccc",
#                 "borderRadius": "10px",
#                 "backgroundColor": "#f9f9f9"
#             }),

#             html.H5("✨ Why AfriPulse?", className="mt-4"),
#             html.Ul([
#                 html.Li("Crowdsources real-time data from students and communities."),
#                 html.Li("Dashboards built by African MDS students using open-source tools."),
#                 html.Li("Used by policymakers to make informed, community-centered decisions."),
#             ]),

#             dbc.Row([
#                 dbc.Col([
#                     html.H6("📈 5,000+ Youth Contributors", className="text-success"),
#                     html.P("Local data from schools, farms, clinics, and homes.")
#                 ], width=4),
#                 dbc.Col([
#                     html.H6("🌍 12 Countries Active", className="text-success"),
#                     html.P("Built by MDS students, powered by local voices.")
#                 ], width=4),
#                 dbc.Col([
#                     html.H6("📊 30 Dashboards Deployed", className="text-success"),
#                     html.P("From school attendance to rainfall tracking.")
#                 ], width=4),
#             ], className="mt-4"),

#             html.Blockquote("“Data used to be foreign. Now, it’s ours. We’re building the dashboards for Africa’s future.”", style={
#                 "font-style": "italic",
#                 "margin": "30px auto",
#                 "width": "80%",
#                 "color": "#444"
#             })
#         ]),

#         # Tab 5: Dream 2035
#         dcc.Tab(label='5. Dream 2035', children=[
#             html.Br(),
#             html.H4("🌟 Our Dream for Africa by 2035"),
#             html.P("We imagine an Africa where every decision — from classrooms to capitals — is powered by data and the dreams of its youth."),

#             html.Ul([
#                 html.Li("📚 All students equipped with digital and data tools."),
#                 html.Li("🗺️ Youth from all 54 countries connected through data exchanges."),
#                 html.Li("📈 Dashboards used by village leaders and presidents alike."),
#             ]),

#             html.Blockquote("“I dream of an Africa where data is not extracted — it's created, owned, and shared by Africans.” – Team MDS", style={
#                 "font-style": "italic",
#                 "color": "#555",
#                 "margin": "30px auto",
#                 "width": "80%"
#             }),

#             html.Img(src="/assets/dream2035_wordcloud.png", style={
#                 "width": "70%",
#                 "margin": "20px auto",
#                 "display": "block",
#                 "border": "1px solid #ccc"
#             })
#         ])
#     ])
# ], fluid=True)

# # -------------------------
# # Run Server
# # -------------------------
# if __name__ == '__main__':
#     app.run_server(debug=True, host='127.0.0.1', port=8000)


import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from youth_chart import get_youth_population_chart
from unemployment_chart import get_unemployment_chart
from literacy import get_literacy_chart

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# -------------------------
# Layout
# -------------------------
app.layout = dbc.Container([
    html.H1("Africa Day Dashboard – What Africa Means to Us", className="my-4 text-center"),

    dcc.Tabs([
        
        
        dcc.Tab(label='Welcome', children=[
    html.Div([
        html.H1(
            "🌍 What Does Africa Mean to You?",
            style={
                "textAlign": "center",
                "fontSize": "80px",
                "fontWeight": "bold",
                "lineHeight": "1.2",
                "color": "darkgreen",
                "textShadow": "2px 2px 6px rgba(0, 0, 0, 0.7)"
            }
        )
    ], style={
        "height": "70vh",
        "backgroundImage": "url('/assets/africa.jpg')",  # Replace with your actual file name
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "backgroundRepeat": "no-repeat",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "40px"
    })
]),

        # Tab 1: Reflections (Video with flags)
        dcc.Tab(label= ' Our Reflections (Videos)', children=[
            html.Br(),
            html.Div([
                html.P(
                    "This video combines reflections from each team member on what 🌟 Africa means to them.",
                    className="lead",
                    style={"textAlign": "center", "color": "white", "marginBottom": "40px"}
                ),
                dbc.Row([
                    # Left flags
                    dbc.Col([
                        html.Div([
                            html.P("🇬🇭", style={"fontSize": "100px"}),
                            html.P("🇰🇪", style={"fontSize": "100px"}),
                            html.P("🇺🇬", style={"fontSize": "100px"}),
                        ], style={"textAlign": "center"})
                    ], width=2),

                    # Video
                    dbc.Col([
                        html.Video(
                            src="/assets/team_reflections.MOV",
                            controls=True,
                            autoPlay=True,
                            style={
                                "height": "65vh",
                                "margin": "auto",
                                "display": "block",
                                "borderRadius": "12px",
                                "boxShadow": "0 6px 20px rgba(0,0,0,0.25)"
                            }
                        )
                    ], width=8),

                    # Right flags
                    dbc.Col([
                        html.Div([
                            html.P("🇳🇬", style={"fontSize": "100px"}),
                            html.P("🇪🇹", style={"fontSize": "100px"}),
                            html.P("🇬🇭", style={"fontSize": "100px"}),
                        ], style={"textAlign": "center"})
                    ], width=2)
                ])
            ], style={
                "backgroundColor": "#111",
                "padding": "60px 0",
                "textAlign": "center"
            })
        ]),

        # Tab 2: Cultural + Economic Strengths
        dcc.Tab(label='Cultural + Economic Strengths', children=[
            html.Br(),
            html.P("Africa’s greatest asset is its people, especially its youth. A young, dynamic population drives both cultural creativity and future economic power.", className="lead"),
            dcc.Graph(figure=get_youth_population_chart())
        ]),

        # Tab 3: Shared Challenges
        dcc.Tab(label='Shared Challenges', children=[
            html.Br(),
            dcc.Graph(figure=get_literacy_chart()),
            dcc.Graph(figure=get_unemployment_chart())
        ]),

        # Tab 4: AfriPulse Vision
        dcc.Tab(label='Our Vision: AfriPulse – The African Data Observatory', children=[
            html.Br(),
            html.H4("📡 AfriPulse: The African Data Observatory", className="text-primary"),
            html.P("AfriPulse is a real-time, open dashboard platform that tracks Africa’s progress in education, health, climate, and innovation — powered by data from students, communities, and local governments."),
             html.Br(),

            html.Img(src="/assets/afripulse_illustration.jpeg",style={
            "width": "30%",
            "margin": "0 auto",
            "display": "block",
            "borderRadius": "10px",
            "boxShadow": "0 4px 10px rgba(0,0,0,0.2)"
        }
    ),
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
        dcc.Tab(label='Dream 2035', children=[
            html.Br(),
            html.Img( src="/assets/future_africa.jpeg",
                     style={"width": "50%", "margin": "0 auto", "display": "block", "borderRadius": "10px"}
        ),
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
