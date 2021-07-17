from django.test import TestCase
from shop.forms import SearchForm


class SearchFormTest(TestCase):

    def test_form(self):

        data = {'query' : 'mohsen'}
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())
