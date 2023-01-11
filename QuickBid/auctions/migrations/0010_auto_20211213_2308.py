# Generated by Django 3.2.8 on 2021-12-14 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]