# Generated by Django 4.2.6 on 2023-10-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_name_deliveryperson_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparando', 'Preparando'), ('en_camino', 'En Camino'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparando', 'Preparando'), ('en_camino', 'En Camino'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], max_length=15),
        ),
    ]
