# Generated by Django 4.1.7 on 2023-03-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField()),
                ('left_at', models.DateTimeField(auto_now_add=True)),
                ('is_solved', models.BooleanField(default=False)),
            ],
        ),
    ]