# Generated by Django 4.1.7 on 2023-03-15 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_created_comment and like models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocomment',
            options={'ordering': ['-date_of_publication']},
        ),
    ]
