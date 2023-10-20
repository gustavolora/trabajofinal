# Generated by Django 4.2.6 on 2023-10-19 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='status',
        ),
        migrations.AddField(
            model_name='deliveryperson',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='deliveryperson',
            name='identification',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='deliveryperson',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='delivery_persons/'),
        ),
        migrations.CreateModel(
            name='DeliveryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('cancelado', 'Cancelado'), ('entregado', 'Entregado')], max_length=15)),
                ('delivery_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.deliveryperson')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]