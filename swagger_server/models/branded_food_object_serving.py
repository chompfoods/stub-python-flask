# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BrandedFoodObjectServing(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, size: int=None, measurement_unit: str=None, size_fulltext: str=None, total: int=None):  # noqa: E501
        """BrandedFoodObjectServing - a model defined in Swagger

        :param size: The size of this BrandedFoodObjectServing.  # noqa: E501
        :type size: int
        :param measurement_unit: The measurement_unit of this BrandedFoodObjectServing.  # noqa: E501
        :type measurement_unit: str
        :param size_fulltext: The size_fulltext of this BrandedFoodObjectServing.  # noqa: E501
        :type size_fulltext: str
        :param total: The total of this BrandedFoodObjectServing.  # noqa: E501
        :type total: int
        """
        self.swagger_types = {
            'size': int,
            'measurement_unit': str,
            'size_fulltext': str,
            'total': int
        }

        self.attribute_map = {
            'size': 'size',
            'measurement_unit': 'measurement_unit',
            'size_fulltext': 'size_fulltext',
            'total': 'total'
        }
        self._size = size
        self._measurement_unit = measurement_unit
        self._size_fulltext = size_fulltext
        self._total = total

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObjectServing':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject_serving of this BrandedFoodObjectServing.  # noqa: E501
        :rtype: BrandedFoodObjectServing
        """
        return util.deserialize_model(dikt, cls)

    @property
    def size(self) -> int:
        """Gets the size of this BrandedFoodObjectServing.

        Serving size  # noqa: E501

        :return: The size of this BrandedFoodObjectServing.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this BrandedFoodObjectServing.

        Serving size  # noqa: E501

        :param size: The size of this BrandedFoodObjectServing.
        :type size: int
        """

        self._size = size

    @property
    def measurement_unit(self) -> str:
        """Gets the measurement_unit of this BrandedFoodObjectServing.

        Serving measurement unit (e.g. if measure is 3 tsp, the unit is tsp)  # noqa: E501

        :return: The measurement_unit of this BrandedFoodObjectServing.
        :rtype: str
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit: str):
        """Sets the measurement_unit of this BrandedFoodObjectServing.

        Serving measurement unit (e.g. if measure is 3 tsp, the unit is tsp)  # noqa: E501

        :param measurement_unit: The measurement_unit of this BrandedFoodObjectServing.
        :type measurement_unit: str
        """

        self._measurement_unit = measurement_unit

    @property
    def size_fulltext(self) -> str:
        """Gets the size_fulltext of this BrandedFoodObjectServing.

        Serving size description  # noqa: E501

        :return: The size_fulltext of this BrandedFoodObjectServing.
        :rtype: str
        """
        return self._size_fulltext

    @size_fulltext.setter
    def size_fulltext(self, size_fulltext: str):
        """Sets the size_fulltext of this BrandedFoodObjectServing.

        Serving size description  # noqa: E501

        :param size_fulltext: The size_fulltext of this BrandedFoodObjectServing.
        :type size_fulltext: str
        """

        self._size_fulltext = size_fulltext

    @property
    def total(self) -> int:
        """Gets the total of this BrandedFoodObjectServing.

        Total servings  # noqa: E501

        :return: The total of this BrandedFoodObjectServing.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this BrandedFoodObjectServing.

        Total servings  # noqa: E501

        :param total: The total of this BrandedFoodObjectServing.
        :type total: int
        """

        self._total = total
