# Generated by Django 4.2.6 on 2024-02-12 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sprincipale', models.CharField(max_length=100)),
                ('slocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_students', to='app1.school')),
            ],
        ),
    ]
