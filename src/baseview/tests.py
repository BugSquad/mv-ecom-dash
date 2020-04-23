from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate

# Create your tests here.

def test_uses_index_template(self):
    activate('en')
    response = self.client.get(reverse("dashboard"))
    self.assertTemplateUsed(response, "dashboard/mv_admin_dashboard.html")

def test_internationalization(self):
    for lang, title_text in [('en', 'MV Ecom Admin Dashboard'),
                                ('ar', 'لوحة تحكم سوق متعدد المتاجر')]:
        activate(lang)
        self.browser.get(self.get_full_url("dashboard"))
        title = self.browser.find_element_by_tag_name("title")
        self.assertEqual(title.text, title_text)