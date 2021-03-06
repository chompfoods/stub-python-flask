# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BrandedFoodObjectPackagingPhotosNutrition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, small: str=None, thumb: str=None, display: str=None):  # noqa: E501
        """BrandedFoodObjectPackagingPhotosNutrition - a model defined in Swagger

        :param small: The small of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type small: str
        :param thumb: The thumb of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type thumb: str
        :param display: The display of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type display: str
        """
        self.swagger_types = {
            'small': str,
            'thumb': str,
            'display': str
        }

        self.attribute_map = {
            'small': 'small',
            'thumb': 'thumb',
            'display': 'display'
        }
        self._small = small
        self._thumb = thumb
        self._display = display

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObjectPackagingPhotosNutrition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject_packaging_photos_nutrition of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotosNutrition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def small(self) -> str:
        """Gets the small of this BrandedFoodObjectPackagingPhotosNutrition.

        Small photo of this item's nutrition label  # noqa: E501

        :return: The small of this BrandedFoodObjectPackagingPhotosNutrition.
        :rtype: str
        """
        return self._small

    @small.setter
    def small(self, small: str):
        """Sets the small of this BrandedFoodObjectPackagingPhotosNutrition.

        Small photo of this item's nutrition label  # noqa: E501

        :param small: The small of this BrandedFoodObjectPackagingPhotosNutrition.
        :type small: str
        """

        self._small = small

    @property
    def thumb(self) -> str:
        """Gets the thumb of this BrandedFoodObjectPackagingPhotosNutrition.

        Thumbnail photo of this item's nutrition label  # noqa: E501

        :return: The thumb of this BrandedFoodObjectPackagingPhotosNutrition.
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb: str):
        """Sets the thumb of this BrandedFoodObjectPackagingPhotosNutrition.

        Thumbnail photo of this item's nutrition label  # noqa: E501

        :param thumb: The thumb of this BrandedFoodObjectPackagingPhotosNutrition.
        :type thumb: str
        """

        self._thumb = thumb

    @property
    def display(self) -> str:
        """Gets the display of this BrandedFoodObjectPackagingPhotosNutrition.

        Full-sized photo of this item's nutrition label  # noqa: E501

        :return: The display of this BrandedFoodObjectPackagingPhotosNutrition.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display: str):
        """Sets the display of this BrandedFoodObjectPackagingPhotosNutrition.

        Full-sized photo of this item's nutrition label  # noqa: E501

        :param display: The display of this BrandedFoodObjectPackagingPhotosNutrition.
        :type display: str
        """

        self._display = display
