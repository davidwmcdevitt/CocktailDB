import os
import requests
import json
import string
import tqdm
from rdflib import Graph, Literal, Namespace, RDF, URIRef


class cocktailDB():
    
    def __init__(self):
        
        self.data = []
        
        for alpha in tqdm.tqdm(string.ascii_lowercase):
            url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={alpha}"
            res = requests.get(url)
            results = res.json()
            if results['drinks']:
                self.data.extend(results['drinks'])
                
        self.json_objects = self.data.copy()
        
        
        for item in self.json_objects:
            item['ingredients'] = []
            for key in item:
                if "strIngredient" in key and item[key]:
                    item['ingredients'].append(item[key])
                    
            item['ingredients_string'] = ', '.join(item['ingredients']).lower()
            
            
        
        # Define the vocabulary
        drink = Namespace("http://example.com/drink/")
        
        # Create an RDF graph
        self.g = Graph()
        
        # Iterate over each JSON object and add RDF triples to the graph
        for obj in self.json_objects:
            drink_uri = URIRef(drink + obj['idDrink'])
            self.g.add((drink_uri, RDF.type, drink.Drink))
            self.g.add((drink_uri, drink.id, Literal(obj['idDrink'])))
            # g.add((drink_uri, drink.ingredients_string, Literal(obj['ingredients_string'])))
            self.g.add((drink_uri, drink.name, Literal(obj['strDrink'])))
            self.g.add((drink_uri, drink.alternateName, Literal(obj['strDrinkAlternate'])))
            self.g.add((drink_uri, drink.tags, Literal(obj['strTags'])))
            self.g.add((drink_uri, drink.category, Literal(obj['strCategory'])))
            self.g.add((drink_uri, drink.iba, Literal(obj['strIBA'])))
            self.g.add((drink_uri, drink.alcoholic, Literal(obj['strAlcoholic'])))
            self.g.add((drink_uri, drink.glass, Literal(obj['strGlass'])))
            self.g.add((drink_uri, drink.instructions, Literal(obj['strInstructions'])))
            
            # add triples for the list of ingredients
            self.ingredients = obj['ingredients_string'].split(", ")
            for ingredient in self.ingredients:
                self.g.add((drink_uri, drink.ingredient, Literal(ingredient)))
        
    
    def getCocktailIngredients(self, input):
    
      finalDict = {}
    
      #empty input
      if len(input) == 0:
        return ("Please provide a valid input")
    
      #get the input string, lowercase it, and convert it to tuple
      inputFinal = tuple(input.lower().split(","))
    
      if len(inputFinal) == 1:
        inputFinal = '("' + str(input.lower()) + '")'
    
      #concatenate the input string to the query 
      filterStr = "FILTER (?ingredient in " + str(inputFinal) + ")"
    
      #final query
      query = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?name
      WHERE {
          ?drink drink:name ?name .
          ?drink drink:category "Cocktail" .
          ?drink drink:ingredient ?ingredient .
          ''' + filterStr + '}'
    
      results = self.g.query(query)
    
      for i, row in enumerate(results):
        finalDict[i] = str(row['name'])
    
      return finalDict
  
    def getNonAlcoholicDrinkIngredient(self, input):
    
      #empty input
      if len(input) == 0:
        return ("Please provide a valid input")
    
      #get the input string, lowercase it, and convert it to tuple
      inputFinal = tuple(input.lower().split(","))
    
      if len(inputFinal) == 1:
        inputFinal = '("' + str(input.lower()) + '")'
        
      finalDict = {}
    
      #concatenate the input string to the query 
      filterStr = "FILTER (?ingredient in " + str(inputFinal) + ")"
    
      #final query
      query = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?name
      WHERE {
          ?drink drink:name ?name .
          ?drink drink:alcoholic "Non alcoholic" .
          ?drink drink:ingredient ?ingredient .
          ''' + filterStr + '}'
    
      results = self.g.query(query)
    
      if len(results) == 0:
        return("The drink does not exist")
    
      for i, row in enumerate(results):
        finalDict[i] = str(row['name'])
    
      return finalDict
    
  
    def getIngredients(self,input):
    
      #empty input
      if len(input) == 0:
        return ("Please provide a valid input")
        
      finalList = []
    
      #concatenate the input string to the query 
      filterStr = "?drink drink:name '" + str(input) + "' ."
    
      #final query
      query = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?ingredient
         WHERE {
             ?drink drink:ingredient ?ingredient .
          ''' + filterStr + '}'
    
      results = self.g.query(query)
    
      #instructions query
      instructionsQuery = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?instructions
         WHERE {
             ?drink drink:instructions ?instructions .
          ''' + filterStr + '}'
    
      results2 = self.g.query(instructionsQuery)
    
      if len(results) == 0:
        return("The drink does not exist")
      
      for i, row in enumerate(results):
        finalList.append(str(row['ingredient']+" \n "))
      
      #for i, row in enumerate(results2):
        #finalList.append(str(row['instructions']))
    
      return finalList
  
    def getRecipe(self,input):
    
      #empty input
      if len(input) == 0:
        return ("Please provide a valid input")
        
      finalList = []
    
      #concatenate the input string to the query 
      filterStr = "?drink drink:name '" + str(input) + "' ."
    
      #final query
      query = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?ingredient
         WHERE {
             ?drink drink:ingredient ?ingredient .
          ''' + filterStr + '}'
    
      results = self.g.query(query)
    
      #instructions query
      instructionsQuery = '''
      PREFIX drink: <http://example.com/drink/>
      
      SELECT DISTINCT ?instructions
         WHERE {
             ?drink drink:instructions ?instructions .
          ''' + filterStr + '}'
    
      results2 = self.g.query(instructionsQuery)
    
      if len(results) == 0:
        return("The drink does not exist")
      
      #for i, row in enumerate(results):
        #finalList.append(str(row['ingredient']+" \n "))
      
      for i, row in enumerate(results2):
        finalList.append(str(row['instructions']+" \n "))
    
      return finalList

    
    def getSpeceficDrink(self, drinkCategory, drinkType, glassType, containsIngredient):
      

      drinkCategory = "?drink drink:category '"+ drinkCategory + "' ." + "\n"
      drinkType = "?drink drink:alcoholic '"+ drinkType + "' ."+ "\n"
      glassType = "?drink drink:glass '"+ glassType + "' ."+ "\n"
    
      #Ingredient tuple
      containsIngredientFinal = tuple(containsIngredient.lower().split(","))
    
      if len(containsIngredientFinal) == 1:
        containsIngredient = '("' + str(containsIngredient) + '")'
      
      filterIngredient = "FILTER (?ingredient in " + str(containsIngredient) + ")"
    
      #final query
      query = '''
      PREFIX drink: <http://example.com/drink/>
      
        SELECT DISTINCT ?name
        WHERE {
          ?drink drink:name ?name .
          ''' + drinkCategory + drinkType + glassType + \
          "?drink drink:ingredient ?ingredient ." + "\n" +\
          filterIngredient + '}'
    
      results = self.g.query(query)
    
      finalDict = {}
    
      if len(results) == 0:
        return("The drink does not exist")
    
      for i, row in enumerate(results):
        finalDict[i] = str(row['name'])
    
      return finalDict