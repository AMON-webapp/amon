# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cubedata(models.Model):
    declination = models.FloatField(blank=True, null=True)
    right_ascension = models.FloatField(db_column='RightAscension', blank=True, null=True)  # Field name made lowercase.
    DeDx = models.FloatField(db_column='dEdX', blank=True, null=True)  # Field name made lowercase.
    emu = models.FloatField(db_column='Emu', blank=True, null=True)  # Field name made lowercase.
    nch = models.FloatField(db_column='NCH', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(blank=True, null=True)
    day = models.FloatField(blank=True, null=True)
    second = models.FloatField(blank=True, null=True)
    mjd = models.FloatField(db_column='MJD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cubedata'
