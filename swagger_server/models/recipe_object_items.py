# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.recipe_object_attributes import RecipeObjectAttributes  # noqa: F401,E501
from swagger_server.models.recipe_object_ingredients import RecipeObjectIngredients  # noqa: F401,E501
from swagger_server.models.recipe_object_meta import RecipeObjectMeta  # noqa: F401,E501
from swagger_server.models.recipe_object_nutrients import RecipeObjectNutrients  # noqa: F401,E501
from swagger_server import util


class RecipeObjectItems(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, meta: RecipeObjectMeta=None, categories: List[str]=None, author: str=None, keywords: List[str]=None, topics: List[str]=None, attributes: RecipeObjectAttributes=None, ingredients: List[RecipeObjectIngredients]=None, base_ingredients: List[str]=None, nutrients: RecipeObjectNutrients=None, diabetic_exchanges: List[str]=None):  # noqa: E501
        """RecipeObjectItems - a model defined in Swagger

        :param id: The id of this RecipeObjectItems.  # noqa: E501
        :type id: str
        :param title: The title of this RecipeObjectItems.  # noqa: E501
        :type title: str
        :param meta: The meta of this RecipeObjectItems.  # noqa: E501
        :type meta: RecipeObjectMeta
        :param categories: The categories of this RecipeObjectItems.  # noqa: E501
        :type categories: List[str]
        :param author: The author of this RecipeObjectItems.  # noqa: E501
        :type author: str
        :param keywords: The keywords of this RecipeObjectItems.  # noqa: E501
        :type keywords: List[str]
        :param topics: The topics of this RecipeObjectItems.  # noqa: E501
        :type topics: List[str]
        :param attributes: The attributes of this RecipeObjectItems.  # noqa: E501
        :type attributes: RecipeObjectAttributes
        :param ingredients: The ingredients of this RecipeObjectItems.  # noqa: E501
        :type ingredients: List[RecipeObjectIngredients]
        :param base_ingredients: The base_ingredients of this RecipeObjectItems.  # noqa: E501
        :type base_ingredients: List[str]
        :param nutrients: The nutrients of this RecipeObjectItems.  # noqa: E501
        :type nutrients: RecipeObjectNutrients
        :param diabetic_exchanges: The diabetic_exchanges of this RecipeObjectItems.  # noqa: E501
        :type diabetic_exchanges: List[str]
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'meta': RecipeObjectMeta,
            'categories': List[str],
            'author': str,
            'keywords': List[str],
            'topics': List[str],
            'attributes': RecipeObjectAttributes,
            'ingredients': List[RecipeObjectIngredients],
            'base_ingredients': List[str],
            'nutrients': RecipeObjectNutrients,
            'diabetic_exchanges': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'meta': 'meta',
            'categories': 'categories',
            'author': 'author',
            'keywords': 'keywords',
            'topics': 'topics',
            'attributes': 'attributes',
            'ingredients': 'ingredients',
            'base_ingredients': 'base_ingredients',
            'nutrients': 'nutrients',
            'diabetic_exchanges': 'diabetic_exchanges'
        }
        self._id = id
        self._title = title
        self._meta = meta
        self._categories = categories
        self._author = author
        self._keywords = keywords
        self._topics = topics
        self._attributes = attributes
        self._ingredients = ingredients
        self._base_ingredients = base_ingredients
        self._nutrients = nutrients
        self._diabetic_exchanges = diabetic_exchanges

    @classmethod
    def from_dict(cls, dikt) -> 'RecipeObjectItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RecipeObject_items of this RecipeObjectItems.  # noqa: E501
        :rtype: RecipeObjectItems
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this RecipeObjectItems.

        Unique recipe ID  # noqa: E501

        :return: The id of this RecipeObjectItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this RecipeObjectItems.

        Unique recipe ID  # noqa: E501

        :param id: The id of this RecipeObjectItems.
        :type id: str
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this RecipeObjectItems.

        Recipe title  # noqa: E501

        :return: The title of this RecipeObjectItems.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this RecipeObjectItems.

        Recipe title  # noqa: E501

        :param title: The title of this RecipeObjectItems.
        :type title: str
        """

        self._title = title

    @property
    def meta(self) -> RecipeObjectMeta:
        """Gets the meta of this RecipeObjectItems.


        :return: The meta of this RecipeObjectItems.
        :rtype: RecipeObjectMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: RecipeObjectMeta):
        """Sets the meta of this RecipeObjectItems.


        :param meta: The meta of this RecipeObjectItems.
        :type meta: RecipeObjectMeta
        """

        self._meta = meta

    @property
    def categories(self) -> List[str]:
        """Gets the categories of this RecipeObjectItems.


        :return: The categories of this RecipeObjectItems.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]):
        """Sets the categories of this RecipeObjectItems.


        :param categories: The categories of this RecipeObjectItems.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def author(self) -> str:
        """Gets the author of this RecipeObjectItems.

        The author of this recipe. You must attribute this author when displaying this recipe.  # noqa: E501

        :return: The author of this RecipeObjectItems.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this RecipeObjectItems.

        The author of this recipe. You must attribute this author when displaying this recipe.  # noqa: E501

        :param author: The author of this RecipeObjectItems.
        :type author: str
        """

        self._author = author

    @property
    def keywords(self) -> List[str]:
        """Gets the keywords of this RecipeObjectItems.


        :return: The keywords of this RecipeObjectItems.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: List[str]):
        """Sets the keywords of this RecipeObjectItems.


        :param keywords: The keywords of this RecipeObjectItems.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def topics(self) -> List[str]:
        """Gets the topics of this RecipeObjectItems.


        :return: The topics of this RecipeObjectItems.
        :rtype: List[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics: List[str]):
        """Sets the topics of this RecipeObjectItems.


        :param topics: The topics of this RecipeObjectItems.
        :type topics: List[str]
        """

        self._topics = topics

    @property
    def attributes(self) -> RecipeObjectAttributes:
        """Gets the attributes of this RecipeObjectItems.


        :return: The attributes of this RecipeObjectItems.
        :rtype: RecipeObjectAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: RecipeObjectAttributes):
        """Sets the attributes of this RecipeObjectItems.


        :param attributes: The attributes of this RecipeObjectItems.
        :type attributes: RecipeObjectAttributes
        """

        self._attributes = attributes

    @property
    def ingredients(self) -> List[RecipeObjectIngredients]:
        """Gets the ingredients of this RecipeObjectItems.

        An array containing this recipe's ingredients  # noqa: E501

        :return: The ingredients of this RecipeObjectItems.
        :rtype: List[RecipeObjectIngredients]
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: List[RecipeObjectIngredients]):
        """Sets the ingredients of this RecipeObjectItems.

        An array containing this recipe's ingredients  # noqa: E501

        :param ingredients: The ingredients of this RecipeObjectItems.
        :type ingredients: List[RecipeObjectIngredients]
        """

        self._ingredients = ingredients

    @property
    def base_ingredients(self) -> List[str]:
        """Gets the base_ingredients of this RecipeObjectItems.


        :return: The base_ingredients of this RecipeObjectItems.
        :rtype: List[str]
        """
        return self._base_ingredients

    @base_ingredients.setter
    def base_ingredients(self, base_ingredients: List[str]):
        """Sets the base_ingredients of this RecipeObjectItems.


        :param base_ingredients: The base_ingredients of this RecipeObjectItems.
        :type base_ingredients: List[str]
        """

        self._base_ingredients = base_ingredients

    @property
    def nutrients(self) -> RecipeObjectNutrients:
        """Gets the nutrients of this RecipeObjectItems.


        :return: The nutrients of this RecipeObjectItems.
        :rtype: RecipeObjectNutrients
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients: RecipeObjectNutrients):
        """Sets the nutrients of this RecipeObjectItems.


        :param nutrients: The nutrients of this RecipeObjectItems.
        :type nutrients: RecipeObjectNutrients
        """

        self._nutrients = nutrients

    @property
    def diabetic_exchanges(self) -> List[str]:
        """Gets the diabetic_exchanges of this RecipeObjectItems.


        :return: The diabetic_exchanges of this RecipeObjectItems.
        :rtype: List[str]
        """
        return self._diabetic_exchanges

    @diabetic_exchanges.setter
    def diabetic_exchanges(self, diabetic_exchanges: List[str]):
        """Sets the diabetic_exchanges of this RecipeObjectItems.


        :param diabetic_exchanges: The diabetic_exchanges of this RecipeObjectItems.
        :type diabetic_exchanges: List[str]
        """

        self._diabetic_exchanges = diabetic_exchanges
