# Generated by Django 3.2 on 2022-04-28 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '__first__'),
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dialog_in_receiver', to='accounts.employe')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_in_sender', to='accounts.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Group_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(blank=True, max_length=20, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='Chat/Groups/logos/')),
                ('info', models.CharField(blank=True, max_length=200)),
                ('add_members', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('admins', models.ManyToManyField(blank=True, related_name='my_admin_groups', to='accounts.Employe')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_groups', to='accounts.employe')),
                ('members', models.ManyToManyField(related_name='my_follow_groups', to='accounts.Employe')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500)),
                ('file', models.FileField(blank=True, upload_to='Chat/messages/files/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.employe')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.contact')),
                ('dialog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dialog_messages', to='chat.dialog_chat')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.group_chat')),
            ],
        ),
    ]