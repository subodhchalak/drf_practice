# Generated by Django 5.0 on 2023-12-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ManyToManyField(
                related_name="watchlist", to="watchlist_app.platform"
            ),
        ),
    ]
