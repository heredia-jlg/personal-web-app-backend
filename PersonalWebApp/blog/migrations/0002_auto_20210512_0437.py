# Generated by Django 3.0.5 on 2021-05-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
