# Generated by Django 4.0.3 on 2022-04-21 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_usbook_alter_hirebook_issu_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usbook',
        ),
    ]
