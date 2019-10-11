from django.db import models



class Song(models.Model):
   album = models.CharField(max_length=250)
   file = models.FileField(upload_to='musics/')
   song_title = models.CharField(max_length=250)
   

   def __str__(self):
       return self.song_title


