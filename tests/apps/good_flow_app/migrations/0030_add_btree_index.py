# Generated by Django 3.0a1 on 2019-10-14 19:45

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0029_drop_brin_index_with_condition'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='testtable',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['test_field_int'], name='test_index'),
        ),
    ]
