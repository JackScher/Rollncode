# Generated by Django 3.1.1 on 2020-09-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=255)),
                ('ISBN_code', models.CharField(max_length=255, unique=True)),
                ('author', models.ManyToManyField(to='library.Author')),
            ],
        ),
    ]
