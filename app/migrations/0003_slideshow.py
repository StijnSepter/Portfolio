# Generated by Django 4.2.5 on 2024-01-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_projects_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='slideshow',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('url', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
