# Generated by Django 4.1 on 2023-03-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='number_of_hours',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]