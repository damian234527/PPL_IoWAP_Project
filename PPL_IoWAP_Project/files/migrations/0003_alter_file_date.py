# Generated by Django 4.2.9 on 2024-01-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_alter_file_date_alter_file_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]