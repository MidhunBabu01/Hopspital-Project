# Generated by Django 3.1.7 on 2021-05-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_auto_20210531_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='small_desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
