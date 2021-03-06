# Generated by Django 3.2.6 on 2021-09-23 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.add_class')),
            ],
        ),
        migrations.CreateModel(
            name='Add_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120)),
                ('father_name', models.CharField(max_length=120)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('religion', models.CharField(max_length=1200)),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.add_class')),
            ],
        ),
    ]
