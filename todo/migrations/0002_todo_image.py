# Generated by Django 4.2.4 on 2023-09-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]