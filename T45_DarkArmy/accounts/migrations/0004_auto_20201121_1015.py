# Generated by Django 3.1.1 on 2020-11-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201121_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='injury_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='injury_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
