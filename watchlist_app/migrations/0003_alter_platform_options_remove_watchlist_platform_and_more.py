# Generated by Django 5.0 on 2023-12-17 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist_app", "0002_watchlist_platform"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="platform",
            options={"ordering": ("-id",)},
        ),
        migrations.RemoveField(
            model_name="watchlist",
            name="platform",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="watchlist_app.platform",
            ),
        ),
    ]