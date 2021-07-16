from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    confirm_email = models.EmailField()
    short_bio = models.TextField(null=True, max_length=500, blank=True)


# 参考https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy
# 创建两个receiver修饰符以便当我们创建/更新User实例时，Profile模型会自动被创建/被更新，
# 当一个save发生时，我们将下面这两个methods跟User模型挂钩，这样的signal叫做post_save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
