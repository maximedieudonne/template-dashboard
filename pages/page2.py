from dash import html, dcc

# Layout pour la page 2
layout = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "flex-start",
        "alignItems": "center",
        "height": "100%",
        "backgroundColor": "#ffffff",
        "borderRadius": "8px",
        "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
        "padding": "20px",
    },
    children=[
        html.H2("Page 2: Adjust Sliders", style={"marginBottom": "20px"}),
        html.Div(
            style={
                "width": "100%",
                "maxWidth": "400px",
                "textAlign": "center",
            },
            children=[
                html.Label("Slider 1", style={"fontSize": "16px"}),
                dcc.Slider(id='slider-1', min=0, max=100, step=1, value=50, tooltip={"placement": "bottom"}),
                html.Label("Slider 2", style={"marginTop": "20px", "fontSize": "16px"}),
                dcc.Slider(id='slider-2', min=0, max=200, step=10, value=100, tooltip={"placement": "bottom"}),
                html.Div(
                    id='slider-output',
                    style={
                        "marginTop": "20px",
                        "fontSize": "18px",
                        "fontWeight": "bold",
                    },
                ),
            ],
        ),
    ],
)
