# Generated by Django 4.0.3 on 2022-05-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_delete_usbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='hirebook',
            name='due2',
            field=models.IntegerField(default=0),
        ),
    ]
