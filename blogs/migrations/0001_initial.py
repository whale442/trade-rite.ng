# Generated by Django 4.0.5 on 2022-06-25 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('content', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('datedate_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'db_table': 'blogs',
                'managed': True,
            },
        ),
    ]
