# Generated by Django 5.0.6 on 2024-05-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernumber', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
