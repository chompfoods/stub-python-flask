# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.branded_food_object_items import BrandedFoodObjectItems  # noqa: F401,E501
from swagger_server import util


class BrandedFoodObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, items: List[BrandedFoodObjectItems]=None):  # noqa: E501
        """BrandedFoodObject - a model defined in Swagger

        :param items: The items of this BrandedFoodObject.  # noqa: E501
        :type items: List[BrandedFoodObjectItems]
        """
        self.swagger_types = {
            'items': List[BrandedFoodObjectItems]
        }

        self.attribute_map = {
            'items': 'items'
        }
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject of this BrandedFoodObject.  # noqa: E501
        :rtype: BrandedFoodObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[BrandedFoodObjectItems]:
        """Gets the items of this BrandedFoodObject.

        An array containing an object for each individual item returned by your API call.  # noqa: E501

        :return: The items of this BrandedFoodObject.
        :rtype: List[BrandedFoodObjectItems]
        """
        return self._items

    @items.setter
    def items(self, items: List[BrandedFoodObjectItems]):
        """Sets the items of this BrandedFoodObject.

        An array containing an object for each individual item returned by your API call.  # noqa: E501

        :param items: The items of this BrandedFoodObject.
        :type items: List[BrandedFoodObjectItems]
        """

        self._items = items