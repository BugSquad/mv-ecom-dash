from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate

# Create your tests here.

class TestTemp(TestCase):

    def test_temp_uses_index_template(self):
        activate("en")
        response = self.client.get(reverse("dashboard"))
        self.assertTemplateUsed(response, "dashboard/mv_admin_dashboard.html")