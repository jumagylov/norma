# Generated by Django 3.1.5 on 2021-05-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_ofd'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofd',
            name='images',
            field=models.ImageField(default=1, upload_to='ofd/images'),
            preserve_default=False,
        ),
    ]
