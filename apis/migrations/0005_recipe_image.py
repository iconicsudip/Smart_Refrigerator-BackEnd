# Generated by Django 4.0.3 on 2023-05-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_rename_capsicum_fridge_beans_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.TextField(default=None),
        ),
    ]
