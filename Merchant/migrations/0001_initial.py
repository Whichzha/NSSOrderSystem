# Generated by Django 2.2.4 on 2019-08-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchantdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('merchantName', models.CharField(max_length=16)),
                ('merchantPassword', models.CharField(max_length=16)),
                ('merchantMoney', models.IntegerField()),
            ],
        ),
    ]