# Generated by Django 5.0.6 on 2024-06-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='learn_more_link',
        ),
        migrations.AlterField(
            model_name='service',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
