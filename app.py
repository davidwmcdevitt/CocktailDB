import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL
from cocktailDB import cocktailDB


''' 

    To access locally, go to:
    http://127.0.0.1:8050/
    
'''


db = cocktailDB()

# initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# set the layout of the app
app.layout = dbc.Container([
    html.H1("CocktailDB"),
    dbc.Row([
        dbc.Col([
            dcc.Input(id="pantry-input", type="text"),
            html.Button(id="pantry-submit", children="Add Item"),
            html.Button(id="pantry-reset", children="Reset"),
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
        ], md=4),
        dbc.Col([
            html.Button(id="ideas-button", children="Get Alcoholic Cocktail Ideas"),
            html.Div(id="ideas-output")
        ], md=4),
        dbc.Col([
            html.Div(id="recipe-output")
        ], md=4)
    ], style={"margin-top": "50px"})
], fluid=True)


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
        ideas_list = []
        for key, value in ideas.items():
            recipe_button = html.Button("Get recipe", id={"type": "recipe-button", "index": value}, style={"margin-left": "10px"})
            idea_item = html.Div([value, recipe_button])
            ideas_list.append(idea_item)
        return html.Div([
            html.H3("Cocktail Options"),
            html.Div(ideas_list, style={"whiteSpace": "pre-line"})
        ])
    

@app.callback(Output("recipe-output", "children"),
              [Input({"type": "recipe-button", "index": ALL}, "n_clicks")],
              [State({"type": "recipe-button", "index": ALL}, "id")])
def get_recipe(n_clicks_list, button_ids):
    if not any(n_clicks_list):
        # no buttons have been clicked yet
        return None
    else:
        # find the index of the button that was clicked
        non_empty_clicks = [x for x in n_clicks_list if x is not None]
        if not non_empty_clicks:
            return None
        button_index = n_clicks_list.index(max(non_empty_clicks))
        button_id = button_ids[button_index]
        key = button_id["index"]
        ingredients_dict = db.getIngredients(key)
        ingredients_list = list(ingredients_dict.values())
        ingredients_str = ", ".join(ingredients_list)
        return ingredients_str



                    
# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
