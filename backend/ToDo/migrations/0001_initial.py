# Generated by Django 4.0.3 on 2022-10-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name': 'ToDo',
                'verbose_name_plural': 'ToDos',
            },
        ),
    ]