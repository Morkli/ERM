# Generated by Django 3.0.7 on 2020-09-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200909_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='member_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
