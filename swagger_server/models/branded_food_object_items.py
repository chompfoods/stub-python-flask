# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.branded_food_object_calorie_conversion_factor import BrandedFoodObjectCalorieConversionFactor  # noqa: F401,E501
from swagger_server.models.branded_food_object_components import BrandedFoodObjectComponents  # noqa: F401,E501
from swagger_server.models.branded_food_object_country_details import BrandedFoodObjectCountryDetails  # noqa: F401,E501
from swagger_server.models.branded_food_object_diet_flags import BrandedFoodObjectDietFlags  # noqa: F401,E501
from swagger_server.models.branded_food_object_diet_labels import BrandedFoodObjectDietLabels  # noqa: F401,E501
from swagger_server.models.branded_food_object_ingredients import BrandedFoodObjectIngredients  # noqa: F401,E501
from swagger_server.models.branded_food_object_nutrients import BrandedFoodObjectNutrients  # noqa: F401,E501
from swagger_server.models.branded_food_object_package import BrandedFoodObjectPackage  # noqa: F401,E501
from swagger_server.models.branded_food_object_packaging_photos import BrandedFoodObjectPackagingPhotos  # noqa: F401,E501
from swagger_server.models.branded_food_object_portions import BrandedFoodObjectPortions  # noqa: F401,E501
from swagger_server.models.branded_food_object_serving import BrandedFoodObjectServing  # noqa: F401,E501
from swagger_server import util


