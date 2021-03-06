# Generated by Django 3.1.2 on 2022-03-01 06:37

from django.db import migrations, models
import url_shortening.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.CharField(default=url_shortening.models._generate_uuid, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('long_url', models.URLField(db_index=True, max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'URLs',
            },
        ),
    ]
