# Generated by Django 4.2.6 on 2024-02-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_projects_description_alter_skill_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
