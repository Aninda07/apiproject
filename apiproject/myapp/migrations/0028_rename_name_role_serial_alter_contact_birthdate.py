# Generated by Django 4.0.6 on 2022-07-26 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_contact_birthdate_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='serial',
        ),
        migrations.AlterField(
            model_name='contact',
            name='Birthdate',
            field=models.DateField(default=datetime.datetime(2022, 7, 26, 10, 42, 23, 881464)),
        ),
    ]
