# Generated by Django 4.2.2 on 2023-07-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbankmodel',
            name='balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
