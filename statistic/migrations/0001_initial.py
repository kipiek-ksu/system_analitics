# Generated by Django 3.0.3 on 2020-03-07 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statistic.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('grade', models.IntegerField(choices=[(7, 'Бакалавр'), (8, 'Магістр')])),
                ('education_form', models.IntegerField(choices=[(0, 'Денна'), (1, 'Заочна')])),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statistic.Speciality')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')])),
                ('value', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statistic.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statistic.Subject')),
            ],
        ),
    ]