# Generated by Django 4.0.4 on 2022-05-30 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='dafault value', upload_to='images/'),
        ),
    ]
