# Generated by Django 4.2.2 on 2023-07-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_withdrawamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='notimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicnew', models.CharField(max_length=50)),
                ('textar', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]