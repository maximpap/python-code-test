# Generated by Django 2.2.6 on 2019-10-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiptrader', '0003_auto_20191002_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]