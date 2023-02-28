from django.db import models

class Image(models.Model):
    upload = models.ImageField(upload_to ='uploads/image/')
