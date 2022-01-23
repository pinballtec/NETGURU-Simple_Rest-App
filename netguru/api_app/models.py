from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Cars(models.Model):
    make = models.CharField(verbose_name='make', max_length=64)
    model = models.CharField(verbose_name='model', max_length=64)
    rating = models.IntegerField(verbose_name='rating', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True)