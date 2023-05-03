
from django.http.response import JsonResponse
from django.views import View
from .models import Channel, Content


#todos los canales que no tienen padre
class ViewChannelsParents(View):
    
    def get(self, request):
        channels = Channel.objects.filter(parent=None).all()
        print("channels",channels)
        list_channels =  list(channels.values())    
        data = {'message': "Success", 'channels': list_channels}
        return JsonResponse(data)  

#canales hijos de un canal especifico
class ViewChannels(View):

    def get(self, request, channelId):
        channels = Channel.objects.filter(parent=channelId).all()
        list_channels =  list(channels.values())
        if list_channels:
            data = {'message': "Success", 'Channels':list_channels}
        else:
            data = {'message': "Not Subchannels found..."}
        return JsonResponse(data)


#contenidos para un id de canal especifico
class ViewChannelContent(View):

    def get(self, request, channelId):
        contents = Content.objects.filter(channel_id=channelId).all() 
        if contents:  
            list_contents = list(contents.values()) 
            data = {'message': "Success", 'contents': list_contents}
        else:
            data = {'message': "Not content found ..."}
        return JsonResponse(data)


 