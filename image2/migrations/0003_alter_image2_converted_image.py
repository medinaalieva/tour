# Generated by Django 5.1.5 on 2025-02-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image2', '0002_image2_converted_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image2',
            name='converted_image',
            field=models.ImageField(blank=True, null=True, upload_to='converted_images/'),
        ),
    ]
