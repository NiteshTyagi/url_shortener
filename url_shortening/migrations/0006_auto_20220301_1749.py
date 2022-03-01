# Generated by Django 3.1.2 on 2022-03-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortening', '0005_auto_20220301_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(db_index=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='url',
            name='total_clicks',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
