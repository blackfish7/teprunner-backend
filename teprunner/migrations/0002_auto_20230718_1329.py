# Generated by Django 3.1.3 on 2023-07-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teprunner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(verbose_name='任务id')),
                ('case_id', models.IntegerField(verbose_name='用例id')),
            ],
            options={
                'db_table': 'task_case',
            },
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(verbose_name='任务id')),
                ('case_id', models.IntegerField(verbose_name='用例id')),
                ('result', models.CharField(max_length=50, verbose_name='运行结果')),
                ('elapsed', models.CharField(max_length=50, verbose_name='耗时')),
                ('output', models.TextField(default='', verbose_name='输出日志')),
                ('run_env', models.CharField(max_length=20, verbose_name='运行环境')),
                ('run_user_nickname', models.CharField(max_length=64, verbose_name='运行用户昵称')),
                ('run_time', models.DateTimeField(auto_now=True, verbose_name='运行时间')),
            ],
            options={
                'db_table': 'task_result',
            },
        ),
        migrations.RenameModel(
            old_name='Plan',
            new_name='Task',
        ),
        migrations.DeleteModel(
            name='CaseResult',
        ),
        migrations.DeleteModel(
            name='EnvVar',
        ),
        migrations.DeleteModel(
            name='Fixture',
        ),
        migrations.DeleteModel(
            name='PlanCase',
        ),
        migrations.DeleteModel(
            name='PlanResult',
        ),
        migrations.RemoveField(
            model_name='case',
            name='code',
        ),
        migrations.RemoveField(
            model_name='case',
            name='source',
        ),
        migrations.AddField(
            model_name='case',
            name='filepath',
            field=models.CharField(default='', max_length=500, verbose_name='文件路径'),
        ),
        migrations.AlterModelTable(
            name='task',
            table='task',
        ),
    ]