from django.db import models

class Channel(models.Model):

    parent = models. ManyToManyField('self', related_name='children',symmetrical=False , blank=True)
    title = models.CharField(max_length=255, unique=True)
    langueage = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%y/%m')
    

class Content(models.Model):

    ranking = models.IntegerField(default=0)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
   

class Metadatos(models.Model):
    
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

   