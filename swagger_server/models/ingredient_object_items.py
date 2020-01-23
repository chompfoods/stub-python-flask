# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.branded_food_object_calorie_conversion_factor import BrandedFoodObjectCalorieConversionFactor  # noqa: F401,E501
from swagger_server.models.branded_food_object_diet_labels import BrandedFoodObjectDietLabels  # noqa: F401,E501
from swagger_server.models.ingredient_object_components import IngredientObjectComponents  # noqa: F401,E501
from swagger_server.models.ingredient_object_nutrients import IngredientObjectNutrients  # noqa: F401,E501
from swagger_server.models.ingredient_object_portions import IngredientObjectPortions  # noqa: F401,E501
from swagger_server import util


class IngredientObjectItems(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, categories: List[str]=None, nutrients: IngredientObjectNutrients=None, calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor=None, protein_conversion_factor: float=None, diet_labels: BrandedFoodObjectDietLabels=None, components: List[IngredientObjectComponents]=None, portions: List[IngredientObjectPortions]=None, common_names: str=None, description: str=None, footnote: str=None):  # noqa: E501
        """IngredientObjectItems - a model defined in Swagger

        :param name: The name of this IngredientObjectItems.  # noqa: E501
        :type name: str
        :param categories: The categories of this IngredientObjectItems.  # noqa: E501
        :type categories: List[str]
        :param nutrients: The nutrients of this IngredientObjectItems.  # noqa: E501
        :type nutrients: IngredientObjectNutrients
        :param calorie_conversion_factor: The calorie_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :type calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor
        :param protein_conversion_factor: The protein_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :type protein_conversion_factor: float
        :param diet_labels: The diet_labels of this IngredientObjectItems.  # noqa: E501
        :type diet_labels: BrandedFoodObjectDietLabels
        :param components: The components of this IngredientObjectItems.  # noqa: E501
        :type components: List[IngredientObjectComponents]
        :param portions: The portions of this IngredientObjectItems.  # noqa: E501
        :type portions: List[IngredientObjectPortions]
        :param common_names: The common_names of this IngredientObjectItems.  # noqa: E501
        :type common_names: str
        :param description: The description of this IngredientObjectItems.  # noqa: E501
        :type description: str
        :param footnote: The footnote of this IngredientObjectItems.  # noqa: E501
        :type footnote: str
        """
        self.swagger_types = {
            'name': str,
            'categories': List[str],
            'nutrients': IngredientObjectNutrients,
            'calorie_conversion_factor': BrandedFoodObjectCalorieConversionFactor,
            'protein_conversion_factor': float,
            'diet_labels': BrandedFoodObjectDietLabels,
            'components': List[IngredientObjectComponents],
            'portions': List[IngredientObjectPortions],
            'common_names': str,
            'description': str,
            'footnote': str
        }

        self.attribute_map = {
            'name': 'name',
            'categories': 'categories',
            'nutrients': 'nutrients',
            'calorie_conversion_factor': 'calorie_conversion_factor',
            'protein_conversion_factor': 'protein_conversion_factor',
            'diet_labels': 'diet_labels',
            'components': 'components',
            'portions': 'portions',
            'common_names': 'common_names',
            'description': 'description',
            'footnote': 'footnote'
        }
        self._name = name
        self._categories = categories
        self._nutrients = nutrients
        self._calorie_conversion_factor = calorie_conversion_factor
        self._protein_conversion_factor = protein_conversion_factor
        self._diet_labels = diet_labels
        self._components = components
        self._portions = portions
        self._common_names = common_names
        self._description = description
        self._footnote = footnote

    @classmethod
    def from_dict(cls, dikt) -> 'IngredientObjectItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IngredientObject_items of this IngredientObjectItems.  # noqa: E501
        :rtype: IngredientObjectItems
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this IngredientObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :return: The name of this IngredientObjectItems.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IngredientObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :param name: The name of this IngredientObjectItems.
        :type name: str
        """

        self._name = name

    @property
    def categories(self) -> List[str]:
        """Gets the categories of this IngredientObjectItems.


        :return: The categories of this IngredientObjectItems.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]):
        """Sets the categories of this IngredientObjectItems.


        :param categories: The categories of this IngredientObjectItems.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def nutrients(self) -> IngredientObjectNutrients:
        """Gets the nutrients of this IngredientObjectItems.


        :return: The nutrients of this IngredientObjectItems.
        :rtype: IngredientObjectNutrients
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients: IngredientObjectNutrients):
        """Sets the nutrients of this IngredientObjectItems.


        :param nutrients: The nutrients of this IngredientObjectItems.
        :type nutrients: IngredientObjectNutrients
        """

        self._nutrients = nutrients

    @property
    def calorie_conversion_factor(self) -> BrandedFoodObjectCalorieConversionFactor:
        """Gets the calorie_conversion_factor of this IngredientObjectItems.


        :return: The calorie_conversion_factor of this IngredientObjectItems.
        :rtype: BrandedFoodObjectCalorieConversionFactor
        """
        return self._calorie_conversion_factor

    @calorie_conversion_factor.setter
    def calorie_conversion_factor(self, calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor):
        """Sets the calorie_conversion_factor of this IngredientObjectItems.


        :param calorie_conversion_factor: The calorie_conversion_factor of this IngredientObjectItems.
        :type calorie_conversion_factor: BrandedFoodObjectCalorieConversionFactor
        """

        self._calorie_conversion_factor = calorie_conversion_factor

    @property
    def protein_conversion_factor(self) -> float:
        """Gets the protein_conversion_factor of this IngredientObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :return: The protein_conversion_factor of this IngredientObjectItems.
        :rtype: float
        """
        return self._protein_conversion_factor

    @protein_conversion_factor.setter
    def protein_conversion_factor(self, protein_conversion_factor: float):
        """Sets the protein_conversion_factor of this IngredientObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :param protein_conversion_factor: The protein_conversion_factor of this IngredientObjectItems.
        :type protein_conversion_factor: float
        """

        self._protein_conversion_factor = protein_conversion_factor

    @property
    def diet_labels(self) -> BrandedFoodObjectDietLabels:
        """Gets the diet_labels of this IngredientObjectItems.


        :return: The diet_labels of this IngredientObjectItems.
        :rtype: BrandedFoodObjectDietLabels
        """
        return self._diet_labels

    @diet_labels.setter
    def diet_labels(self, diet_labels: BrandedFoodObjectDietLabels):
        """Sets the diet_labels of this IngredientObjectItems.


        :param diet_labels: The diet_labels of this IngredientObjectItems.
        :type diet_labels: BrandedFoodObjectDietLabels
        """

        self._diet_labels = diet_labels

    @property
    def components(self) -> List[IngredientObjectComponents]:
        """Gets the components of this IngredientObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :return: The components of this IngredientObjectItems.
        :rtype: List[IngredientObjectComponents]
        """
        return self._components

    @components.setter
    def components(self, components: List[IngredientObjectComponents]):
        """Sets the components of this IngredientObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :param components: The components of this IngredientObjectItems.
        :type components: List[IngredientObjectComponents]
        """

        self._components = components

    @property
    def portions(self) -> List[IngredientObjectPortions]:
        """Gets the portions of this IngredientObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :return: The portions of this IngredientObjectItems.
        :rtype: List[IngredientObjectPortions]
        """
        return self._portions

    @portions.setter
    def portions(self, portions: List[IngredientObjectPortions]):
        """Sets the portions of this IngredientObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :param portions: The portions of this IngredientObjectItems.
        :type portions: List[IngredientObjectPortions]
        """

        self._portions = portions

    @property
    def common_names(self) -> str:
        """Gets the common_names of this IngredientObjectItems.

        Common names associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")  # noqa: E501

        :return: The common_names of this IngredientObjectItems.
        :rtype: str
        """
        return self._common_names

    @common_names.setter
    def common_names(self, common_names: str):
        """Sets the common_names of this IngredientObjectItems.

        Common names associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")  # noqa: E501

        :param common_names: The common_names of this IngredientObjectItems.
        :type common_names: str
        """

        self._common_names = common_names

    @property
    def description(self) -> str:
        """Gets the description of this IngredientObjectItems.

        A description of this item  # noqa: E501

        :return: The description of this IngredientObjectItems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this IngredientObjectItems.

        A description of this item  # noqa: E501

        :param description: The description of this IngredientObjectItems.
        :type description: str
        """

        self._description = description

    @property
    def footnote(self) -> str:
        """Gets the footnote of this IngredientObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :return: The footnote of this IngredientObjectItems.
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote: str):
        """Sets the footnote of this IngredientObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :param footnote: The footnote of this IngredientObjectItems.
        :type footnote: str
        """

        self._footnote = footnote
