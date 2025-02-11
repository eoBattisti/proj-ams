# Generated by Django 5.1.2 on 2025-02-05 20:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("street", models.CharField(max_length=100, verbose_name="Rua")),
                ("number", models.IntegerField(verbose_name="Numero")),
                ("neighborhood", models.CharField(max_length=100, verbose_name="Bairro")),
                ("city", models.CharField(max_length=100, verbose_name="Cidade")),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created At")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated At")),
                ("name", models.TextField(verbose_name="Nome")),
                ("phone", models.TextField(verbose_name="Telefone")),
                ("annotations", models.TextField(verbose_name="Anotações")),
                ("address", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="clients.address")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
