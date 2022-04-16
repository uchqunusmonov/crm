# Generated by Django 3.2 on 2022-04-14 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdduserCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='postion',
            name='section',
        ),
        migrations.AlterField(
            model_name='employe',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.employe'),
        ),
        migrations.AlterField(
            model_name='employe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postion',
            name='position',
            field=models.CharField(choices=[('', ''), ('director', 'director'), ('deputy', 'deputy'), ('worker', 'worker')], default=False, max_length=250, null=True),
        ),
    ]
