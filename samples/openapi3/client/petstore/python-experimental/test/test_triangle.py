# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
try:
    from petstore_api.model import equilateral_triangle
except ImportError:
    equilateral_triangle = sys.modules[
        'petstore_api.model.equilateral_triangle']
try:
    from petstore_api.model import isosceles_triangle
except ImportError:
    isosceles_triangle = sys.modules[
        'petstore_api.model.isosceles_triangle']
try:
    from petstore_api.model import scalene_triangle
except ImportError:
    scalene_triangle = sys.modules[
        'petstore_api.model.scalene_triangle']
from petstore_api.model.triangle import Triangle


class TestTriangle(unittest.TestCase):
    """Triangle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTriangle(self):
        """Test Triangle"""
        tri = Triangle(shape_type="Triangle", triangle_type="EquilateralTriangle")
        assert isinstance(tri, equilateral_triangle.EquilateralTriangle)
        tri = Triangle(shape_type="Triangle", triangle_type="IsoscelesTriangle")
        assert isinstance(tri, isosceles_triangle.IsoscelesTriangle)
        tri = Triangle(shape_type="Triangle", triangle_type="ScaleneTriangle")
        assert isinstance(tri, scalene_triangle.ScaleneTriangle)


if __name__ == '__main__':
    unittest.main()
