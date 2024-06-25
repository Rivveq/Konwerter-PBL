import json

# Open file
with open('jednostki.json', 'r', encoding='utf-8') as file:
    dane_jednostek = json.load(file)

def get_item(category, item):
    """This function returns a value associated with an item in the json dictionary.

    Args:
        - category: Item category in the json file (for example masa, czas).
        - item: Specified item in the category (for example in "masa": tona, gram).
    
    Returns:
        float: Value assigned to the specified item in the dictionary.
    """

    return dane_jednostek[category][item]

def get_convert_factor(category, input, output):
    """This function returns a calculated conversion factor by which to multiply in order to convert one unit to another.

    Args:
        - category: Item category in the json file (for example masa, czas).
        - input: unit to convert from.
        - output: unit to convert to.
    
    Returns:
        float: Conversion value for calculations.
    """

    input_factor = get_item(category, input)
    output_factor = get_item(category, output)
    return output_factor/input_factor

def convert(category, input, output, quantity: float):
    """This function returns a calculated conversion between two units.

    Args:
        - category: Item category in the json file (for example masa, czas).
        - input: unit to convert from.
        - output: unit to convert to.
        - quantity (float): quantity to be converted.
    
    Returns:
        float: Value of the output unit after conversion from the input.
    """
    return quantity * get_convert_factor(category, input, output)

def fetch_items(category):
    """This function returns a list of items from a category.

    Args:
        - category: Item category in the json file (for example masa, czas).
    """

    return list(dane_jednostek[category].keys())