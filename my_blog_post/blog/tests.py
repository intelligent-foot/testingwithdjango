from django.test import TestCase
from .models import Topic

# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Topic.objects.create(name = 'Django')

    def test_topic_model(self):
        d = self.blog
        self.assertTrue(isinstance(d,Topic))
        self.assertEqual(str(d),'Django')