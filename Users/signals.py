from django.db.models.signals import post_save
from .models import SiteUser
from django.dispatch import receiver
from .models import Profile

# 06-18-20 6:03 pm. I dont know if ill ever see this again. Im in Lathrop rn. I hope we really made it man like really im feeling
# this project/idea has potential. UnveilSale has potential. Please make me the worlds youngest Billionaire. Waheguruji Ka Khalsa
# Waheguruji Ki Phate
@receiver(post_save, sender=SiteUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=SiteUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()