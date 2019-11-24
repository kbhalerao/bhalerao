# Generated by Django 2.2.6 on 2019-11-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0003_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.AddField(
            model_name='menu',
            name='cb',
            field=models.URLField(default='nothing', help_text='Carrie Busey Menu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='ems',
            field=models.URLField(default='nothing', help_text='Edison Menu'),
            preserve_default=False,
        ),
    ]