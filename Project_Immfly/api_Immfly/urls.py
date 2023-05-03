from django.urls import path
from .views import ViewChannelsParents, ViewChannels, ViewChannelContent

urlpatterns=[
    path('channels/', ViewChannelsParents.as_view(), name='channels_list'),
    path('channel/<channelId>', ViewChannels.as_view(), name='channels_list'),
    path('contents/<channelId>', ViewChannelContent.as_view(), name='contents_list'),
]