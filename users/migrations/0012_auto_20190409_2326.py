# Generated by Django 2.1.7 on 2019-04-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_detailedbudget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Debt_Payments_Each_Month',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Getting_Married',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Graduating_College',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Housing_Cost_Per_Month',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Income_Per_Year',
        ),
        migrations.RemoveField(
            model_name='detailedbudget',
            name='Purchasing_A_Home',
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Alcohol',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Auto_and_Transport',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Eating_Out',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Education',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Gas',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Gifts_and_Donations',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Groceries',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Health_and_Fitness',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Housing',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Personal_Care',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='detailedbudget',
            name='Pets',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
