# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.branded_food_object_packaging_photos_front import BrandedFoodObjectPackagingPhotosFront  # noqa: F401,E501
from swagger_server.models.branded_food_object_packaging_photos_ingredients import BrandedFoodObjectPackagingPhotosIngredients  # noqa: F401,E501
from swagger_server.models.branded_food_object_packaging_photos_nutrition import BrandedFoodObjectPackagingPhotosNutrition  # noqa: F401,E501
from swagger_server import util


class BrandedFoodObjectPackagingPhotos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, front: BrandedFoodObjectPackagingPhotosFront=None, nutrition: BrandedFoodObjectPackagingPhotosNutrition=None, ingredients: BrandedFoodObjectPackagingPhotosIngredients=None):  # noqa: E501
        """BrandedFoodObjectPackagingPhotos - a model defined in Swagger

        :param front: The front of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type front: BrandedFoodObjectPackagingPhotosFront
        :param nutrition: The nutrition of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type nutrition: BrandedFoodObjectPackagingPhotosNutrition
        :param ingredients: The ingredients of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type ingredients: BrandedFoodObjectPackagingPhotosIngredients
        """
        self.swagger_types = {
            'front': BrandedFoodObjectPackagingPhotosFront,
            'nutrition': BrandedFoodObjectPackagingPhotosNutrition,
            'ingredients': BrandedFoodObjectPackagingPhotosIngredients
        }

        self.attribute_map = {
            'front': 'front',
            'nutrition': 'nutrition',
            'ingredients': 'ingredients'
        }
        self._front = front
        self._nutrition = nutrition
        self._ingredients = ingredients

    @classmethod
    def from_dict(cls, dikt) -> 'BrandedFoodObjectPackagingPhotos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrandedFoodObject_packaging_photos of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def front(self) -> BrandedFoodObjectPackagingPhotosFront:
        """Gets the front of this BrandedFoodObjectPackagingPhotos.


        :return: The front of this BrandedFoodObjectPackagingPhotos.
        :rtype: BrandedFoodObjectPackagingPhotosFront
        """
        return self._front

    @front.setter
    def front(self, front: BrandedFoodObjectPackagingPhotosFront):
        """Sets the front of this BrandedFoodObjectPackagingPhotos.


        :param front: The front of this BrandedFoodObjectPackagingPhotos.
        :type front: BrandedFoodObjectPackagingPhotosFront
        """

        self._front = front

    @property
    def nutrition(self) -> BrandedFoodObjectPackagingPhotosNutrition:
        """Gets the nutrition of this BrandedFoodObjectPackagingPhotos.


        :return: The nutrition of this BrandedFoodObjectPackagingPhotos.
        :rtype: BrandedFoodObjectPackagingPhotosNutrition
        """
        return self._nutrition

    @nutrition.setter
    def nutrition(self, nutrition: BrandedFoodObjectPackagingPhotosNutrition):
        """Sets the nutrition of this BrandedFoodObjectPackagingPhotos.


        :param nutrition: The nutrition of this BrandedFoodObjectPackagingPhotos.
        :type nutrition: BrandedFoodObjectPackagingPhotosNutrition
        """

        self._nutrition = nutrition

    @property
    def ingredients(self) -> BrandedFoodObjectPackagingPhotosIngredients:
        """Gets the ingredients of this BrandedFoodObjectPackagingPhotos.


        :return: The ingredients of this BrandedFoodObjectPackagingPhotos.
        :rtype: BrandedFoodObjectPackagingPhotosIngredients
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: BrandedFoodObjectPackagingPhotosIngredients):
        """Sets the ingredients of this BrandedFoodObjectPackagingPhotos.


        :param ingredients: The ingredients of this BrandedFoodObjectPackagingPhotos.
        :type ingredients: BrandedFoodObjectPackagingPhotosIngredients
        """

        self._ingredients = ingredients
