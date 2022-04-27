# Generated by Django 3.2 on 2022-04-27 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('add_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employe')),
                ('add_contact_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_contacts', to='accounts.employe')),
            ],
        ),
    ]
