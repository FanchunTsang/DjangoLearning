# Generated by Django 2.1.7 on 2019-04-03 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190403_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cuser_id',
            new_name='user',
        ),
    ]
