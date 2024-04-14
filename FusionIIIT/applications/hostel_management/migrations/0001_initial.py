# Generated by Django 3.1.5 on 2024-04-15 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_id', models.CharField(max_length=10)),
                ('hall_name', models.CharField(max_length=50)),
                ('max_accomodation', models.IntegerField(default=0)),
                ('number_students', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=10)),
                ('worker_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=2020)),
                ('month', models.IntegerField(default=1)),
                ('absent', models.IntegerField(default=0)),
                ('total_day', models.IntegerField(default=31)),
                ('remark', models.CharField(max_length=100)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
        migrations.CreateModel(
            name='StaffSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_type', models.CharField(default='Caretaker', max_length=100)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=15)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='globals.staff')),
            ],
        ),
        migrations.CreateModel(
            name='HostelStudentAttendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='HostelNoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_line', models.CharField(max_length=100)),
                ('content', models.FileField(blank=True, null=True, upload_to='hostel_management/')),
                ('description', models.TextField(blank=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='HallWarden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.faculty')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
        migrations.CreateModel(
            name='HallRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
                ('block_no', models.CharField(max_length=1)),
                ('room_cap', models.IntegerField(default=3)),
                ('room_occupied', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
        migrations.CreateModel(
            name='HallCaretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.staff')),
            ],
        ),
        migrations.CreateModel(
            name='GuestRoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4, unique=True)),
                ('room_status', models.CharField(choices=[('Booked', 'Booked'), ('CheckedIn', 'Checked In'), ('Available', 'Available'), ('UnderMaintenance', 'Under Maintenance')], default='Available', max_length=20)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
        migrations.CreateModel(
            name='GuestRoomBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_phone', models.CharField(max_length=15)),
                ('guest_email', models.CharField(blank=True, max_length=40)),
                ('guest_address', models.TextField(blank=True)),
                ('rooms_required', models.IntegerField(blank=True, default=1, null=True)),
                ('total_guest', models.IntegerField(default=1)),
                ('purpose', models.TextField()),
                ('arrival_date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled'), ('CancelRequested', 'Cancel Requested'), ('CheckedIn', 'Checked In'), ('Complete', 'Complete'), ('Forward', 'Forward')], default='Pending', max_length=15)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
                ('nationality', models.CharField(blank=True, max_length=20)),
                ('guest_room_id', models.ManyToManyField(to='hostel_management.GuestRoomDetail')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
                ('intender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
