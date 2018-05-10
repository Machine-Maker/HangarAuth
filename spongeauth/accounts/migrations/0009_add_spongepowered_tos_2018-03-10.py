# Generated by Django 2.0.3 on 2018-04-28 12:53

import datetime

from django.db import migrations



def create_tos(apps, schema_editor):
    TermsOfService = apps.get_model('accounts', 'TermsOfService')
    db_alias = schema_editor.connection.alias
    tos = TermsOfService(
            name='SpongePowered Terms of Service (2018-03-10)',
            tos_date=datetime.date(2018, 3, 10),
            tos_url='https://docs.spongepowered.org/stable/en/about/tos.html',
            current_tos=True)
    tos.save(using=db_alias)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180428_1214'),
    ]

    operations = [
        migrations.RunPython(create_tos),
    ]
