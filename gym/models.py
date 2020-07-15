from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=25, unique=True)
    mobile_no = models.IntegerField(unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name


class Chats(models.Model):
    quries = models.TextField(max_length=500)

    def __str__(self):
        return self.quries
