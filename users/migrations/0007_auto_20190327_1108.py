# Generated by Django 2.1.7 on 2019-03-27 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190327_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='Income',
            new_name='Income_Per_Year',
        ),
    ]