# Generated by Django 3.1.3 on 2020-11-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201107_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='phone1',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='phone2',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]