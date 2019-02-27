from django.test import TestCase
from .tasks import get_hg_data
from .views import retroative_variation


class ViewTest(TestCase):

    def test_page_status(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_retroative_variation(self):
        days = 155
        currency = 'Yen'
        self.assertEquals(type(retroative_variation(days_before=days, currency_name=currency)),str)


class TaskTest(TestCase):

    def test_get_hg_data(self):
        self.assertEquals(type(get_hg_data()),dict)

