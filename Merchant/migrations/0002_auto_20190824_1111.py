# Generated by Django 2.2.4 on 2019-08-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchantdaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchantAccountName', models.CharField(max_length=16)),
                ('merchantAccountPassword', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='merchantdata',
            name='merchantMoney',
        ),
        migrations.RemoveField(
            model_name='merchantdata',
            name='merchantPassword',
        ),
    ]
