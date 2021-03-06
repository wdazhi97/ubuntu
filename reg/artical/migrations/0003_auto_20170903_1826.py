# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artical', '0002_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewTime', models.DateTimeField(null=True, verbose_name='审稿时间')),
                ('reviewOpinionToAuthor', models.TextField(null=True, verbose_name='给作者的审稿意见')),
                ('reviewOpinionToEditor', models.TextField(null=True, verbose_name='给编辑的审稿意见')),
                ('reviewResult', models.CharField(choices=[('0', '强烈推荐'), ('1', '推荐'), ('2', '弱推荐'), ('3', '弱拒绝'), ('4', '拒绝'), ('5', '强烈拒绝')], max_length=1, null=True, verbose_name='审稿结果')),
            ],
        ),
        migrations.RemoveField(
            model_name='inspect',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='inspect',
            name='reviewer',
        ),
        migrations.AlterModelOptions(
            name='paper',
            options={},
        ),
        migrations.AlterModelOptions(
            name='web',
            options={'verbose_name': '网页', 'verbose_name_plural': '网页'},
        ),
        migrations.RenameField(
            model_name='web',
            old_name='Approver',
            new_name='approver',
        ),
        migrations.RenameField(
            model_name='web',
            old_name='webAmender',
            new_name='webModifier',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authorAdress',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authorWorkplace',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentStatus',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='web',
            name='APPROVALStatus',
        ),
        migrations.RemoveField(
            model_name='web',
            name='ApprovalOpinion',
        ),
        migrations.RemoveField(
            model_name='web',
            name='ApprovalTime',
        ),
        migrations.RemoveField(
            model_name='web',
            name='FirstInstanceOpinion',
        ),
        migrations.RemoveField(
            model_name='web',
            name='FirstInstanceStatus',
        ),
        migrations.RemoveField(
            model_name='web',
            name='FirstInstanceTime',
        ),
        migrations.RemoveField(
            model_name='web',
            name='FirstReviewer',
        ),
        migrations.RemoveField(
            model_name='web',
            name='SecondInstanceOpinion',
        ),
        migrations.RemoveField(
            model_name='web',
            name='SecondInstanceStatus',
        ),
        migrations.RemoveField(
            model_name='web',
            name='SecondInstanceTime',
        ),
        migrations.RemoveField(
            model_name='web',
            name='SecondReviewer',
        ),
        migrations.RemoveField(
            model_name='web',
            name='webAmendTime',
        ),
        migrations.AddField(
            model_name='author',
            name='authorAddress',
            field=models.CharField(max_length=255, null=True, verbose_name='作者地址'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorCompany',
            field=models.CharField(max_length=255, null=True, verbose_name='作者工作单位'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorEmail',
            field=models.CharField(max_length=30, null=True, verbose_name='作者邮件地址'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorJob',
            field=models.CharField(max_length=30, null=True, verbose_name='作者职称'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorOfficePhone',
            field=models.CharField(max_length=12, null=True, verbose_name='作者办公电话'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reviewStatus',
            field=models.CharField(choices=[('0', '未审核'), ('1', '正在审核'), ('2', '已审核'), ('3', '批准'), ('4', '拒绝')], max_length=1, null=True, verbose_name='审核状态'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='web',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artical.web'),
        ),
        migrations.AddField(
            model_name='journal',
            name='jourEmail',
            field=models.CharField(max_length=255, null=True, verbose_name='期刊邮件地址'),
        ),
        migrations.AddField(
            model_name='journal',
            name='jourOfficePhone',
            field=models.CharField(max_length=12, null=True, verbose_name='期刊办公电话'),
        ),
        migrations.AddField(
            model_name='web',
            name='approvalOpinion',
            field=models.TextField(null=True, verbose_name='批准意见'),
        ),
        migrations.AddField(
            model_name='web',
            name='approvalStatus',
            field=models.CharField(choices=[('0', '正在批准'), ('1', '批准'), ('2', '拒绝')], max_length=1, null=True, verbose_name='批准状态'),
        ),
        migrations.AddField(
            model_name='web',
            name='approvalTime',
            field=models.DateTimeField(null=True, verbose_name='批准时间'),
        ),
        migrations.AddField(
            model_name='web',
            name='firstReviewOpinion',
            field=models.TextField(null=True, verbose_name='一审意见'),
        ),
        migrations.AddField(
            model_name='web',
            name='firstReviewStatus',
            field=models.CharField(choices=[('0', '未审核'), ('1', '正在审核'), ('2', '已审核'), ('3', '批准'), ('4', '拒绝')], max_length=1, null=True, verbose_name='一审状态'),
        ),
        migrations.AddField(
            model_name='web',
            name='firstReviewTime',
            field=models.DateTimeField(null=True, verbose_name='一审时间'),
        ),
        migrations.AddField(
            model_name='web',
            name='firstReviewer',
            field=models.CharField(max_length=30, null=True, verbose_name='第一审核人'),
        ),
        migrations.AddField(
            model_name='web',
            name='secondReviewOpinion',
            field=models.TextField(null=True, verbose_name='二审意见'),
        ),
        migrations.AddField(
            model_name='web',
            name='secondReviewStatus',
            field=models.CharField(choices=[('0', '未审核'), ('1', '正在审核'), ('2', '已审核'), ('3', '批准'), ('4', '拒绝')], max_length=1, null=True, verbose_name='二审状态'),
        ),
        migrations.AddField(
            model_name='web',
            name='secondReviewTime',
            field=models.DateTimeField(null=True, verbose_name='二审时间'),
        ),
        migrations.AddField(
            model_name='web',
            name='secondReviewer',
            field=models.CharField(max_length=30, null=True, verbose_name='第二审核人'),
        ),
        migrations.AddField(
            model_name='web',
            name='webModifyTime',
            field=models.DateTimeField(null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='author',
            name='authorName',
            field=models.CharField(max_length=30, verbose_name='作者姓名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='authorPhone',
            field=models.CharField(max_length=11, null=True, verbose_name='作者手机号'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentLevel',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentReviewTime',
            field=models.DateTimeField(null=True, verbose_name='审核时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(null=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='jourLevel',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True, verbose_name='期刊等级'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='jourPhone',
            field=models.CharField(max_length=11, verbose_name='期刊联系手机号'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='jourUrl',
            field=models.CharField(max_length=255, verbose_name='期刊网址'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paperChineseName',
            field=models.CharField(max_length=255, verbose_name='论文中文名称'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paperChineseSummary',
            field=models.CharField(max_length=1000, verbose_name='论文中文摘要'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paperEnglishName',
            field=models.CharField(max_length=255, verbose_name='论文英文名称'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paperEnglishSummary',
            field=models.CharField(max_length=1000, verbose_name='论文英文摘要'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paperStatus',
            field=models.CharField(choices=[('0', '已投稿'), ('1', '审稿'), ('2', '已录用'), ('3', '已拒绝')], max_length=1, null=True, verbose_name='论文录用状态'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerBankName',
            field=models.CharField(max_length=255, verbose_name='银行名称'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerEmail',
            field=models.CharField(max_length=128, verbose_name='邮件地址'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerMoney',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='审稿金额'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerName',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerOfficePhone',
            field=models.CharField(max_length=12, verbose_name='办公电话'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerSecondEmail',
            field=models.CharField(max_length=128, verbose_name='备用邮箱'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerTitle',
            field=models.CharField(max_length=3, verbose_name='职称'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewerWorkplace',
            field=models.CharField(max_length=255, verbose_name='工作单位'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='reviewernumber',
            field=models.IntegerField(null=True, verbose_name='审稿论文数'),
        ),
        migrations.AlterField(
            model_name='web',
            name='webCreateTime',
            field=models.DateTimeField(null=True, verbose_name='生成时间'),
        ),
        migrations.AlterField(
            model_name='web',
            name='webDetail',
            field=models.TextField(null=True, verbose_name='网页内容'),
        ),
        migrations.AlterField(
            model_name='web',
            name='webTitle',
            field=models.CharField(max_length=255, verbose_name='网页title'),
        ),
        migrations.AlterField(
            model_name='web',
            name='webUrl',
            field=models.CharField(max_length=255, verbose_name='网址'),
        ),
        migrations.DeleteModel(
            name='inspect',
        ),
        migrations.AddField(
            model_name='review',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artical.paper'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artical.reviewer'),
        ),
        migrations.AddField(
            model_name='reviewer',
            name='paper',
            field=models.ManyToManyField(through='artical.review', to='artical.paper'),
        ),
    ]
