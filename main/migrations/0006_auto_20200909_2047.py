# Generated by Django 3.0.7 on 2020-09-09 20:47

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200909_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='member_id',
            field=models.CharField(default=main.models.id_no, max_length=10, primary_key=True, serialize=False),
        ),
    ]
