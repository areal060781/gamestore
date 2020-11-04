# Generated by Django 3.1.2 on 2020-10-27 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(null=True)),
                ('developer', models.CharField(max_length=100)),
                ('published_by', models.CharField(max_length=100)),
                ('image', models.ImageField(default='images/placeholder.png', upload_to='images/')),
                ('highlighted', models.BooleanField(default=False)),
                ('gameplatform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.gameplatform')),
            ],
            options={
                'ordering': ['-highlighted', 'name'],
            },
        ),
    ]