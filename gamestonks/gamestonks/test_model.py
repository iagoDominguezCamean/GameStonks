from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your tests here.
"""
class TestStatusOkIndex(TestCase):
    pass
"""


class TestUser(TestCase):
    def test_auth_fail(self):

        uname = "iagodc"
        passwd = "@Iagodc29"
        user = authenticate(username=uname, password=passwd)

        self.assertIsNone(user)

    def test_auth_suc(self):

        uname = "iagodc"
        passwd = "@Iagodc29"

        user = User.objects.create(username=uname)
        user.set_password(passwd)
        user.save()

        user = authenticate(username=uname, password=passwd)

        self.assertIsNotNone(user)
