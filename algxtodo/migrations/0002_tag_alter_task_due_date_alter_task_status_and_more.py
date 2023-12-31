# Generated by Django 5.0 on 2023-12-22 14:07

import algxtodo.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("algxtodo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(
                blank=True, null=True, validators=[algxtodo.models.validate_due_date]
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("OPEN", "OPEN"),
                    ("WORKING", "WORKING"),
                    ("DONE", "DONE"),
                    ("OVERDUE", "OVERDUE"),
                ],
                default="OPEN",
                max_length=7,
            ),
        ),
        migrations.RemoveField(
            model_name="task",
            name="tags",
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(blank=True, to="algxtodo.tag"),
        ),
    ]
