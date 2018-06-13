# Generated by Django 2.0.5 on 2018-06-13 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id_file', models.BigAutoField(primary_key=True, serialize=False)),
                ('path_file', models.FilePathField(default=None)),
                ('status', models.CharField(default='Stand by', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default=None, max_length=255, unique=True, verbose_name='email address')),
                ('group', models.CharField(default='user', max_length=50)),
                ('last_name', models.CharField(default=None, max_length=150, null=True)),
                ('first_name', models.CharField(default=None, max_length=200, null=True)),
                ('affiliation', models.TextField(default=None, null=True)),
                ('orcid', models.CharField(default=None, max_length=19, null=True)),
                ('last_date_upload', models.DateField(default=None, null=True)),
                ('number_of_upload_this_day', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='importfile',
            name='id_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