class BrandedFoodObjectItems(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, barcode: str=None, name: str=None, brand: str=None, ingredients: BrandedFoodObjectIngredients=None, package: BrandedFoodObjectPackage=None, serving: BrandedFoodObjectServing=None, categories: List[str]=None, nutrients: BrandedFoodObjectNutrients=None, calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor=None, protein_conversion_factor: float=None, diet_labels: BrandedFoodObjectDietLabels=None, diet_flags: List[BrandedFoodObjectDietFlags]=None, packaging_photos: BrandedFoodObjectPackagingPhotos=None, components: List[BrandedFoodObjectComponents]=None, portions: List[BrandedFoodObjectPortions]=None, allergens: List[str]=None, brand_list: List[str]=None, countries: List[str]=None, country_details: BrandedFoodObjectCountryDetails=None, palm_oil_ingredients: List[str]=None, ingredient_list: List[str]=None, has_english_ingredients: bool=None, minerals: List[str]=None, traces: List[str]=None, vitamins: List[str]=None, common_names: List[str]=None, description: str=None, keywords: List[str]=None, footnote: str=None):  # noqa: E501
        """BrandedFoodObjectItems - a model defined in Swagger

        :param barcode: The barcode of this BrandedFoodObjectItems.  # noqa: E501
        :type barcode: str
        :param name: The name of this BrandedFoodObjectItems.  # noqa: E501
        :type name: str
        :param brand: The brand of this BrandedFoodObjectItems.  # noqa: E501
        :type brand: str
        :param ingredients: The ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type ingredients: BrandedFoodObjectIngredients
        :param package: The package of this BrandedFoodObjectItems.  # noqa: E501
        :type package: BrandedFoodObjectPackage
        :param serving: The serving of this BrandedFoodObjectItems.  # noqa: E501
        :type serving: BrandedFoodObjectServing
        :param categories: The categories of this BrandedFoodObjectItems.  # noqa: E501
        :type categories: List[str]
        :param nutrients: The nutrients of this BrandedFoodObjectItems.  # noqa: E501
        :type nutrients: BrandedFoodObjectNutrients
        :param calorie_conversion_factor: The calorie_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :type calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor
        :param protein_conversion_factor: The protein_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :type protein_conversion_factor: float
        :param diet_labels: The diet_labels of this BrandedFoodObjectItems.  # noqa: E501
        :type diet_labels: BrandedFoodObjectDietLabels
        :param diet_flags: The diet_flags of this BrandedFoodObjectItems.  # noqa: E501
        :type diet_flags: List[BrandedFoodObjectDietFlags]
        :param packaging_photos: The packaging_photos of this BrandedFoodObjectItems.  # noqa: E501
        :type packaging_photos: BrandedFoodObjectPackagingPhotos
        :param components: The components of this BrandedFoodObjectItems.  # noqa: E501
        :type components: List[BrandedFoodObjectComponents]
        :param portions: The portions of this BrandedFoodObjectItems.  # noqa: E501
        :type portions: List[BrandedFoodObjectPortions]
        :param allergens: The allergens of this BrandedFoodObjectItems.  # noqa: E501
        :type allergens: List[str]
        :param brand_list: The brand_list of this BrandedFoodObjectItems.  # noqa: E501
        :type brand_list: List[str]
        :param countries: The countries of this BrandedFoodObjectItems.  # noqa: E501
        :type countries: List[str]
        :param country_details: The country_details of this BrandedFoodObjectItems.  # noqa: E501
        :type country_details: BrandedFoodObjectCountryDetails
        :param palm_oil_ingredients: The palm_oil_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type palm_oil_ingredients: List[str]
        :param ingredient_list: The ingredient_list of this BrandedFoodObjectItems.  # noqa: E501
        :type ingredient_list: List[str]
        :param has_english_ingredients: The has_english_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type has_english_ingredients: bool
        :param minerals: The minerals of this BrandedFoodObjectItems.  # noqa: E501
        :type minerals: List[str]
        :param traces: The traces of this BrandedFoodObjectItems.  # noqa: E501
        :type traces: List[str]
        :param vitamins: The vitamins of this BrandedFoodObjectItems.  # noqa: E501
        :type vitamins: List[str]
        :param common_names: The common_names of this BrandedFoodObjectItems.  # noqa: E501
        :type common_names: List[str]
        :param description: The description of this BrandedFoodObjectItems.  # noqa: E501
        :type description: str
        :param keywords: The keywords of this BrandedFoodObjectItems.  # noqa: E501
        :type keywords: List[str]
        :param footnote: The footnote of this BrandedFoodObjectItems.  # noqa: E501
        :type footnote: str
        """
        self.swagger_types = {
            'barcode': str,
            'name': str,
            'brand': str,
            'ingredients': BrandedFoodObjectIngredients,
            'package': BrandedFoodObjectPackage,
            'serving': BrandedFoodObjectServing,
            'categories': List[str],
            'nutrients': BrandedFoodObjectNutrients,
            'calorie_conversion_factor': BrandedFoodObjectCalorieConversionFactor,
            'protein_conversion_factor': float,
            'diet_labels': BrandedFoodObjectDietLabels,
            'diet_flags': List[BrandedFoodObjectDietFlags],
            'packaging_photos': BrandedFoodObjectPackagingPhotos,
            'components': List[BrandedFoodObjectComponents],
            'portions': List[BrandedFoodObjectPortions],
            'allergens': List[str],
            'brand_list': List[str],
            'countries': List[str],
            'country_details': BrandedFoodObjectCountryDetails,
            'palm_oil_ingredients': List[str],
            'ingredient_list': List[str],
            'has_english_ingredients': bool,
            'minerals': List[str],
            'traces': List[str],
            'vitamins': List[str],
            'common_names': List[str],
            'description': str,
            'keywords': List[str],
            'footnote': str
        }

        self.attribute_map = {
            'barcode': 'barcode',
            'name': 'name',
            'brand': 'brand',
            'ingredients': 'ingredients',
            'package': 'package',
            'serving': 'serving',
            'categories': 'categories',
            'nutrients': 'nutrients',
            'calorie_conversion_factor': 'calorie_conversion_factor',
            'protein_conversion_factor': 'protein_conversion_factor',
            'diet_labels': 'diet_labels',
            'diet_flags': 'diet_flags',
            'packaging_photos': 'packaging_photos',
            'components': 'components',
            'portions': 'portions',
            'allergens': 'allergens',
            'brand_list': 'brand_list',
            'countries': 'countries',
            'country_details': 'country_details',
            'palm_oil_ingredients': 'palm_oil_ingredients',
            'ingredient_list': 'ingredient_list',
            'has_english_ingredients': 'has_english_ingredients',
            'minerals': 'minerals',
            'traces': 'traces',
            'vitamins': 'vitamins',
            'common_names': 'common_names',
            'description': 'description',
            'keywords': 'keywords',
            'footnote': 'footnote'
        }
        self._barcode = barcode
        self._name = name
        self._brand = brand
        self._ingredients = ingredients
        self._package = package
        self._serving = serving
        self._categories = categories
        self._nutrients = nutrients
        self._calorie_conversion_factor = calorie_conversion_factor
        self._protein_conversion_factor = protein_conversion_factor
        self._diet_labels = diet_labels
        self._diet_flags = diet_flags
        self._packaging_photos = packaging_photos
        self._components = components
        self._portions = portions
        self._allergens = allergens
        self._brand_list = brand_list
        self._countries = countries
        self._country_details = country_details
        self._palm_oil_ingredients = palm_oil_ingredients
        self._ingredient_list = ingredient_list
        self._has_english_ingredients = has_english_ingredients
        self._minerals = minerals
        self._traces = traces
        self._vitamins = vitamins
        self._common_names = common_names
        self._description = description
        self._keywords = keywords
        self._footnote = footnote

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObjectItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject_items of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectItems
        """
        return util.deserialize_model(dikt, cls)

    @property
    def barcode(self) -> str:
        """Gets the barcode of this BrandedFoodObjectItems.

        EAN/UPC barcode  # noqa: E501

        :return: The barcode of this BrandedFoodObjectItems.
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode: str):
        """Sets the barcode of this BrandedFoodObjectItems.

        EAN/UPC barcode  # noqa: E501

        :param barcode: The barcode of this BrandedFoodObjectItems.
        :type barcode: str
        """

        self._barcode = barcode

    @property
    def name(self) -> str:
        """Gets the name of this BrandedFoodObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :return: The name of this BrandedFoodObjectItems.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BrandedFoodObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :param name: The name of this BrandedFoodObjectItems.
        :type name: str
        """

        self._name = name

    @property
    def brand(self) -> str:
        """Gets the brand of this BrandedFoodObjectItems.

        The brand name that owns this item  # noqa: E501

        :return: The brand of this BrandedFoodObjectItems.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        """Sets the brand of this BrandedFoodObjectItems.

        The brand name that owns this item  # noqa: E501

        :param brand: The brand of this BrandedFoodObjectItems.
        :type brand: str
        """

        self._brand = brand

    @property
    def ingredients(self) -> BrandedFoodObjectIngredients:
        """Gets the ingredients of this BrandedFoodObjectItems.


        :return: The ingredients of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectIngredients
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: BrandedFoodObjectIngredients):
        """Sets the ingredients of this BrandedFoodObjectItems.


        :param ingredients: The ingredients of this BrandedFoodObjectItems.
        :type ingredients: BrandedFoodObjectIngredients
        """

        self._ingredients = ingredients

    @property
    def package(self) -> BrandedFoodObjectPackage:
        """Gets the package of this BrandedFoodObjectItems.


        :return: The package of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectPackage
        """
        return self._package

    @package.setter
    def package(self, package: BrandedFoodObjectPackage):
        """Sets the package of this BrandedFoodObjectItems.


        :param package: The package of this BrandedFoodObjectItems.
        :type package: BrandedFoodObjectPackage
        """

        self._package = package

    @property
    def serving(self) -> BrandedFoodObjectServing:
        """Gets the serving of this BrandedFoodObjectItems.


        :return: The serving of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectServing
        """
        return self._serving

    @serving.setter
    def serving(self, serving: BrandedFoodObjectServing):
        """Sets the serving of this BrandedFoodObjectItems.


        :param serving: The serving of this BrandedFoodObjectItems.
        :type serving: BrandedFoodObjectServing
        """

        self._serving = serving

    @property
    def categories(self) -> List[str]:
        """Gets the categories of this BrandedFoodObjectItems.


        :return: The categories of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]):
        """Sets the categories of this BrandedFoodObjectItems.


        :param categories: The categories of this BrandedFoodObjectItems.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def nutrients(self) -> BrandedFoodObjectNutrients:
        """Gets the nutrients of this BrandedFoodObjectItems.


        :return: The nutrients of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectNutrients
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients: BrandedFoodObjectNutrients):
        """Sets the nutrients of this BrandedFoodObjectItems.


        :param nutrients: The nutrients of this BrandedFoodObjectItems.
        :type nutrients: BrandedFoodObjectNutrients
        """

        self._nutrients = nutrients

    @property
    def calorie_conversion_factor(self) -> BrandedFoodObjectCalorieConversionFactor:
        """Gets the calorie_conversion_factor of this BrandedFoodObjectItems.


        :return: The calorie_conversion_factor of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectCalorieConversionFactor
        """
        return self._calorie_conversion_factor

    @calorie_conversion_factor.setter
    def calorie_conversion_factor(self, calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor):
        """Sets the calorie_conversion_factor of this BrandedFoodObjectItems.


        :param calorie_conversion_factor: The calorie_conversion_factor of this BrandedFoodObjectItems.
        :type calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor
        """

        self._calorie_conversion_factor = calorie_conversion_factor

    @property
    def protein_conversion_factor(self) -> float:
        """Gets the protein_conversion_factor of this BrandedFoodObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :return: The protein_conversion_factor of this BrandedFoodObjectItems.
        :rtype: float
        """
        return self._protein_conversion_factor

    @protein_conversion_factor.setter
    def protein_conversion_factor(self, protein_conversion_factor: float):
        """Sets the protein_conversion_factor of this BrandedFoodObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :param protein_conversion_factor: The protein_conversion_factor of this BrandedFoodObjectItems.
        :type protein_conversion_factor: float
        """

        self._protein_conversion_factor = protein_conversion_factor

    @property
    def diet_labels(self) -> BrandedFoodObjectDietLabels:
        """Gets the diet_labels of this BrandedFoodObjectItems.


        :return: The diet_labels of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectDietLabels
        """
        return self._diet_labels

    @diet_labels.setter
    def diet_labels(self, diet_labels: BrandedFoodObjectDietLabels):
        """Sets the diet_labels of this BrandedFoodObjectItems.


        :param diet_labels: The diet_labels of this BrandedFoodObjectItems.
        :type diet_labels: BrandedFoodObjectDietLabels
        """

        self._diet_labels = diet_labels

    @property
    def diet_flags(self) -> List[BrandedFoodObjectDietFlags]:
        """Gets the diet_flags of this BrandedFoodObjectItems.

        An array of ingredient objects that were flagged while grading this item for compatibility with each diet  # noqa: E501

        :return: The diet_flags of this BrandedFoodObjectItems.
        :rtype: List[BrandedFoodObjectDietFlags]
        """
        return self._diet_flags

    @diet_flags.setter
    def diet_flags(self, diet_flags: List[BrandedFoodObjectDietFlags]):
        """Sets the diet_flags of this BrandedFoodObjectItems.

        An array of ingredient objects that were flagged while grading this item for compatibility with each diet  # noqa: E501

        :param diet_flags: The diet_flags of this BrandedFoodObjectItems.
        :type diet_flags: List[BrandedFoodObjectDietFlags]
        """

        self._diet_flags = diet_flags

    @property
    def packaging_photos(self) -> BrandedFoodObjectPackagingPhotos:
        """Gets the packaging_photos of this BrandedFoodObjectItems.


        :return: The packaging_photos of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectPackagingPhotos
        """
        return self._packaging_photos

    @packaging_photos.setter
    def packaging_photos(self, packaging_photos: BrandedFoodObjectPackagingPhotos):
        """Sets the packaging_photos of this BrandedFoodObjectItems.


        :param packaging_photos: The packaging_photos of this BrandedFoodObjectItems.
        :type packaging_photos: BrandedFoodObjectPackagingPhotos
        """

        self._packaging_photos = packaging_photos

    @property
    def components(self) -> List[BrandedFoodObjectComponents]:
        """Gets the components of this BrandedFoodObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :return: The components of this BrandedFoodObjectItems.
        :rtype: List[BrandedFoodObjectComponents]
        """
        return self._components

    @components.setter
    def components(self, components: List[BrandedFoodObjectComponents]):
        """Sets the components of this BrandedFoodObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :param components: The components of this BrandedFoodObjectItems.
        :type components: List[BrandedFoodObjectComponents]
        """

        self._components = components

    @property
    def portions(self) -> List[BrandedFoodObjectPortions]:
        """Gets the portions of this BrandedFoodObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :return: The portions of this BrandedFoodObjectItems.
        :rtype: List[BrandedFoodObjectPortions]
        """
        return self._portions

    @portions.setter
    def portions(self, portions: List[BrandedFoodObjectPortions]):
        """Sets the portions of this BrandedFoodObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :param portions: The portions of this BrandedFoodObjectItems.
        :type portions: List[BrandedFoodObjectPortions]
        """

        self._portions = portions

    @property
    def allergens(self) -> List[str]:
        """Gets the allergens of this BrandedFoodObjectItems.

        An array of ingredients in this item that may cause allergic reactions in people  # noqa: E501

        :return: The allergens of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._allergens

    @allergens.setter
    def allergens(self, allergens: List[str]):
        """Sets the allergens of this BrandedFoodObjectItems.

        An array of ingredients in this item that may cause allergic reactions in people  # noqa: E501

        :param allergens: The allergens of this BrandedFoodObjectItems.
        :type allergens: List[str]
        """

        self._allergens = allergens

    @property
    def brand_list(self) -> List[str]:
        """Gets the brand_list of this BrandedFoodObjectItems.

        An array of brands we have associated with this item. Some items are sold by more than 1 brand.  # noqa: E501

        :return: The brand_list of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._brand_list

    @brand_list.setter
    def brand_list(self, brand_list: List[str]):
        """Sets the brand_list of this BrandedFoodObjectItems.

        An array of brands we have associated with this item. Some items are sold by more than 1 brand.  # noqa: E501

        :param brand_list: The brand_list of this BrandedFoodObjectItems.
        :type brand_list: List[str]
        """

        self._brand_list = brand_list

    @property
    def countries(self) -> List[str]:
        """Gets the countries of this BrandedFoodObjectItems.

        An array of countries where this item is sold  # noqa: E501

        :return: The countries of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries: List[str]):
        """Sets the countries of this BrandedFoodObjectItems.

        An array of countries where this item is sold  # noqa: E501

        :param countries: The countries of this BrandedFoodObjectItems.
        :type countries: List[str]
        """

        self._countries = countries

    @property
    def country_details(self) -> BrandedFoodObjectCountryDetails:
        """Gets the country_details of this BrandedFoodObjectItems.


        :return: The country_details of this BrandedFoodObjectItems.
        :rtype: BrandedFoodObjectCountryDetails
        """
        return self._country_details

    @country_details.setter
    def country_details(self, country_details: BrandedFoodObjectCountryDetails):
        """Sets the country_details of this BrandedFoodObjectItems.


        :param country_details: The country_details of this BrandedFoodObjectItems.
        :type country_details: BrandedFoodObjectCountryDetails
        """

        self._country_details = country_details

    @property
    def palm_oil_ingredients(self) -> List[str]:
        """Gets the palm_oil_ingredients of this BrandedFoodObjectItems.

        An array of ingredients made from palm oil  # noqa: E501

        :return: The palm_oil_ingredients of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._palm_oil_ingredients

    @palm_oil_ingredients.setter
    def palm_oil_ingredients(self, palm_oil_ingredients: List[str]):
        """Sets the palm_oil_ingredients of this BrandedFoodObjectItems.

        An array of ingredients made from palm oil  # noqa: E501

        :param palm_oil_ingredients: The palm_oil_ingredients of this BrandedFoodObjectItems.
        :type palm_oil_ingredients: List[str]
        """

        self._palm_oil_ingredients = palm_oil_ingredients

    @property
    def ingredient_list(self) -> List[str]:
        """Gets the ingredient_list of this BrandedFoodObjectItems.

        An array of this item's ingredients  # noqa: E501

        :return: The ingredient_list of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._ingredient_list

    @ingredient_list.setter
    def ingredient_list(self, ingredient_list: List[str]):
        """Sets the ingredient_list of this BrandedFoodObjectItems.

        An array of this item's ingredients  # noqa: E501

        :param ingredient_list: The ingredient_list of this BrandedFoodObjectItems.
        :type ingredient_list: List[str]
        """

        self._ingredient_list = ingredient_list

    @property
    def has_english_ingredients(self) -> bool:
        """Gets the has_english_ingredients of this BrandedFoodObjectItems.

        A boolean indicating if we have English ingredients for this item  # noqa: E501

        :return: The has_english_ingredients of this BrandedFoodObjectItems.
        :rtype: bool
        """
        return self._has_english_ingredients

    @has_english_ingredients.setter
    def has_english_ingredients(self, has_english_ingredients: bool):
        """Sets the has_english_ingredients of this BrandedFoodObjectItems.

        A boolean indicating if we have English ingredients for this item  # noqa: E501

        :param has_english_ingredients: The has_english_ingredients of this BrandedFoodObjectItems.
        :type has_english_ingredients: bool
        """

        self._has_english_ingredients = has_english_ingredients

    @property
    def minerals(self) -> List[str]:
        """Gets the minerals of this BrandedFoodObjectItems.

        An array of minerals that this item contains  # noqa: E501

        :return: The minerals of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._minerals

    @minerals.setter
    def minerals(self, minerals: List[str]):
        """Sets the minerals of this BrandedFoodObjectItems.

        An array of minerals that this item contains  # noqa: E501

        :param minerals: The minerals of this BrandedFoodObjectItems.
        :type minerals: List[str]
        """

        self._minerals = minerals

    @property
    def traces(self) -> List[str]:
        """Gets the traces of this BrandedFoodObjectItems.

        An array of trace ingredients that may be found in this item  # noqa: E501

        :return: The traces of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._traces

    @traces.setter
    def traces(self, traces: List[str]):
        """Sets the traces of this BrandedFoodObjectItems.

        An array of trace ingredients that may be found in this item  # noqa: E501

        :param traces: The traces of this BrandedFoodObjectItems.
        :type traces: List[str]
        """

        self._traces = traces

    @property
    def vitamins(self) -> List[str]:
        """Gets the vitamins of this BrandedFoodObjectItems.

        An array of vitamins that are found in this item  # noqa: E501

        :return: The vitamins of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._vitamins

    @vitamins.setter
    def vitamins(self, vitamins: List[str]):
        """Sets the vitamins of this BrandedFoodObjectItems.

        An array of vitamins that are found in this item  # noqa: E501

        :param vitamins: The vitamins of this BrandedFoodObjectItems.
        :type vitamins: List[str]
        """

        self._vitamins = vitamins

    @property
    def common_names(self) -> List[str]:
        """Gets the common_names of this BrandedFoodObjectItems.

        An array containing other names commonly associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" a common name may be \"Chicken enchilada\")  # noqa: E501

        :return: The common_names of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._common_names

    @common_names.setter
    def common_names(self, common_names: List[str]):
        """Sets the common_names of this BrandedFoodObjectItems.

        An array containing other names commonly associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" a common name may be \"Chicken enchilada\")  # noqa: E501

        :param common_names: The common_names of this BrandedFoodObjectItems.
        :type common_names: List[str]
        """

        self._common_names = common_names

    @property
    def description(self) -> str:
        """Gets the description of this BrandedFoodObjectItems.

        A description of this item  # noqa: E501

        :return: The description of this BrandedFoodObjectItems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this BrandedFoodObjectItems.

        A description of this item  # noqa: E501

        :param description: The description of this BrandedFoodObjectItems.
        :type description: str
        """

        self._description = description

    @property
    def keywords(self) -> List[str]:
        """Gets the keywords of this BrandedFoodObjectItems.

        An array of keywords that can be used to describe this item  # noqa: E501

        :return: The keywords of this BrandedFoodObjectItems.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: List[str]):
        """Sets the keywords of this BrandedFoodObjectItems.

        An array of keywords that can be used to describe this item  # noqa: E501

        :param keywords: The keywords of this BrandedFoodObjectItems.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def footnote(self) -> str:
        """Gets the footnote of this BrandedFoodObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :return: The footnote of this BrandedFoodObjectItems.
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote: str):
        """Sets the footnote of this BrandedFoodObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :param footnote: The footnote of this BrandedFoodObjectItems.
        :type footnote: str
        """

        self._footnote = footnote
