# Generated by Django 4.2.14 on 2024-07-22 16:02

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('title', 'author', 'genre')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgresTest.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postgres_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('book', 'user')},
            },
        ),
    ]
