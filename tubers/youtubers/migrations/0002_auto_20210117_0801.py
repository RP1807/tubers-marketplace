# Generated by Django 3.1.5 on 2021-01-17 08:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('tech_reviews', 'tech_reviews'), ('vlogs', 'vlogs'), ('traveling', 'traveling'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('cooking', 'cooking')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]