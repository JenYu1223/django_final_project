from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField(default=list, null=True, blank=True)
    suggested_course_id = models.JSONField(blank=True, default=list, null=True)
    recently_viewed_course_id = models.JSONField(blank=True, default=list, null=True)


    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()

@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.delete()
    except UserProfile.DoesNotExist:
        pass