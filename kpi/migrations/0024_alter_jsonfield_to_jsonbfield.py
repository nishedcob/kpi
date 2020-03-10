# Generated by Django 2.2.7 on 2020-02-25 19:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import kpi.fields.kpi_uid
import kpi.models.asset_file
import kpi.models.import_export_task
import private_storage.fields
import private_storage.storage.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0023_partial_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='_deployment_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='asset',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='summary',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='assetsnapshot',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assetsnapshot',
            name='source',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='assetversion',
            name='_deployment_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='messages',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='messages',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
