# Generated by Django 4.1.1 on 2022-10-04 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("betel", "0026_rename_fr_ficha_de_avaliacao_fr_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ficha_de_avaliacao",
            old_name="sra_complicacoes",
            new_name="SRA_complicacoes",
        ),
        migrations.RenameField(
            model_name="ficha_de_avaliacao",
            old_name="sra_quando",
            new_name="SRA_quando",
        ),
    ]
