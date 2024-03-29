# Generated by Django 4.1.7 on 2023-03-15 11:19

import DjangoPetstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_created_user_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default=None, upload_to='media_files/accounts_app', validators=[DjangoPetstagram.photos.validators.check_file_size_5mb]),
            preserve_default=False,
        ),
    ]
