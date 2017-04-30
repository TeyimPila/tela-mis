# [Created by SkaeX @ 2016-02-22 16:18:15] 
# -*- coding: utf-8 -*-
from django.utils.translation import activate
from django.test import TestCase
from django.core.urlresolvers import reverse
 
 
class TestHomePage(TestCase):
 
    def test_uses_index_template(self):
    	activate('en')
    	response = self.client.get(reverse("home"))
    	self.assertTemplateUsed(response, "TelaMIS/index.html")
 
    def test_uses_base_template(self):
    	activate('en')
    	response = self.client.get(reverse("home"))
    	self.assertTemplateUsed(response, "base.html")