import connexion
import six

from swagger_server.models.branded_food_object import BrandedFoodObject  # noqa: E501
from swagger_server.models.ingredient_object import IngredientObject  # noqa: E501
from swagger_server import util


def food_branded_barcode_php_get(code):  # noqa: E501
    """Get a branded food item using a barcode

    # Get data for a branded food using the food&#x27;s UPC/EAN barcode.  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/barcode.php?api_key&#x3D;API_KEY&amp;code&#x3D;CODE&#x60;&#x60;&#x60;  # noqa: E501

    :param code: UPC/EAN barcode  __Example:__ 0842234000988  __Resources:__ [Database search](https://chompthis.com/api/lookup.php)  _Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for tips and tricks._ 
    :type code: str

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_id_php_get(id, source=None):  # noqa: E501
    """Get a branded food item using an ID number

    # Get data for a branded food using Chomp&#x27;s internal ID number.  _Alternatively, set the \&quot;source\&quot; parameter to \&quot;USDA\&quot; and use the food&#x27;s FDC ID._  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/id.php?api_key&#x3D;API_KEY&amp;id&#x3D;ID&#x60;&#x60;&#x60;  # noqa: E501

    :param id: Chomp branded food ID.  _Set \&quot;source&#x3D;USDA\&quot; if you wish to pass in the food&#x27;s FoodData Central ID (fdc_id)._  __Example #1:__ 15  __Resources:__ [Find branded food IDs](https://chompthis.com/api/lookup.php) 
    :type id: int
    :param source: Specify the data source (optional).  You must pass in \&quot;USDA\&quot; if you want to look up a food item using a USDA FDC ID.  __Example:__ USDA _(defaults to \&quot;Chomp\&quot;)_ 
    :type source: str

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_name_php_get(name, limit=None):  # noqa: E501
    """Get a branded food item by name

    # Search for branded food items by name.  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/name.php?api_key&#x3D;API_KEY&amp;name&#x3D;NAME&#x60;&#x60;&#x60;  # noqa: E501

    :param name: Branded food name  __Example:__ Starburst  __Resources:__ [Find branded food names](https://chompthis.com/api/lookup.php) 
    :type name: str
    :param limit: Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_ 
    :type limit: int

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_search_php_get(allergen=None, brand=None, category=None, country=None, diet=None, ingredient=None, keyword=None, mineral=None, nutrient=None, palm_oil=None, trace=None, vitamin=None, limit=None, page=None):  # noqa: E501
    """Get data for branded food items using various search parameters

    # Search for branded food items using various parameters.  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/search.php?api_key&#x3D;API_KEY&amp;brand&#x3D;BRAND&amp;country&#x3D;COUNTRY&amp;page&#x3D;1&#x60;&#x60;&#x60;  ___Tip:__ Get started by using the [Query Builder](https://chompthis.com/api/build.php)._  # noqa: E501

    :param allergen: Specify a required allergen ingredient (optional)  __Example__: Peanuts  __Resources__: [List of allergens](https://chompthis.com/api/data/allergen.php) 
    :type allergen: str
    :param brand: Specify a required brand (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php) 
    :type brand: str
    :param category: Specify a required category (optional)  __Example__: Pasta Dishes  __Resources__: [List of categories](https://chompthis.com/api/data/category.php) 
    :type category: str
    :param country: Specify a required country (optional)  __Example__: United States  __Resources__: [List of countries](https://chompthis.com/api/data/country.php) 
    :type country: str
    :param diet: Specify a required diet (optional)  _Filters the search to only include food items that are considered compatible with the following diets: Vegan, Vegetarian, Gluten Free_  __Example__: Gluten Free  __Resources__: [List of diets](https://chompthis.com/api/data/lifestyle.php) 
    :type diet: str
    :param ingredient: Specify a required ingredient (optional)  __Example__: Salt  __Resources__: [List of ingredients](https://chompthis.com/api/data/ingredient.php) 
    :type ingredient: str
    :param keyword: Specify a required keyword (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php) 
    :type keyword: str
    :param mineral: Specify a required mineral (optional)  __Example__: Potassium  __Resources__: [List of minerals](https://chompthis.com/api/data/mineral.php) 
    :type mineral: str
    :param nutrient: Specify a required nutrition label item (optional)  __Example__: Caffeine  __Resources__: [List of nutrition label items](https://chompthis.com/api/data/nutrition.php) 
    :type nutrient: str
    :param palm_oil: Specify a required palm oil ingredient (optional)  __Example__: E160a Beta Carotene  __Resources__: [List of palm oil ingredients](https://chompthis.com/api/data/palm-oil.php) 
    :type palm_oil: str
    :param trace: Specify a required trace ingredient (optional)  __Example__: Tree Nuts  __Resources__: [List of trace ingredients](https://chompthis.com/api/data/trace.php) 
    :type trace: str
    :param vitamin: Specify a required vitamin (optional)  __Example__: Biotin  __Resources__: [List of vitamins](https://chompthis.com/api/data/vitamin.php) 
    :type vitamin: str
    :param limit: Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_ 
    :type limit: int
    :param page: Specify the search response page number.  _Each page will contain up to 10 items._  __Example__: 1 _(default)_ 
    :type page: int

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def ingredient_search_php_get(find, list, raw=None, limit=None):  # noqa: E501
    """Get raw/generic food ingredient item(s)

    # Get data for a specific ingredient or a specific set of ingredients.  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/ingredient/search.php?api_key&#x3D;API_KEY&amp;find&#x3D;STRING/LIST&amp;list&#x3D;BOOLEAN&amp;raw&#x3D;BOOLEAN&#x60;&#x60;&#x60;  # noqa: E501

    :param find: Specify the ingredient name(s).  __Example #1:__ broccoli  __Example #2:__ broccoli,cauliflower,spinach  ___Important Note:__ Set the \&quot;is_list\&quot; parameter to true before passing in a comma-separated list of ingredients._ 
    :type find: int
    :param list: Specify if you are searching for multiple ingredients.  _Setting this to true will configure this endpoint so that it accepts a comma-separated list of ingredients._  _By default, this endpoint expects a single ingredient._  __Example:__ true _(defaults to false)_ 
    :type list: bool
    :param raw: Specify if you only want data for raw ingredients.  __Example:__ true _(defaults to true)_ 
    :type raw: bool
    :param limit: Set maximum number of records you want the API to return.  ___Important Note:__ Setting this to \&quot;1\&quot; will return 1 record per search term._  __Example:__ 1 _(defaults to 1, max is 3)_ 
    :type limit: int

    :rtype: IngredientObject
    """
    return 'do some magic!'
