# Generated by Django 3.0a1 on 2019-12-10 21:47
from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('good_flow_app_concurrently', '0001_initial'),
    ]

    operations = [
        AddIndexConcurrently(
            model_name='testtable',
            index=models.Index(fields=['test_field_int'], name='good_flow_a_test_fi_0b7e6f_idx'),
        ),
    ]