# Generated by Django 4.1.7 on 2023-05-09 01:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('key', models.SlugField(default='', help_text='Please enter a valid url key', unique=True)),
                ('pic', models.ImageField(upload_to='blog/')),
                ('short_description', models.TextField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
