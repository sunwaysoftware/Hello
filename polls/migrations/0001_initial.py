# Generated by Django 3.0.3 on 2020-02-20 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='买方名称')),
                ('tax_no', models.CharField(max_length=50, verbose_name='企业税号')),
                ('address', models.CharField(max_length=100, verbose_name='联系地址')),
                ('contact_name', models.CharField(max_length=100, verbose_name='联 系 人')),
                ('contact_tel', models.CharField(blank=True, max_length=100, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '买方',
                'verbose_name_plural': '买方信息',
            },
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='卖方名称')),
                ('tax_no', models.CharField(max_length=50, verbose_name='企业税号')),
                ('address', models.CharField(max_length=100, verbose_name='经营地址')),
                ('tel', models.CharField(max_length=100, verbose_name='联系电话')),
                ('account_bank', models.CharField(max_length=100, verbose_name='开户银行')),
                ('account_no', models.CharField(max_length=100, verbose_name='银行账号')),
            ],
            options={
                'verbose_name': '卖方',
                'verbose_name_plural': '卖方信息',
            },
        ),
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(max_length=50, verbose_name='合同编号')),
                ('contract_name', models.CharField(max_length=100, verbose_name='合同名称')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='合同总额')),
                ('award_date', models.DateField(verbose_name='签定日期')),
                ('expiry_date', models.DateField(verbose_name='有效日期')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Buyers', verbose_name='买方名称')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Sellers', verbose_name='卖方名称')),
            ],
            options={
                'verbose_name': '合同',
                'verbose_name_plural': '合同档案',
            },
        ),
    ]
