from django.core.management.base import BaseCommand, CommandError
from api_Immfly.models import Channel, Content
import statistics as stats
import csv


class Command(BaseCommand):

    def calculate_average(self, contents, channel, channel_parent, dict_average):
            #Generamos una lista con los contenidos que pertenecen al canal
            rating_contents = []
            rating_channel = 0
            if contents:
                for content in contents:
                    rating_contents.append(content.ranking)
                rating_channel = stats.mean(rating_contents)
                dict_average[channel.title] = round(rating_channel,2)  
            elif channel_parent.title in dict_average:
                total = dict_average[channel_parent.title] + dict_average[channel.title]
                rating_channel = total / 2
                dict_average[channel_parent.title] = round(rating_channel,2)
            else:
                dict_average[channel_parent.title] = round(dict_average[channel.title],2)
            return(dict_average)   

    def handle(self, *args, **options):

        def route_reverse_channels(channel,list_parents):
            for channel_parent in list_parents:
                self.calculate_average(None, channel, channel_parent, dict_average)
                list_parents = channel.parent.all()
                route_reverse_channels(channel_parent,list_parents)
        

        with open('average.csv', 'w', newline='') as csvfile:
        
            dict_average = {}
            channels = Channel.objects.all()
            for channel in channels:
                contents = Content.objects.filter(channel_id=channel.id).all()
                if contents:
                    self.calculate_average(contents, channel, None, dict_average) 
                    parents = channel.parent.all()
                    if parents:
                        route_reverse_channels(channel, parents)
            list_average = []
            for average in dict_average.items():
                list_average.append({'channel title':average[0], 'average rating':average[1]})
            order_average =  sorted(list_average, key=lambda a: a['average rating'], reverse=True)
            fieldnames = ['channel title', 'average rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(order_average)

     
       
             
               
        
       