from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

class BlogUrlsTest(TestCase):
    def test_blog_home_url(self):
        response = self.client.get(reverse("blog_home"))
        self.assertEqual(response.status_code, 200)

    def test_blog_about_url(self):
        response = self.client.get(reverse("blog_about"))
        self.assertEqual(response.status_code, 200)

    def test_blog_contact_url(self):
        response = self.client.get(reverse("blog_contact"))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_page_url(self):
        response = self.client.get(reverse("post_detail", args=[1]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_update_url(self):
        response = self.client.get(reverse("post_update", args=[1]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_delete_url(self):
        response = self.client.get(reverse("post_delete", args=[1]), follow=True)
        self.assertEqual(response.status_code, 200)
    

class BlogTemplatesTest(TestCase):
    def test_blog_home_url(self):
        response = self.client.get(reverse("blog_home"))
        templates = ['blog/base.html', 'blog/home.html']
        self.assertTemplateUsed(response, *templates)

    def test_blog_about_url(self):
        response = self.client.get(reverse("blog_about"))
        templates = ['blog/base.html', 'blog/about.html']
        self.assertTemplateUsed(response, *templates)

    def test_blog_contact_url(self):
        response = self.client.get(reverse("blog_contact"))
        templates = ['blog/base.html', 'blog/contact.html']
        self.assertTemplateUsed(response, *templates)

    def test_blog_detail_page_url(self):
        response = self.client.get(reverse("post_detail", args=[1]), follow=True)
        self.assertTemplateNotUsed(response, "post_detail.html")

    def test_blog_post_update_url(self):
        response = self.client.get(reverse("post_update", args=[1]), follow=True)
        self.assertTemplateNotUsed(response, "post_form.html")

    def test_blog_post_delete_url(self):
        response = self.client.get(reverse("post_delete", args=[1]), follow=True)
        self.assertTemplateNotUsed(response, "post_confirm_delete.html")

# Test models
