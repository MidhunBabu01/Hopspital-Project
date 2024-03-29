# Generated by Django 3.1.7 on 2021-05-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Dental Department', 'Dental Department'), ('Surgical Department', 'Surgical Department'), ('Neurological Department', 'Neurological Department'), ('Ophthalmological Department', 'Ophthalmological Department')], max_length=250)),
                ('hosptladrs', models.TextField()),
                ('dprtimag', models.ImageField(upload_to='')),
                ('small_desc', models.TextField()),
                ('big_desc', models.TextField()),
                ('doctor_name', models.CharField(max_length=250)),
                ('doctor_img', models.ImageField(upload_to='pictures')),
                ('doctor_detail', models.TextField()),
            ],
        ),
    ]
