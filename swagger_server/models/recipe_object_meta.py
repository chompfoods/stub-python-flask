# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.recipe_object_meta_images import RecipeObjectMetaImages  # noqa: F401,E501
from swagger_server import util


class RecipeObjectMeta(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, url: str=None, images: RecipeObjectMetaImages=None, source: str=None, cuisine: str=None, created: str=None, modified: str=None, nutrients_notice: str=None):  # noqa: E501
        """RecipeObjectMeta - a model defined in Swagger

        :param url: The url of this RecipeObjectMeta.  # noqa: E501
        :type url: str
        :param images: The images of this RecipeObjectMeta.  # noqa: E501
        :type images: RecipeObjectMetaImages
        :param source: The source of this RecipeObjectMeta.  # noqa: E501
        :type source: str
        :param cuisine: The cuisine of this RecipeObjectMeta.  # noqa: E501
        :type cuisine: str
        :param created: The created of this RecipeObjectMeta.  # noqa: E501
        :type created: str
        :param modified: The modified of this RecipeObjectMeta.  # noqa: E501
        :type modified: str
        :param nutrients_notice: The nutrients_notice of this RecipeObjectMeta.  # noqa: E501
        :type nutrients_notice: str
        """
        self.swagger_types = {
            'url': str,
            'images': RecipeObjectMetaImages,
            'source': str,
            'cuisine': str,
            'created': str,
            'modified': str,
            'nutrients_notice': str
        }

        self.attribute_map = {
            'url': 'url',
            'images': 'images',
            'source': 'source',
            'cuisine': 'cuisine',
            'created': 'created',
            'modified': 'modified',
            'nutrients_notice': 'nutrients_notice'
        }
        self._url = url
        self._images = images
        self._source = source
        self._cuisine = cuisine
        self._created = created
        self._modified = modified
        self._nutrients_notice = nutrients_notice

    @classmethod
    def from_dict(cls, dikt) -> 'RecipeObjectMeta':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RecipeObject_meta of this RecipeObjectMeta.  # noqa: E501
        :rtype: RecipeObjectMeta
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this RecipeObjectMeta.

        URL to the recipe. You must link back to the recipe when displaying it.  # noqa: E501

        :return: The url of this RecipeObjectMeta.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this RecipeObjectMeta.

        URL to the recipe. You must link back to the recipe when displaying it.  # noqa: E501

        :param url: The url of this RecipeObjectMeta.
        :type url: str
        """

        self._url = url

    @property
    def images(self) -> RecipeObjectMetaImages:
        """Gets the images of this RecipeObjectMeta.


        :return: The images of this RecipeObjectMeta.
        :rtype: RecipeObjectMetaImages
        """
        return self._images

    @images.setter
    def images(self, images: RecipeObjectMetaImages):
        """Sets the images of this RecipeObjectMeta.


        :param images: The images of this RecipeObjectMeta.
        :type images: RecipeObjectMetaImages
        """

        self._images = images

    @property
    def source(self) -> str:
        """Gets the source of this RecipeObjectMeta.

        The source of the recipe. You must attribute this source when displaying this recipe.  # noqa: E501

        :return: The source of this RecipeObjectMeta.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this RecipeObjectMeta.

        The source of the recipe. You must attribute this source when displaying this recipe.  # noqa: E501

        :param source: The source of this RecipeObjectMeta.
        :type source: str
        """

        self._source = source

    @property
    def cuisine(self) -> str:
        """Gets the cuisine of this RecipeObjectMeta.

        This recipe's cuisine  # noqa: E501

        :return: The cuisine of this RecipeObjectMeta.
        :rtype: str
        """
        return self._cuisine

    @cuisine.setter
    def cuisine(self, cuisine: str):
        """Sets the cuisine of this RecipeObjectMeta.

        This recipe's cuisine  # noqa: E501

        :param cuisine: The cuisine of this RecipeObjectMeta.
        :type cuisine: str
        """

        self._cuisine = cuisine

    @property
    def created(self) -> str:
        """Gets the created of this RecipeObjectMeta.

        The date when this recipe was created  # noqa: E501

        :return: The created of this RecipeObjectMeta.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created: str):
        """Sets the created of this RecipeObjectMeta.

        The date when this recipe was created  # noqa: E501

        :param created: The created of this RecipeObjectMeta.
        :type created: str
        """

        self._created = created

    @property
    def modified(self) -> str:
        """Gets the modified of this RecipeObjectMeta.

        The date when this recipe was most recently modified  # noqa: E501

        :return: The modified of this RecipeObjectMeta.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified: str):
        """Sets the modified of this RecipeObjectMeta.

        The date when this recipe was most recently modified  # noqa: E501

        :param modified: The modified of this RecipeObjectMeta.
        :type modified: str
        """

        self._modified = modified

    @property
    def nutrients_notice(self) -> str:
        """Gets the nutrients_notice of this RecipeObjectMeta.

        Additional information about this recipe's nutrients  # noqa: E501

        :return: The nutrients_notice of this RecipeObjectMeta.
        :rtype: str
        """
        return self._nutrients_notice

    @nutrients_notice.setter
    def nutrients_notice(self, nutrients_notice: str):
        """Sets the nutrients_notice of this RecipeObjectMeta.

        Additional information about this recipe's nutrients  # noqa: E501

        :param nutrients_notice: The nutrients_notice of this RecipeObjectMeta.
        :type nutrients_notice: str
        """

        self._nutrients_notice = nutrients_notice
