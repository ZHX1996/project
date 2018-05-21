from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    
    class Meta:
        permissions = (
                    ("source", "can see source"),
                    ("logistic", "can see logistic"),
                    ("indoor", "can see indoor"),
                    )
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
