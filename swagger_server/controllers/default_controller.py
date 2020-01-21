import connexion
import six

from swagger_server.models.branded_food_object import BrandedFoodObject  # noqa: E501
from swagger_server.models.ingredient_object import IngredientObject  # noqa: E501
from swagger_server import util


def food_branded_barcode_php_get(code):  # noqa: E501
    """Get a branded food item using a barcode

    # Get data for a branded food using the food&#x27;s UPC/EAN barcode.  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/barcode.php?api_key&#x3D;API_KEY&amp;code&#x3D;CODE&#x60;&#x60;&#x60;  # noqa: E501

    :param code: UPC/EAN barcode  __Example:__ &amp;code&#x3D;0842234000988  __Tips:__    - Use our [food lookup tool](https://chompthis.com/api/lookup.php).   - Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for general tips and tricks. 
    :type code: str

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_id_php_get(id, source=None):  # noqa: E501
    """Get a branded food item using an ID number

    # Get data for a branded food using Chomp&#x27;s internal ID number.  _Alternatively, set the \&quot;source\&quot; parameter to \&quot;USDA\&quot; and use the food&#x27;s FDC ID._  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/id.php?api_key&#x3D;API_KEY&amp;id&#x3D;ID&#x60;&#x60;&#x60;  # noqa: E501

    :param id: The ID number of a branded food item.  __Example #1:__ &amp;id&#x3D;15  __Example #2:__ &amp;id&#x3D;FDC_ID&amp;source&#x3D;USDA  ___Tip:__ Get started by using our  [ood lookup tool](https://chompthis.com/api/lookup.php)._ 
    :type id: int
    :param source: Configure the endpoint to accept food IDs from various data sources. This endpoint defaults to Chomp but can accept FDC IDs.  __Example:__ &amp;source&#x3D;Chomp  ___Important Note:__ Pass in &amp;source&#x3D;USDA if you want to look up food items using a USDA FDC ID._ 
    :type source: str

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_name_php_get(name, limit=None, page=None):  # noqa: E501
    """Get a branded food item by name

    # Search for branded food items by name.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren&#x27;t sure how to upgrade your subscription._  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/name.php?api_key&#x3D;API_KEY&amp;name&#x3D;NAME&#x60;&#x60;&#x60;  # noqa: E501

    :param name: Search for branded food items using a general food name keyword. This does not have to exactly match the \&quot;official\&quot; name for the food.  __Example:__ &amp;name&#x3D;Starburst  ___Tip:__ Get started by using our [food lookup tool](https://chompthis.com/api/lookup.php)._ 
    :type name: str
    :param limit: Set maximum number of records you want the API to return.  __Example:__ &amp;limit&#x3D;10 
    :type limit: int
    :param page: This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &amp;page&#x3D;1 
    :type page: int

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_branded_search_php_get(allergen=None, brand=None, category=None, country=None, diet=None, ingredient=None, keyword=None, mineral=None, nutrient=None, palm_oil=None, trace=None, vitamin=None, limit=None, page=None):  # noqa: E501
    """Get data for branded food items using various search parameters

    # Search for branded food items using various parameters.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren&#x27;t sure how to upgrade your subscription._  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/food/branded/search.php?api_key&#x3D;API_KEY&amp;brand&#x3D;BRAND&amp;country&#x3D;COUNTRY&amp;page&#x3D;1&#x60;&#x60;&#x60;  ___Tip:__ Get started by using the [Query Builder](https://chompthis.com/api/build.php)._  # noqa: E501

    :param allergen: Filter the search to only include branded foods that contain a specific allergen.  __Example__: &amp;allergen&#x3D;Peanuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type allergen: str
    :param brand: Filter the search to only include branded foods that are owned by a specific brand.  __Example__: &amp;brand&#x3D;Starbucks 
    :type brand: str
    :param category: Filter the search to only include branded foods from a specific category.  __Example__: &amp;category&#x3D;Plant Based Foods 
    :type category: str
    :param country: Filter the search to only include branded foods that are sold in a specific country.  __Example__: &amp;country&#x3D;United States  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type country: str
    :param diet: Filter the search to only include branded foods that are considered compatible with a specific diet.  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type diet: str
    :param ingredient: Filter the search to only include branded foods that contain a specific ingredient.  __Example__: &amp;ingredient&#x3D;Salt 
    :type ingredient: str
    :param keyword: Filter the search to only include branded foods that are associated with a specific keyword.  __Example__: &amp;keyword&#x3D;Organic  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type keyword: str
    :param mineral: Filter the search to only include branded foods that contain a specific mineral.  __Example__: &amp;mineral&#x3D;Potassium 
    :type mineral: str
    :param nutrient: Filter the search to only include branded foods that contain a specific nutrient.  __Example__: &amp;nutrient&#x3D;Caffeine  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type nutrient: str
    :param palm_oil: Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  __Example__: &amp;palm_oil&#x3D;E160a Beta Carotene 
    :type palm_oil: str
    :param trace: Filter the search to only include branded foods that contain a specific trace ingredient.  __Example__: &amp;trace&#x3D;Tree Nuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._ 
    :type trace: str
    :param vitamin: Filter the search to only include branded foods that contain a specific vitamin.  __Example__: &amp;vitamin&#x3D;Biotin 
    :type vitamin: str
    :param limit: Set maximum number of records you want the API to return.  __Example:__ &amp;limit&#x3D;10 
    :type limit: int
    :param page: This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &amp;page&#x3D;1 
    :type page: int

    :rtype: BrandedFoodObject
    """
    return 'do some magic!'


def food_ingredient_search_php_get(find, list, raw=None, limit=None):  # noqa: E501
    """Get raw/generic food ingredient item(s)

    # Get data for a specific ingredient or a specific set of ingredients.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren&#x27;t sure how to upgrade your subscription._  __Example:__ &#x60;&#x60;&#x60;https://chompthis.com/api/v2/ingredient/search.php?api_key&#x3D;API_KEY&amp;find&#x3D;STRING/LIST&amp;list&#x3D;BOOLEAN&amp;raw&#x3D;BOOLEAN&#x60;&#x60;&#x60;  # noqa: E501

    :param find: Search our database for a single ingredient or a specific set of ingredients.  __Example #1:__ &amp;find&#x3D;broccoli  __Example #2:__ &amp;find&#x3D;broccoli,cauliflower,spinach&amp;list&#x3D;true  __Important List Notes:__    - Set the \&quot;list\&quot; parameter to \&quot;true\&quot; before passing in a comma-separated list of ingredients.   - Comma-separated lists cannot contain more than __15 ingredients__. You must perform additional API calls if you are looking up more than 15 ingredients. 
    :type find: int
    :param list: Setting _&amp;list&#x3D;true_ will configure this endpoint to allow searching for ingredients using a comma-separated list. By default, this endpoint will __only__ return results for the first ingredient.  __Example:__ &amp;list&#x3D;true 
    :type list: bool
    :param raw: Optionally filter the search result to only include raw ingredients.  __Example:__ &amp;raw&#x3D;true 
    :type raw: bool
    :param limit: Set maximum number of records you want the API to return, per search term.  __Example:__ &amp;limit&#x3D;3 
    :type limit: int

    :rtype: IngredientObject
    """
    return 'do some magic!'
