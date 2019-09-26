# -*- coding: utf-8 -*-
import unittest
import deeple.models.deepaas_api as deepaas_api

class TestModelMethods(unittest.TestCase):
    
    def setUp(self):
        self.meta = deepaas_api.get_metadata()
        
    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)
        
    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['Name'].replace('-','').replace('_',''),
                        'deeple'.replace('-','').replace('_',''))
        self.assertEqual(self.meta['Author'], 'Your name (or your organization/company/team)')
        self.assertEqual(self.meta['Author-email'], 'luis.franco@usc.es')


if __name__ == '__main__':
    unittest.main()
