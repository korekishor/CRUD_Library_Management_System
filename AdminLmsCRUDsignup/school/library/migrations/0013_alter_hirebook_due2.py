# Generated by Django 4.0.3 on 2022-05-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_hirebook_due2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirebook',
            name='due2',
            field=models.DateField(default='666'),
        ),
    ]
