from django.test import TestCase, SimpleTestCase
from api_Immfly.models import Channel, Content
from django.core.management import call_command
from api_Immfly.management.commands.ratings import Command


class RatingTestCase(TestCase):

    @classmethod
    def setUpTestData(self):

        Channel.objects.create(id=3, title='prueba', langueage = 'Español' , image = 'image.jpg',)
        self.channel = Channel.objects.get(id=3)
        Content.objects.create(id=7, ranking=5, channel_id=3)
        self.contents=Content.objects.all()
       


    def test_calculate_average(self):
        
        dict_average = {}
        result = Command().calculate_average(self.contents, self.channel, None , dict_average)
        self.assertEqual(result, {'prueba': 5} )
