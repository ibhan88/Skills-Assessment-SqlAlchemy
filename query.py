"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # Database query
    model_info = Model.query.filter(Model.year == year).all()

    # To print out the info from each object in model_info
    for item in model_info:
        print "Model: " + item.name
        print "Brand: " + item.brand_name
        print "HQ: " + item.brands.headquarters
        print "-" * 60


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # Used distinct call in query, so that the model names do not repeat
    brand_info = Model.query.distinct(Model.name).all()

    # Used dictionary key/value pairs to store data
    brand_models = {}

    # Add to dictionary
    for item in brand_info:
        brand_models[item.brand_name] = brand_models.get(item.brand_name, []) + [item.name]

    # Print out the data stored in the dictionary, showing the brand name,
    # then the model names for that brand.
    for brand, model in brand_models.items():
        print brand.upper()
        print ", ".join(model)
        print "-" * 60


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)


# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
########################################################################
# It is a BaseQuery object. It contains the resulting object(s) of the query.
# Records must be fetched using .all(), .first(), .one(). Using .all(), 1 Brand
# object is seen, which is an object that contains all the information in the
# row that fulfills the requirement that the name is "Ford".


# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
########################################################################
# An association table is a table that connects other tables together. It
# serves to show the relationship between the other tables it connects. Thus,
# the association table does not contain any additional data unique to itself,
# but it stores data from the other tables as foreign keys to show how that
# data relates to one another. Therefore, association tables are to manage
# the many to many relationship type.


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Takes a string as input, then return a list of objects whose brand names
    contains OR equals the input string."""

    # Database query
    brand_names = Brand.query.filter((Brand.name.like('%'+mystr+'%') | (Brand.name == mystr))).all()

    return brand_names


def get_models_between(start_year, end_year):
    """Takes start and end years as input, then return a list of objects whose
    model years are in between the start (inclusive) year and end (exclusive)
    year."""

    # Database query
    models_in_range = Model.query.filter(start_year <= Model.year, Model.year < end_year).all()

    return models_in_range
