from dash import *
from testapp import *
from testapp.github_info_header import github_info_header

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/cute_ferret.jpeg")
])

if __name__ == '__main__':
    app.run_server(debug=True)






