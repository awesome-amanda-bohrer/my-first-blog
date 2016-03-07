from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    b = models.FloatField(verbose_name='Fatigue Strength Exponent, b = ', default=-0.087)
    c = models.FloatField(verbose_name='Fatigue Strength Exponent, c = ', default=-0.58)
    EpsilonPrime = models.FloatField(verbose_name='Epsilon Prime, EpsilonPrime = ', default=0.59)
    SigmaPrime = models.FloatField(verbose_name='Sigma Prime, SigmaPrime = ', default=495.0)
    Kcss = models.FloatField(verbose_name='Plasticity Parameter, Kcss = ', default=544.5)
    ncss = models.FloatField(verbose_name='Plasticity Exponent, ncss = ', default=0.15)
    ElasticModulus = models.FloatField(verbose_name='Elastic Modulus, E = ', default=20.0e4)

class UploadModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='./WangBrown')

class InputForm(ModelForm):
    class Meta:
        model = Input
        # omit the fields totally
        #fields = "__all__" - This was for Django >1.8

