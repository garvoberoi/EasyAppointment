# Generated by Django 3.0.7 on 2020-10-08 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201007_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Doctor'),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='phone1',
            field=models.IntegerField(),
        ),
    ]
