# Generated by Django 5.0 on 2024-04-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='donations/media/images/'),
        ),
    ]
