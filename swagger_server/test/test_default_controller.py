# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.branded_food_object import BrandedFoodObject  # noqa: E501
from swagger_server.models.ingredient_object import IngredientObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_food_branded_barcode_php_get(self):
        """Test case for food_branded_barcode_php_get

        Get a branded food item using a barcode
        """
        query_string = [('code', 'code_example')]
        response = self.client.open(
            '/api/v2/food/branded/barcode.php',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_food_branded_id_php_get(self):
        """Test case for food_branded_id_php_get

        Get a branded food item using an ID number
        """
        query_string = [('id', 56),
                        ('source', 'source_example')]
        response = self.client.open(
            '/api/v2/food/branded/id.php',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_food_branded_name_php_get(self):
        """Test case for food_branded_name_php_get

        Get a branded food item by name
        """
        query_string = [('name', 'name_example'),
                        ('limit', 56)]
        response = self.client.open(
            '/api/v2/food/branded/name.php',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_food_branded_search_php_get(self):
        """Test case for food_branded_search_php_get

        Get data for branded food items using various search parameters
        """
        query_string = [('allergen', 'allergen_example'),
                        ('brand', 'brand_example'),
                        ('category', 'category_example'),
                        ('country', 'country_example'),
                        ('diet', 'diet_example'),
                        ('ingredient', 'ingredient_example'),
                        ('keyword', 'keyword_example'),
                        ('mineral', 'mineral_example'),
                        ('nutrient', 'nutrient_example'),
                        ('palm_oil', 'palm_oil_example'),
                        ('trace', 'trace_example'),
                        ('vitamin', 'vitamin_example'),
                        ('limit', 56),
                        ('page', 56)]
        response = self.client.open(
            '/api/v2/food/branded/search.php',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ingredient_search_php_get(self):
        """Test case for ingredient_search_php_get

        Get raw/generic food ingredient item(s)
        """
        query_string = [('find', 56),
                        ('list', true),
                        ('raw', true),
                        ('limit', 56)]
        response = self.client.open(
            '/api/v2/ingredient/search.php',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
