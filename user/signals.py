from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import Signal

from user.models import Customer


user_saved = Signal()


def customer_profile(sender, instance, created, *args, **kwargs):

    if created:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)

        data = kwargs['data']
        name = f'{data["first_name"]} {data["last_name"]}'
        email = data['email']
        phone = data['phone']

        Customer.objects.create(
            user=instance,
            name=name,
            email=email,
            phone=phone
        )


user_saved.connect(customer_profile, sender=User)
