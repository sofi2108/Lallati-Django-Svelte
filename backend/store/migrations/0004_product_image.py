# Generated by Django 4.1.5 on 2023-01-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_collection_feature_product_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]