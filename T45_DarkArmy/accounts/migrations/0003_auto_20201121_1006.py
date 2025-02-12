# Generated by Django 3.1.1 on 2020-11-21 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201121_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.hospital'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.patient'),
        ),
    ]
