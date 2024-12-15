# Generated by Django 5.1.2 on 2024-12-15 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classe",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nom_classe", models.CharField(max_length=20, unique=True)),
                ("nombre_heure_semaine", models.IntegerField()),
                ("description", models.TextField(null=True)),
            ],
            options={
                "verbose_name": "classe",
                "db_table": "classe",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Cours",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("intitule", models.CharField(blank=True, max_length=30, null=True)),
                ("heure_cours_semaine", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "cours",
                "db_table": "cours",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Etablissement",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "nom",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
            ],
            options={
                "verbose_name": "etablissement",
                "db_table": "etablissement",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "grade",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
            ],
            options={
                "verbose_name": "grade",
                "db_table": "grade",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Jour",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("jour", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "verbose_name": "jour",
                "db_table": "jour",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Matiere",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "matiere",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
            ],
            options={
                "verbose_name": "matiere",
                "db_table": "matiere",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Typecours",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "verbose_name": "type_cours",
                "db_table": "typecours",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ClasseCours",
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
                (
                    "id_classe",
                    models.ForeignKey(
                        db_column="id_classe",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.classe",
                    ),
                ),
                (
                    "id_cours",
                    models.ForeignKey(
                        db_column="id_cours",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.cours",
                    ),
                ),
            ],
            options={
                "verbose_name": "classe_cours",
                "db_table": "classe_cours",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Directeur",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(blank=True, max_length=20, null=True)),
                ("prenom", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "login",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "password",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "id_ets",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_ets",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.etablissement",
                    ),
                ),
            ],
            options={
                "verbose_name": "Directeur",
                "db_table": "Directeur",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Enseignant",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("prenom", models.CharField(blank=True, max_length=25, null=True)),
                ("heure_cours_semaine", models.IntegerField(blank=True, null=True)),
                (
                    "login",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "password",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "id_grade",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_grade",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.grade",
                    ),
                ),
            ],
            options={
                "verbose_name": "enseignant",
                "db_table": "enseignant",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Niveau",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("niveau", models.IntegerField(blank=True, null=True, unique=True)),
                (
                    "id_etablissement",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_Etablissement",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.etablissement",
                    ),
                ),
            ],
            options={
                "db_table": "niveau",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="classe",
            name="id_niveau",
            field=models.ForeignKey(
                db_column="id_Niveau",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="EmploiDeTemps.niveau",
            ),
        ),
        migrations.CreateModel(
            name="Periode",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("date_debut", models.IntegerField(blank=True, null=True)),
                ("date_fin", models.IntegerField(blank=True, null=True)),
                (
                    "id_jour",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_Jour",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.jour",
                    ),
                ),
            ],
            options={
                "verbose_name": "periode",
                "db_table": "periode",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Salle",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "nom",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "id_ets",
                    models.ForeignKey(
                        db_column="id_departement",
                        default=0,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.etablissement",
                    ),
                ),
            ],
            options={
                "db_table": "salle",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="cours",
            name="id_salle",
            field=models.ForeignKey(
                db_column="id_salle",
                default=0,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="EmploiDeTemps.salle",
            ),
        ),
        migrations.CreateModel(
            name="Senceur",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(blank=True, max_length=20, null=True)),
                ("prenom", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "login",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "password",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "id_niveau",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_Niveau",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.niveau",
                    ),
                ),
            ],
            options={
                "verbose_name": "senceur",
                "db_table": "senceur",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="cours",
            name="id_typecours",
            field=models.ForeignKey(
                blank=True,
                db_column="id_typeCours",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="EmploiDeTemps.typecours",
            ),
        ),
        migrations.CreateModel(
            name="EnseignantMatiere",
            fields=[
                (
                    "id_enseignant",
                    models.OneToOneField(
                        db_column="id_Enseignant",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="EmploiDeTemps.enseignant",
                    ),
                ),
                (
                    "id_matiere",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_Matiere",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.matiere",
                    ),
                ),
            ],
            options={
                "verbose_name": "enseignant_matiere",
                "db_table": "enseignant_matiere",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SalleEnseignant",
            fields=[
                (
                    "id_enseignant",
                    models.OneToOneField(
                        db_column="id_Enseignant",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="EmploiDeTemps.enseignant",
                    ),
                ),
                (
                    "id_salle",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_Salle",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.salle",
                    ),
                ),
            ],
            options={
                "verbose_name": "salle_enseignant",
                "db_table": "salle_enseignant",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ClasseEnseignantCours",
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
                (
                    "id_classe",
                    models.ForeignKey(
                        db_column="id_classe",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.classe",
                    ),
                ),
                (
                    "id_cours",
                    models.ForeignKey(
                        db_column="id_cours",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.cours",
                    ),
                ),
                (
                    "id_enseignant",
                    models.ForeignKey(
                        db_column="id_eseignant",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.enseignant",
                    ),
                ),
            ],
            options={
                "db_table": "classe_enseignant_cours",
                "managed": True,
                "unique_together": {("id_cours", "id_classe", "id_enseignant")},
            },
        ),
        migrations.CreateModel(
            name="ClassePeriodeCours",
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
                (
                    "id_cours",
                    models.ForeignKey(
                        db_column="id_Cours",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.cours",
                    ),
                ),
                (
                    "id_periode",
                    models.ForeignKey(
                        db_column="id_Periode",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.periode",
                    ),
                ),
                (
                    "id_salle",
                    models.ForeignKey(
                        db_column="id_Salle",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EmploiDeTemps.salle",
                    ),
                ),
            ],
            options={
                "verbose_name": "classe_periode_cours",
                "db_table": "classe_periode_cours",
                "managed": True,
                "unique_together": {("id_salle", "id_periode")},
            },
        ),
        migrations.CreateModel(
            name="SallePeriode",
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
                (
                    "id_periode",
                    models.ForeignKey(
                        db_column="id_periode",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.periode",
                    ),
                ),
                (
                    "id_salle",
                    models.ForeignKey(
                        db_column="id_salle",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="EmploiDeTemps.salle",
                    ),
                ),
            ],
            options={
                "unique_together": {("id_periode", "id_salle")},
            },
        ),
    ]
