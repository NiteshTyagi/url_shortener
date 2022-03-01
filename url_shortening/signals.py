from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.conf import settings

from url_shortening.models import URL


def _calculate_base62(self):
        result = []
        divisor = int(self.id)
        remainder = 0
        while divisor:
            divisor, remainder = divmod(divisor, 62)
            if 10<= remainder <=35:
                remainder = chr(97+remainder-10)
            elif 36<= remainder <=61:
                remainder = chr(65+remainder-36)
            else:
                remainder = str(remainder)
            
            result.append(remainder)
        result.reverse()
        return "".join(result)
        

@receiver(post_save, sender=URL)
def url_post_save_signal(sender, instance, created, **kwargs):
    with transaction.atomic():
        try:
            if created:
              instance.short_url =  '%s/%s'%(settings.DOMAIN_NAME, _calculate_base62(instance))
              instance.save()
        except Exception as e:
            pass