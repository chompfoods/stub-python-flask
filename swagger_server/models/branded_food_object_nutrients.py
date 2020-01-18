# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.branded_food_object_nutrients_chomp import BrandedFoodObjectNutrientsChomp  # noqa: F401,E501
from swagger_server.models.branded_food_object_nutrients_usda import BrandedFoodObjectNutrientsUsda  # noqa: F401,E501
from swagger_server import util


class BrandedFoodObjectNutrients(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, chomp: List[BrandedFoodObjectNutrientsChomp]=None, usda: List[BrandedFoodObjectNutrientsUsda]=None):  # noqa: E501
        """BrandedFoodObjectNutrients - a model defined in Swagger

        :param chomp: The chomp of this BrandedFoodObjectNutrients.  # noqa: E501
        :type chomp: List[BrandedFoodObjectNutrientsChomp]
        :param usda: The usda of this BrandedFoodObjectNutrients.  # noqa: E501
        :type usda: List[BrandedFoodObjectNutrientsUsda]
        """
        self.swagger_types = {
            'chomp': List[BrandedFoodObjectNutrientsChomp],
            'usda': List[BrandedFoodObjectNutrientsUsda]
        }

        self.attribute_map = {
            'chomp': 'chomp',
            'usda': 'usda'
        }
        self._chomp = chomp
        self._usda = usda

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObjectNutrients':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject_nutrients of this BrandedFoodObjectNutrients.  # noqa: E501
        :rtype: BrandedFoodObjectNutrients
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chomp(self) -> List[BrandedFoodObjectNutrientsChomp]:
        """Gets the chomp of this BrandedFoodObjectNutrients.

        An array containing an object for each nutrient data point  # noqa: E501

        :return: The chomp of this BrandedFoodObjectNutrients.
        :rtype: List[BrandedFoodObjectNutrientsChomp]
        """
        return self._chomp

    @chomp.setter
    def chomp(self, chomp: List[BrandedFoodObjectNutrientsChomp]):
        """Sets the chomp of this BrandedFoodObjectNutrients.

        An array containing an object for each nutrient data point  # noqa: E501

        :param chomp: The chomp of this BrandedFoodObjectNutrients.
        :type chomp: List[BrandedFoodObjectNutrientsChomp]
        """

        self._chomp = chomp

    @property
    def usda(self) -> List[BrandedFoodObjectNutrientsUsda]:
        """Gets the usda of this BrandedFoodObjectNutrients.

        An array containing an object for each nutrient data point as found in the USDA database  # noqa: E501

        :return: The usda of this BrandedFoodObjectNutrients.
        :rtype: List[BrandedFoodObjectNutrientsUsda]
        """
        return self._usda

    @usda.setter
    def usda(self, usda: List[BrandedFoodObjectNutrientsUsda]):
        """Sets the usda of this BrandedFoodObjectNutrients.

        An array containing an object for each nutrient data point as found in the USDA database  # noqa: E501

        :param usda: The usda of this BrandedFoodObjectNutrients.
        :type usda: List[BrandedFoodObjectNutrientsUsda]
        """

        self._usda = usda