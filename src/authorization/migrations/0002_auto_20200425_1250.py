# Generated by Django 3.0.5 on 2020-04-25 12:50

import authorization.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authorization", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="mvuser", managers=[("objects", authorization.models.UserManager()),],
        ),
        migrations.RemoveField(model_name="mvuser", name="username",),
    ]
