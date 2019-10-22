# Generated by Django 3.0a1 on 2019-10-14 19:39

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0027_drop_brin_index'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='testtable',
            index=django.contrib.postgres.indexes.BrinIndex(
                condition=models.Q(test_field_int__isnull=False),
                fields=['test_field_int'],
                name='test_index',
            ),
        ),
    ]
