# Generated by Django 2.2.5 on 2023-07-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20230722_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
