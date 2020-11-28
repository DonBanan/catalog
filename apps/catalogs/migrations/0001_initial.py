# Generated by Django 3.1.3 on 2020-11-28 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
    ]