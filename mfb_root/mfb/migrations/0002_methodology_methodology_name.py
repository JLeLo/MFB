# Generated by Django 3.2.5 on 2021-08-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='methodology',
            name='methodology_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]