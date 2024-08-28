from django.test import TestCase
from store.forms import NewUser


class TestForm(TestCase):
    def test_form_valid_data(self):
        form = NewUser(data={
            'username': 'test123',
            'email': 'test123@gmail.com',
            'password1': '@Test14Y#',
            'password2': '@Test14Y#'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = NewUser(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
