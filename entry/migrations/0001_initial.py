# Generated by Django 2.2.5 on 2019-10-23 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adm_Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adm_Type', models.CharField(choices=[('Dip', 'Diploma'), ('CET', 'CET'), ('Mgmt', 'Management'), ('COC', 'Change Of College'), ('COMEDK', 'COMEDK'), ('GATE', 'GATE')], default='CET', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch', models.CharField(choices=[('CS', 'Computer Science'), ('IS', 'Information Science'), ('EC', 'Electronics And Communication'), ('CV', 'Civil'), ('ME', 'Mechanical'), ('None', 'None')], default='None', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(choices=[('BE', 'Bachelor Of Engineering (BE)'), ('ME', 'Master of Technology (MTech)'), ('MBA', 'Master Of Business Administration (MBA)'), ('MCA', 'Master Of Computer Applications (MCA)'), ('AFMA', '(AFMA)')], default='BE', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fee_Str',
            fields=[
                ('Fid', models.AutoField(primary_key=True, serialize=False)),
                ('Adm_Year', models.IntegerField(choices=[(2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020')], default=2019)),
                ('Apti_1', models.IntegerField()),
                ('Tech_2', models.IntegerField()),
                ('Book_3', models.IntegerField()),
                ('IndP_4', models.IntegerField()),
                ('IndV_5', models.IntegerField()),
                ('Inte_6', models.IntegerField()),
                ('Libr_7', models.IntegerField()),
                ('Semi_8', models.IntegerField()),
                ('Soft_9', models.IntegerField()),
                ('Conf_10', models.IntegerField()),
                ('Subj_11', models.IntegerField()),
                ('Spor_13', models.IntegerField()),
                ('Tran_14', models.IntegerField()),
                ('Volu_15', models.IntegerField()),
                ('Adm_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Adm_Types')),
                ('Branch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Branches')),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Quota_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quota', models.CharField(choices=[('Rural', 'Rural'), ('Kannada', 'Kannada'), ('HK', 'Hyderabad Karnataka'), ('SNQ', 'SNQ'), ('None', 'None')], default='None', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stud_PD',
            fields=[
                ('Sid', models.AutoField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=50)),
                ('USN', models.CharField(max_length=10, unique=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=6)),
                ('DOB', models.DateField()),
                ('POB', models.CharField(max_length=50)),
                ('S_Pno', models.CharField(max_length=10)),
                ('S_Add', models.TextField()),
                ('Batch', models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default='2019', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Stud_Admn',
            fields=[
                ('Adm_No', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Sem', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=1)),
                ('Adm_Type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Adm_Types')),
                ('Branch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Branches')),
                ('Course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Courses')),
                ('Fid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Fee_Str')),
                ('Quota', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Quota_List')),
                ('Sid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entry.Stud_PD')),
            ],
        ),
        migrations.AddField(
            model_name='fee_str',
            name='Quota',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entry.Quota_List'),
        ),
    ]