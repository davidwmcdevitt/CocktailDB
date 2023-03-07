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

app.layout = dbc.Container([
    html.H1("CocktailDB"),
    dbc.Row([
        dbc.Col([
            html.H3("Find a Cocktail:"),
            dcc.Dropdown(
                id='cat-dropdown',
                options=[
                    {'label': 'Cocktail', 'value':'Cocktail'},
                    {'label': 'Shot', 'value':'Shot'},
                    {'label': 'Ordinary Drink', 'value':'Ordinary Drink'},
                    {'label': 'Other / Unknown', 'value':'Other / Unknown'},
                    {'label': 'Punch / Party Drink', 'value':'Punch / Party Drink'},
                    {'label': 'Coffee / Tea', 'value':'Coffee / Tea'},
                    {'label': 'Beer', 'value':'Beer'},
                    {'label': 'Shake', 'value':'Shake'},
                    {'label': 'Soft Drink', 'value':'Soft Drink'},
                    {'label': 'Homemade Liqueur', 'value':'Homemade Liqueur'},
                    {'label': 'Cocoa', 'value':'Cocoa'}
                ],
                value='Cocktail'
            ),
            dcc.Dropdown(
                id='type-dropdown',
                options=[
                    {'label': 'Alcoholic', 'value':'Alcoholic'},
                    {'label': 'Non-alcoholic', 'value':'Non-alcoholic'}
                ],
                value='Alcoholic'
            ),
            dcc.Dropdown(
                id='glass-dropdown',
                options=[
                    {'label': 'Cocktail glass', 'value':'Cocktail glass'},
                    {'label': 'Highball glass', 'value':'Highball glass'},
                    {'label': 'Collins Glass', 'value':'Collins Glass'},
                    {'label': 'Old-fashioned glass', 'value':'Old-fashioned glass'},
                    {'label': 'Margarita/Coupette glass', 'value':'Margarita/Coupette glass'},
                    {'label': 'Whiskey sour glass', 'value':'Whiskey sour glass'},
                    {'label': 'Champagne Flute', 'value':'Champagne Flute'},
                    {'label': 'Margarita glass', 'value':'Margarita glass'},
                    {'label': 'Coupe Glass', 'value':'Coupe Glass'},
                    {'label': 'Beer pilsner', 'value':'Beer pilsner'},
                    {'label': 'Punch bowl', 'value':'Punch bowl'},
                    {'label': 'Coffee mug', 'value':'Coffee mug'},
                    {'label': 'Beer mug', 'value':'Beer mug'},
                    {'label': 'Shot Glass', 'value':'Shot Glass'},
                    {'label': 'Pint glass', 'value':'Pint glass'},
                    {'label': 'Hurricane glass', 'value':'Hurricane glass'},
                    {'label': 'Pitcher', 'value':'Pitcher'},
                    {'label': 'Beer Glass', 'value':'Beer Glass'},
                    {'label': 'Irish coffee cup', 'value':'Irish coffee cup'},
                    {'label': 'Mason jar', 'value':'Mason jar'},
                    {'label': 'Balloon Glass', 'value':'Balloon Glass'},
                    {'label': 'Wine Glass', 'value':'Wine Glass'},
                    {'label': 'Cordial glass', 'value':'Cordial glass'},
                    {'label': 'Brandy snifter', 'value':'Brandy snifter'},
                    {'label': 'Copper Mug', 'value':'Copper Mug'},
                    {'label': 'Jar', 'value':'Jar'},
                    {'label': 'Nick and Nora Glass', 'value':'Nick and Nora Glass'},
                    {'label': 'White wine glass', 'value':'White wine glass'},
                    {'label': 'Whiskey Glass', 'value':'Whiskey Glass'},
                    {'label': 'Pousse cafe glass', 'value':'Pousse cafe glass'}
                ],
                value='Cocktail glass'
            ),
            dcc.Dropdown(
                id='ingredients-dropdown',
                options=[
                    {'label': 'light rum', 'value':'light rum'},
                    {'label': 'triple sec', 'value':'triple sec'},
                    {'label': 'lime juice', 'value':'lime juice'},
                    {'label': 'sugar', 'value':'sugar'},
                    {'label': 'mint', 'value':'mint'},
                    {'label': 'scotch', 'value':'scotch'},
                    {'label': 'sweet vermouth', 'value':'sweet vermouth'},
                    {'label': 'dry vermouth', 'value':'dry vermouth'},
                    {'label': 'orange bitters', 'value':'orange bitters'},
                    {'label': 'maraschino liqueur', 'value':'maraschino liqueur'},
                    {'label': 'rum', 'value':'rum'},
                    {'label': 'tequila', 'value':'tequila'},
                    {'label': 'fruit', 'value':'fruit'},
                    {'label': 'ice', 'value':'ice'},
                    {'label': 'salt', 'value':'salt'},
                    {'label': 'fruit juice', 'value':'fruit juice'},
                    {'label': 'soda water', 'value':'soda water'},
                    {'label': 'creme de banane', 'value':'creme de banane'},
                    {'label': 'pineapple juice', 'value':'pineapple juice'},
                    {'label': 'frangelico', 'value':'frangelico'},
                    {'label': 'coffee', 'value':'coffee'},
                    {'label': 'cream', 'value':'cream'},
                    {'label': 'creme de cacao', 'value':'creme de cacao'},
                    {'label': 'light cream', 'value':'light cream'},
                    {'label': 'nutmeg', 'value':'nutmeg'},
                    {'label': 'blended whiskey', 'value':'blended whiskey'},
                    {'label': 'bourbon', 'value':'bourbon'},
                    {'label': 'blackberry brandy', 'value':'blackberry brandy'},
                    {'label': 'lemon peel', 'value':'lemon peel'},
                    {'label': 'sambuca', 'value':'sambuca'},
                    {'label': 'green chartreuse', 'value':'green chartreuse'},
                    {'label': 'irish cream', 'value':'irish cream'},
                    {'label': 'goldschlager', 'value':'goldschlager'},
                    {'label': 'champagne', 'value':'champagne'},
                    {'label': 'peach schnapps', 'value':'peach schnapps'},
                    {'label': 'sugar syrup', 'value':'sugar syrup'},
                    {'label': 'creme de mure', 'value':'creme de mure'},
                    {'label': 'bitters', 'value':'bitters'},
                    {'label': 'blue curacao', 'value':'blue curacao'},
                    {'label': 'rye whiskey', 'value':'rye whiskey'},
                    {'label': 'angostura bitters', 'value':'angostura bitters'},
                    {'label': 'passion fruit juice', 'value':'passion fruit juice'},
                    {'label': 'galliano', 'value':'galliano'},
                    {'label': 'prosecco', 'value':'prosecco'},
                    {'label': 'hot chocolate', 'value':'hot chocolate'},
                    {'label': 'cherry heering', 'value':'cherry heering'},
                    {'label': 'wormwood', 'value':'wormwood'},
                    {'label': 'corona', 'value':'corona'},
                    {'label': 'bacardi limon', 'value':'bacardi limon'},
                    {'label': 'everclear', 'value':'everclear'},
                    {'label': 'mountain dew', 'value':'mountain dew'},
                    {'label': 'surge', 'value':'surge'},
                    {'label': 'sloe gin', 'value':'sloe gin'},
                    {'label': 'midori melon liqueur', 'value':'midori melon liqueur'},
                    {'label': 'jägermeister', 'value':'jägermeister'},
                    {'label': 'southern comfort', 'value':'southern comfort'},
                    {'label': 'lime', 'value':'lime'},
                    {'label': 'sour mix', 'value':'sour mix'},
                    {'label': 'banana liqueur', 'value':'banana liqueur'},
                    {'label': 'vanilla ice-cream', 'value':'vanilla ice-cream'},
                    {'label': 'lemon', 'value':'lemon'},
                    {'label': 'powdered sugar', 'value':'powdered sugar'},
                    {'label': 'cherry', 'value':'cherry'},
                    {'label': 'sweet and sour', 'value':'sweet and sour'},
                    {'label': 'brandy', 'value':'brandy'},
                    {'label': 'cachaca', 'value':'cachaca'},
                    {'label': 'spiced rum', 'value':'spiced rum'},
                    {'label': 'ginger ale', 'value':'ginger ale'},
                    {'label': 'coca-cola', 'value':'coca-cola'},
                    {'label': 'cherry brandy', 'value':'cherry brandy'},
                    {'label': 'falernum', 'value':'falernum'},
                    {'label': 'añejo rum', 'value':'añejo rum'},
                    {'label': 'blackstrap rum', 'value':'blackstrap rum'},
                    {'label': 'white rum', 'value':'white rum'},
                    {'label': 'lager', 'value':'lager'},
                    {'label': 'campari', 'value':'campari'},
                    {'label': 'port', 'value':'port'},
                    {'label': 'carbonated water', 'value':'carbonated water'},
                    {'label': 'cointreau', 'value':'cointreau'},
                    {'label': 'water', 'value':'water'},
                    {'label': 'vanilla', 'value':'vanilla'},
                    {'label': 'caramel coloring', 'value':'caramel coloring'},
                    {'label': 'egg yolk', 'value':'egg yolk'},
                    {'label': 'lillet blanc', 'value':'lillet blanc'},
                    {'label': 'absinthe', 'value':'absinthe'},
                    {'label': 'chocolate liqueur', 'value':'chocolate liqueur'},
                    {'label': 'wine', 'value':'wine'},
                    {'label': 'vanilla extract', 'value':'vanilla extract'},
                    {'label': 'chocolate', 'value':'chocolate'},
                    {'label': 'almond flavoring', 'value':'almond flavoring'},
                    {'label': 'peach bitters', 'value':'peach bitters'},
                    {'label': 'cider', 'value':'cider'},
                    {'label': 'blackcurrant cordial', 'value':'blackcurrant cordial'},
                    {'label': 'fruit punch', 'value':'fruit punch'},
                    {'label': 'sprite', 'value':'sprite'},
                    {'label': 'olive', 'value':'olive'},
                    {'label': 'olive brine', 'value':'olive brine'},
                    {'label': 'ginger beer', 'value':'ginger beer'},
                    {'label': 'demerara sugar', 'value':'demerara sugar'},
                    {'label': 'pisco', 'value':'pisco'},
                    {'label': 'pineapple syrup', 'value':'pineapple syrup'},
                    {'label': 'st. germain', 'value':'st. germain'},
                    {'label': 'pepper', 'value':'pepper'},
                    {'label': 'lavender', 'value':'lavender'},
                    {'label': 'whiskey', 'value':'whiskey'},
                    {'label': 'hot damn', 'value':'hot damn'},
                    {'label': 'dubonnet rouge', 'value':'dubonnet rouge'},
                    {'label': 'cinnamon', 'value':'cinnamon'},
                    {'label': 'whipped cream', 'value':'whipped cream'},
                    {'label': 'chocolate syrup', 'value':'chocolate syrup'},
                    {'label': 'whipping cream', 'value':'whipping cream'},
                    {'label': 'vanilla syrup', 'value':'vanilla syrup'},
                    {'label': 'espresso', 'value':'espresso'},
                    {'label': 'egg', 'value':'egg'},
                    {'label': 'condensed milk', 'value':'condensed milk'},
                    {'label': 'apricot brandy', 'value':'apricot brandy'},
                    {'label': 'elderflower cordial', 'value':'elderflower cordial'},
                    {'label': 'mezcal', 'value':'mezcal'},
                    {'label': 'coffee liqueur', 'value':'coffee liqueur'},
                    {'label': 'rose', 'value':'rose'},
                    {'label': 'strawberries', 'value':'strawberries'},
                    {'label': 'orange', 'value':'orange'},
                    {'label': 'honey', 'value':'honey'},
                    {'label': 'figs', 'value':'figs'},
                    {'label': 'thyme', 'value':'thyme'},
                    {'label': 'benedictine', 'value':'benedictine'},
                    {'label': 'yoghurt', 'value':'yoghurt'},
                    {'label': 'banana', 'value':'banana'},
                    {'label': 'apple', 'value':'apple'},
                    {'label': 'apricot nectar', 'value':'apricot nectar'},
                    {'label': 'pomegranate juice', 'value':'pomegranate juice'},
                    {'label': 'raspberry liqueur', 'value':'raspberry liqueur'},
                    {'label': 'lillet', 'value':'lillet'},
                    {'label': 'orange peel', 'value':'orange peel'},
                    {'label': 'firewater', 'value':'firewater'},
                    {'label': 'absolut peppar', 'value':'absolut peppar'},
                    {'label': 'tabasco sauce', 'value':'tabasco sauce'},
                    {'label': 'dr. pepper', 'value':'dr. pepper'},
                    {'label': 'beer', 'value':'beer'},
                    {'label': 'sarsaparilla', 'value':'sarsaparilla'},
                    {'label': 'pineapple', 'value':'pineapple'},
                    {'label': 'peach vodka', 'value':'peach vodka'},
                    {'label': 'sirup of roses', 'value':'sirup of roses'},
                    {'label': 'red wine', 'value':'red wine'},
                    {'label': 'cloves', 'value':'cloves'},
                    {'label': 'malibu rum', 'value':'malibu rum'},
                    {'label': 'orange spiral', 'value':'orange spiral'},
                    {'label': 'green creme de menthe', 'value':'green creme de menthe'},
                    {'label': 'whisky', 'value':'whisky'},
                    {'label': 'tea', 'value':'tea'},
                    {'label': 'blackberries', 'value':'blackberries'},
                    {'label': 'cherry juice', 'value':'cherry juice'},
                    {'label': 'red chili flakes', 'value':'red chili flakes'},
                    {'label': 'ginger', 'value':'ginger'},
                    {'label': 'grape juice', 'value':'grape juice'},
                    {'label': 'carbonated soft drink', 'value':'carbonated soft drink'},
                    {'label': 'sherbet', 'value':'sherbet'},
                    {'label': 'corn syrup', 'value':'corn syrup'},
                    {'label': 'irish whiskey', 'value':'irish whiskey'},
                    {'label': 'butter', 'value':'butter'},
                    {'label': 'half-and-half', 'value':'half-and-half'},
                    {'label': 'marshmallows', 'value':'marshmallows'},
                    {'label': 'brown sugar', 'value':'brown sugar'},
                    {'label': 'iced tea', 'value':'iced tea'},
                    {'label': 'coconut syrup', 'value':'coconut syrup'},
                    {'label': 'peach brandy', 'value':'peach brandy'},
                    {'label': 'guinness stout', 'value':'guinness stout'},
                    {'label': 'aperol', 'value':'aperol'},
                    {'label': 'chambord raspberry liqueur', 'value':'chambord raspberry liqueur'},
                    {'label': 'jack daniels', 'value':'jack daniels'},
                    {'label': 'anis', 'value':'anis'},
                    {'label': 'jello', 'value':'jello'},
                    {'label': 'mint syrup', 'value':'mint syrup'},
                    {'label': 'yellow chartreuse', 'value':'yellow chartreuse'},
                    {'label': 'apple brandy', 'value':'apple brandy'},
                    {'label': 'tennessee whiskey', 'value':'tennessee whiskey'},
                    {'label': 'creme de cassis', 'value':'creme de cassis'},
                    {'label': 'grain alcohol', 'value':'grain alcohol'},
                    {'label': 'kiwi liqueur', 'value':'kiwi liqueur'},
                    {'label': 'bitter lemon', 'value':'bitter lemon'},
                    {'label': 'absolut kurant', 'value':'absolut kurant'},
                    {'label': 'kiwi', 'value':'kiwi'},
                    {'label': 'cranberry vodka', 'value':'cranberry vodka'},
                    {'label': 'apfelkorn', 'value':'apfelkorn'},
                    {'label': 'schweppes russchian', 'value':'schweppes russchian'},
                    {'label': 'kool-aid', 'value':'kool-aid'},
                    {'label': 'papaya', 'value':'papaya'},
                    {'label': 'lime peel', 'value':'lime peel'},
                    {'label': 'absolut citron', 'value':'absolut citron'},
                    {'label': 'asafoetida', 'value':'asafoetida'},
                    {'label': 'cayenne pepper', 'value':'cayenne pepper'},
                    {'label': 'drambuie', 'value':'drambuie'},
                    {'label': 'mango', 'value':'mango'},
                    {'label': 'tia maria', 'value':'tia maria'},
                    {'label': 'coconut liqueur', 'value':'coconut liqueur'},
                    {'label': 'fresh lemon juice', 'value':'fresh lemon juice'},
                    {'label': 'cumin seed', 'value':'cumin seed'},
                    {'label': 'cocoa powder', 'value':'cocoa powder'},
                    {'label': 'orgeat syrup', 'value':'orgeat syrup'},
                    {'label': 'tomato juice', 'value':'tomato juice'},
                    {'label': 'hot sauce', 'value':'hot sauce'},
                    {'label': 'worcestershire sauce', 'value':'worcestershire sauce'},
                    {'label': 'soy sauce', 'value':'soy sauce'},
                    {'label': 'pepsi cola', 'value':'pepsi cola'},
                    {'label': 'pina colada mix', 'value':'pina colada mix'},
                    {'label': 'daiquiri mix', 'value':'daiquiri mix'},
                    {'label': 'cardamom', 'value':'cardamom'},
                    {'label': 'black pepper', 'value':'black pepper'},
                    {'label': 'cucumber', 'value':'cucumber'},
                    {'label': 'white creme de menthe', 'value':'white creme de menthe'},
                    {'label': 'butterscotch schnapps', 'value':'butterscotch schnapps'},
                    {'label': 'lemon-lime soda', 'value':'lemon-lime soda'},
                    {'label': 'oreo cookie', 'value':'oreo cookie'},
                    {'label': 'jagermeister', 'value':'jagermeister'},
                    {'label': 'rosemary syrup', 'value':'rosemary syrup'},
                    {'label': 'rosemary', 'value':'rosemary'},
                    {'label': 'grape soda', 'value':'grape soda'},
                    {'label': 'orange curacao', 'value':'orange curacao'},
                    {'label': 'blended scotch', 'value':'blended scotch'},
                    {'label': 'honey syrup', 'value':'honey syrup'},
                    {'label': 'ginger syrup', 'value':'ginger syrup'},
                    {'label': 'islay single malt scotch', 'value':'islay single malt scotch'},
                    {'label': 'coconut milk', 'value':'coconut milk'},
                    {'label': 'passoa', 'value':'passoa'},
                    {'label': 'passion fruit syrup', 'value':'passion fruit syrup'},
                    {'label': 'cherry liqueur', 'value':'cherry liqueur'},
                    {'label': 'fresh lime juice', 'value':'fresh lime juice'},
                    {'label': 'pink lemonade', 'value':'pink lemonade'},
                    {'label': 'coffee brandy', 'value':'coffee brandy'},
                    {'label': 'lime vodka', 'value':'lime vodka'},
                    {'label': 'sherry', 'value':'sherry'},
                    {'label': 'black sambuca', 'value':'black sambuca'},
                    {'label': 'raspberry syrup', 'value':'raspberry syrup'},
                    {'label': '7-up', 'value':'7-up'},
                    {'label': 'crown royal', 'value':'crown royal'},
                    {'label': 'raspberry vodka', 'value':'raspberry vodka'},
                    {'label': 'ricard', 'value':'ricard'},
                    {'label': 'peychaud bitters', 'value':'peychaud bitters'},
                    {'label': 'amaro montenegro', 'value':'amaro montenegro'},
                    {'label': 'ruby port', 'value':'ruby port'},
                    {'label': 'blood orange', 'value':'blood orange'},
                    {'label': 'allspice', 'value':'allspice'},
                    {'label': 'advocaat', 'value':'advocaat'},
                    {'label': 'jim beam', 'value':'jim beam'},
                    {'label': 'godiva liqueur', 'value':'godiva liqueur'},
                    {'label': 'anisette', 'value':'anisette'},
                    {'label': 'cherries', 'value':'cherries'},
                    {'label': 'fresca', 'value':'fresca'},
                    {'label': 'coriander', 'value':'coriander'},
                    {'label': 'celery salt', 'value':'celery salt'},
                    {'label': 'rosso vermouth', 'value':'rosso vermouth'},
                    {'label': 'melon liqueur', 'value':'melon liqueur'},
                    {'label': 'yukon jack', 'value':'yukon jack'},
                    {'label': 'maple syrup', 'value':'maple syrup'},
                    {'label': 'limeade', 'value':'limeade'},
                    {'label': 'agave syrup', 'value':'agave syrup'},
                    {'label': 'white wine', 'value':'white wine'},
                    {'label': 'cream of coconut', 'value':'cream of coconut'},
                    {'label': 'peachtree schnapps', 'value':'peachtree schnapps'},
                    {'label': 'root beer', 'value':'root beer'},
                    {'label': 'gold rum', 'value':'gold rum'},
                    {'label': 'pernod', 'value':'pernod'},
                    {'label': 'ouzo', 'value':'ouzo'},
                    {'label': 'zima', 'value':'zima'}
                ],
                value='light rum'
            ),
            html.Button(id="dropdown-submit", children="Find a Cocktail"),
            html.Br(),
            html.H3("Choose your ingredients:"),
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
            html.H3("Ingredients"),
            html.Div(id="ingredients-output"),
            html.H3("Recipe"),
            html.Div(id="recipe-output"),
            html.H3("Missing Ingredients"),
            html.Div(id="missing-output")
        ], md=4),
        dbc.Col([
            html.H3("Cocktail Ideas"),
            html.Div(id="dropdown-output")
        ], md=4)
    ], style={"margin-top": "50px"})
], style={'backgroundColor': '#dcd6f7'},
    fluid=True)


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
    

