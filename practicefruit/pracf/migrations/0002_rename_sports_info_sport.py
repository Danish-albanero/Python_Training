# Generated by Django 3.2.6 on 2021-09-02 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pracf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='sports',
            new_name='sport',
        ),
    ]
