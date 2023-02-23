
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):


    dependencies = [
        ('photos', '0003_alter_photo_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('date_of_publication', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
    ]
