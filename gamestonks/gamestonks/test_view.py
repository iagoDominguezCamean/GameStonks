from http import client
import unittest
from django.test import Client, TestCase


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        #self.assertEqual(len(response.context['customers']), 5)

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_store(self):
        response = self.client.get('/store/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')

    def test_sBn(self):
        response = self.client.get('/sBn/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/sBn.html')

    def test_analisis(self):
        response = self.client.get('/analisis/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/analisis.html')

    def test_deals(self):
        response = self.client.get(
            '/deals/JgjbtVkgfWGW3AzYrPr6yyqxR2R1FZ3n4F9UrN2ZGJc%3D/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/deal.html')
