from django.db import models

# class ToMeet(models.Model):
#         persone = models.CharField(max_length=100)
#         phone_number = models.CharField(max_length=12)
#         date_of_meeting = models.DateField(auto_now_add=True)
#         comment = models.CharField(max_length=12)
#         is_closed = models.BooleanField(default=False)
#         is_favorite = models.BooleanField(default=False)
class ToMeet(models.Model):
        persone = models.CharField(max_length=100)
        phone_number = models.CharField(max_length=12)
        date_of_meeting = models.DateField(auto_now_add=True)
        comment = models.CharField(max_length=100)
        is_closed = models.BooleanField(default=False)
        is_favorite = models.BooleanField(default=False)