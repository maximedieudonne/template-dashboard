from dash.dependencies import Input, Output

def register_callbacks(app):
    @app.callback(
        Output('slider-output', 'children'),
        [Input('slider-1', 'value'), Input('slider-2', 'value')],
    )
    def update_slider_output(slider1_value, slider2_value):
        return f"Slider 1: {slider1_value}, Slider 2: {slider2_value}"
