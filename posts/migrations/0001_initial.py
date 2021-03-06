# Generated by Django 4.0.5 on 2022-06-15 13:00

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('categories_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='', max_length=255)),
                ('time', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=False)),
                ('image', models.TextField(default='')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_user', models.CharField(default='', max_length=255)),
                ('comment_email', models.CharField(default='', max_length=255, null=True)),
                ('comment_content', models.TextField(default='')),
                ('time', models.DateTimeField(auto_now=True)),
                ('posts_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.posts')),
            ],
        ),
    ]
