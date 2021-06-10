# Generated by Django 3.1.7 on 2021-05-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='small_desc',
        ),
        migrations.AddField(
            model_name='categories',
            name='department',
            field=models.CharField(choices=[('Dental Department', 'Dental Department'), ('Surgical Department', 'Surgical Department'), ('Neurological Department', 'Neurological Department'), ('Ophthalmological Department', 'Ophthalmological Department')], default=1, max_length=250),
            preserve_default=False,
        ),
    ]