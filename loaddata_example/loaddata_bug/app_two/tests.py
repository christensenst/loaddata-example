from django.test import TestCase

from app_one.models import Office, Person
from app_two.models import Author, Book


class TestAppTwo(TestCase):
    fixtures = ['app_one_data', 'app_two_data']
    multi_db = True

    def test_lengths(self):
        self.assertEquals(len(Book.objects.all()), 2)
        self.assertEquals(len(Author.objects.all()), 2)
        self.assertEquals(len(Office.objects.all()), 2)
        self.assertEquals(len(Person.objects.all()), 2)
