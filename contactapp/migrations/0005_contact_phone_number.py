# Generated by Django 5.1 on 2024-08-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0004_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]