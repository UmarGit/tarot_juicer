# Generated by Django 2.2.13 on 2021-01-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToggle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_protection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PassPhrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passphrase', models.CharField(default='YourMagicPassphrase', max_length=100)),
            ],
        ),
    ]