@app.callback(Output("ingredients-output", "children"),
              [Input({"type": "recipe-button", "index": ALL}, "n_clicks")],
              [State({"type": "recipe-button", "index": ALL}, "id")])
def get_ingredients(n_clicks_list, button_ids):
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
        ingredients_str = db.getIngredients(key)
        #ingredients_dict = db.getIngredients(key)
        #ingredients_list = list(ingredients_dict.values())
        #ingredients_str = ", ".join(ingredients_list)
        return ingredients_str
    

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
        ingredients_str = db.getRecipe(key)
        #ingredients_dict = db.getIngredients(key)
        #ingredients_list = list(ingredients_dict.values())
        #ingredients_str = ", ".join(ingredients_list)
        return ingredients_str
    
       
@app.callback(Output("missing-output", "children"),
              [Input({"type": "recipe-button", "index": ALL}, "n_clicks")],
              [State({"type": "recipe-button", "index": ALL}, "id")])
def get_missing(n_clicks_list, button_ids):
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
        needs = db.getIngredients(key)
        
        have = list(pantry.keys())
        
        upper_have = []
        for i in have:
            g = i.upper().strip()
            g = g + " "
            upper_have.append(g)
            
        upper_needs =[]    
        for i in needs:
            g = i.upper().strip()
            g = g + " "
            upper_needs.append(g)
          
            
        print(repr(upper_have[0]))
        print(repr(upper_needs[0]))
        
        missing_ingredients = [item for item in upper_needs if item not in upper_have]

        return missing_ingredients
    


@app.callback(Output("dropdown-output", "children"),
              [Input("dropdown-submit", "n_clicks")],
              [State("cat-dropdown", "value"),
               State("type-dropdown", "value"),
               State("glass-dropdown", "value"),
               State("ingredients-dropdown", "value")])
def print_dropdowns(n_clicks, value1, value2, value3, value4):
    if n_clicks:
        ingredients_dict = db.getSpeceficDrink(value1,value2,value3,value4)
        if type(ingredients_dict) == str:
            ingredients_str = "No Cocktail Found"
        else:
            ingredients_list = list(ingredients_dict.values())
            ingredients_str = ", ".join(ingredients_list)
        #test = ", ".join([value1, value2])
        return ingredients_str
        
                    
# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
