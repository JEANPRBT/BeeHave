# Generated by Django 3.0.8 on 2020-09-12 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.FilePathField(default=django.utils.timezone.now, path='C:\\Users\\Jean PERBET\\Codage\\beehave\\accounts/static/accounts/avatars/'),
            preserve_default=False,
        ),
    ]
