# Generated by Django 2.2.2 on 2019-08-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='img_url',
            new_name='img_url_before',
        ),
        migrations.AddField(
            model_name='card',
            name='img_url_after',
            field=models.TextField(default='http'),
            preserve_default=False,
        ),
    ]
