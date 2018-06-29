# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CustomerCare(models.Model):
    care_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('CustomerInfo', models.DO_NOTHING, blank=True, null=True)
    care_theme = models.CharField(max_length=50, blank=True, null=True)
    care_way = models.CharField(max_length=50, blank=True, null=True)
    care_time = models.DateTimeField()
    care_remark = models.CharField(max_length=1000, blank=True, null=True)
    care_nexttime = models.DateTimeField()
    care_people = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_care'


class CustomerCondition(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=50, blank=True, null=True)
    condition_explain = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_condition'


class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True)
    condition = models.ForeignKey(CustomerCondition, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('CustomerSource', models.DO_NOTHING, blank=True, null=True)
    # user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('CustomerType', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_sex = models.CharField(max_length=10, blank=True, null=True)
    customer_mobile = models.CharField(max_length=20, blank=True, null=True)
    customer_qq = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=500, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_remark = models.CharField(max_length=1000, blank=True, null=True)
    customer_job = models.CharField(max_length=100, blank=True, null=True)
    customer_blog = models.CharField(max_length=100, blank=True, null=True)
    customer_tel = models.CharField(max_length=20, blank=True, null=True)
    customer_msn = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.DateTimeField()
    customer_addtime = models.DateTimeField()
    customer_addman = models.CharField(max_length=50, blank=True, null=True)
    customer_changtime = models.DateTimeField()
    change_man = models.CharField(max_length=20, blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_info'


class CustomerLinkman(models.Model):
    linkman_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    linkman_name = models.CharField(max_length=50, blank=True, null=True)
    linkman_sex = models.CharField(max_length=20, blank=True, null=True)
    linkman_job = models.CharField(max_length=100, blank=True, null=True)
    linkman_mobile = models.CharField(max_length=20, blank=True, null=True)
    linkman_age = models.IntegerField(blank=True, null=True)
    linkman_relation = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_linkman'


class CustomerLinkreord(models.Model):
    record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    link_time = models.DateTimeField()
    who_link = models.CharField(max_length=50, blank=True, null=True)
    link_type = models.CharField(max_length=50, blank=True, null=True)
    link_theme = models.CharField(max_length=200, blank=True, null=True)
    link_nexttime = models.DateTimeField()
    link_remark = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_linkreord'


class CustomerSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_source'


class CustomerType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_type'