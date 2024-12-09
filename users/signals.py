from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


#@receiver(post_save, sender=Profile)
def createdProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
    print('profile updated!')

#@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()

    print('profile deleted!')

post_save.connect(createdProfile, sender=User)
post_delete.connect(profileDeleted, sender=Profile)