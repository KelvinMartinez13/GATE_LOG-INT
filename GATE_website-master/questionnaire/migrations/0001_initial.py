# Generated by Django 4.1.7 on 2023-03-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Joueur",
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
                ("username", models.CharField(max_length=255)),
                ("qcmpdd1", models.FloatField(default=0)),
                ("qcmpdd2", models.FloatField(default=0)),
                ("qcmpdd3", models.FloatField(default=0)),
                ("qcmpdd1pourcentage", models.IntegerField(default=0)),
                ("qcmpdd2pourcentage", models.IntegerField(default=0)),
                ("qcmpdd3pourcentage", models.IntegerField(default=0)),
                ("qcmpddTpourcentage", models.IntegerField(default=0)),
                ("validepdd1", models.BooleanField(default=False)),
                ("validepdd2", models.BooleanField(default=False)),
                ("validepdd3", models.BooleanField(default=False)),
                ("validepddT", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="MdpEtAuthLv1",
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
                ("numero", models.CharField(max_length=255)),
                ("enonce", models.CharField(max_length=255)),
                ("reponse1", models.CharField(max_length=255)),
                ("reponse2", models.CharField(max_length=255)),
                ("reponse3", models.CharField(max_length=255)),
                ("reponce4", models.CharField(max_length=255)),
                ("reponseVrai", models.CharField(max_length=255)),
                ("reponse", models.CharField(max_length=255)),
                ("explication", models.CharField(default="", max_length=1000)),
                ("qcm", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ProtecDesDonneesLv1",
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
                ("numero", models.CharField(max_length=255)),
                ("enonce", models.CharField(max_length=255)),
                ("reponse1", models.CharField(max_length=255)),
                ("reponse2", models.CharField(max_length=255)),
                ("reponse3", models.CharField(max_length=255)),
                ("reponce4", models.CharField(max_length=255)),
                ("reponseVrai", models.CharField(max_length=255)),
                ("reponse", models.CharField(max_length=255)),
                ("explication", models.CharField(default="", max_length=1000)),
                ("qcm", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ProtecDesDonneesLv2",
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
                ("numero", models.CharField(max_length=255)),
                ("enonce", models.CharField(max_length=255)),
                ("reponse1", models.CharField(max_length=255)),
                ("reponse2", models.CharField(max_length=255)),
                ("reponse3", models.CharField(max_length=255)),
                ("reponce4", models.CharField(max_length=255)),
                ("reponseVrai", models.CharField(max_length=255)),
                ("reponse", models.CharField(max_length=255)),
                ("explication", models.CharField(default="", max_length=1000)),
                ("qcm", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ProtecDesDonneesLv3",
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
                ("numero", models.CharField(max_length=255)),
                ("enonce", models.CharField(max_length=255)),
                ("reponse1", models.CharField(max_length=255)),
                ("reponse2", models.CharField(max_length=255)),
                ("reponse3", models.CharField(max_length=255)),
                ("reponce4", models.CharField(max_length=255)),
                ("reponseVrai", models.CharField(max_length=255)),
                ("reponse", models.CharField(max_length=255)),
                ("explication", models.CharField(default="", max_length=1000)),
                ("qcm", models.BooleanField(default=False)),
            ],
        ),
    ]