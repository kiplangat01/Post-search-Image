# Generated by Django 4.0.4 on 2022-05-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_rename_uploader_image_user_alter_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
