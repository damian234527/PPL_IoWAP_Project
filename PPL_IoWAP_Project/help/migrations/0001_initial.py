# Generated by Django 4.2.9 on 2024-01-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
    ]
