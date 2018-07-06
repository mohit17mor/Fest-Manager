from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

class User(AbstractUser):

    USER_TYPE_CHOICES = (
        (1,'organiser'),
        (2,'vendor'),
    )
    user_type = models.PositiveSmallIntegerField(null=True,choices = USER_TYPE_CHOICES)

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phone = models.CharField(null=True, max_length=15)
    organisation = models.CharField(null=True, max_length=50)

    def get_type(self):
        for tpl in self.USER_TYPE_CHOICES:
            if tpl[0] == self.user_type:
                return tpl[1]

class Contract(models.Model):

    CONTRACT_TYPE_CHOICES = (
        ('proshow','proshow'),
        ('catering','catering'),
        ('logistics','logistics'),
    )

    vendor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        limit_choices_to = Q(user_type = 2), # type 2 = vendor
        related_name = 'vendor',
        null = True,
    )

    organiser = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        limit_choices_to = Q(user_type = 1), # type 1 = organiser
        related_name = 'organiser',
        null = True,
    )

    description = models.CharField(max_length = 500)
    date_of_contract = models.DateField(null = True)
    price = models.IntegerField(null = True)
    contract_type = models.CharField(null = True, max_length = 20, choices = CONTRACT_TYPE_CHOICES)

