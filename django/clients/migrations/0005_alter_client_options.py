# Generated by Django 5.2.3 on 2025-06-20 11:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0004_alter_client_annotations"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ["created_at", "name"], "verbose_name": "Client", "verbose_name_plural": "Clients"},
        ),
    ]
