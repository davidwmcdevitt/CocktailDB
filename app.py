import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from cocktailDB import cocktailDB


db = cocktailDB()

# initialize the Dash app
app = dash.Dash(__name__)

# set the layout of the app
app.layout = html.Div([
    html.H1("CocktailDB"),
    html.Div([
        dcc.Input(id="pantry-input", type="text"),
        html.Button(id="pantry-submit", children="Add Item"),
        html.Button(id="pantry-reset", children="Reset")
    ]),
    html.H3("Pantry Contents"),
    html.Table([
        html.Thead([
            html.Tr([
                html.Th("Item"),
                html.Th("Quantity")
            ])
        ]),
        html.Tbody(id="pantry-table")
    ]),
    html.Br(),
    html.Button(id="ideas-button", children="Get Cocktail Ideas"),
    html.Div(id="ideas-output")
])

pantry = {}

# define the app callbacks
@app.callback(Output("pantry-table", "children"),
              [Input("pantry-submit", "n_clicks"),
               Input("pantry-reset", "n_clicks")],
              [State("pantry-input", "value")])
def update_pantry_table(submit_clicks, reset_clicks, item):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "pantry-submit" in changed_id:
        if item not in pantry:
            pantry[item] = 1
        else:
            pantry[item] += 1
    elif "pantry-reset" in changed_id:
        # clear the pantry
        pantry.clear()
    # create a list of table rows from the pantry dictionary
    rows = [html.Tr([html.Td(k), html.Td(v)]) for k, v in pantry.items()]
    return rows

@app.callback(Output("ideas-output", "children"),
              [Input("ideas-button", "n_clicks")])
def generate_ideas(n_clicks):
    if n_clicks:
        pantry_list = ", ".join([k for k, v in pantry.items() for i in range(v)])
        ideas = db.getCocktailIngredients(pantry_list)
        ideas_list = "\n".join(ideas.values())
        return html.Div([
            html.H3("Cocktail Options"),
            html.Div(ideas_list, style={"whiteSpace": "pre-line"})
        ])

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
