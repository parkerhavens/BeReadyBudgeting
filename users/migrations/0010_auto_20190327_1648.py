# Generated by Django 2.1.7 on 2019-03-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190327_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='Getting_Married',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='budget',
            name='Graduating_College',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='budget',
            name='Purchasing_A_Home',
            field=models.BooleanField(default=False),
        ),
    ]
