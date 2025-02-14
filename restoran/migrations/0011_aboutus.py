# Generated by Django 5.1.2 on 2025-02-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0010_alter_galleryimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.URLField()),
                ('image2', models.URLField()),
                ('image3', models.URLField()),
                ('image4', models.URLField()),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
                ('experience_years', models.IntegerField()),
                ('master_chefs', models.IntegerField()),
            ],
        ),
    ]
