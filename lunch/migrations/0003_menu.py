# Generated by Django 2.2.6 on 2019-11-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0002_auto_20191009_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]