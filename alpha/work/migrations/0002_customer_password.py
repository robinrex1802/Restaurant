# Generated by Django 3.2.15 on 2022-10-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=225, null=True, verbose_name='Password'),
        ),
    ]
