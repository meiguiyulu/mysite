from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    relation_choice = (('自己', '自己'), ('夫妻', '夫妻'), ('父子', '父子'), ('父女', '父女'), ('母子', '母子'),
                       ('母女', '母女'), ('兄弟姐妹', '兄弟姐妹'), ('其他', '其他'))

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                 to_field='username', default='lyj')#一家之主
    member_name = models.CharField(max_length=8)#成员姓名
    member_relation = models.CharField(max_length=4, choices=relation_choice)#关系
    description = models.TextField(null=True)  # 说明

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.member_name


class Expend(models.Model):#支出数据库表

    account_choice = (('现金', '现金'), ('银行卡', '银行卡'), ('支付宝', '支付宝'))
    outcome_choice = (('食品酒水', '食品酒水'), ('服饰', '服饰'), ('居家物业', '居家物业'),
                      ('行车交通', '行车交通'), ('交流通讯', '交流通讯'), ('休闲娱乐', '休闲娱乐'),
                      ('文化教育', '文化教育'), ('人情往来', '人情往来'), ('医疗医药', '医疗医药'),
                      ('其他', '其他'))

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                 to_field='username', default='lyj')
    date = models.DateTimeField(auto_now_add=False)  # 日期
    account = models.CharField(max_length=4, choices=account_choice)  # 账户
    outcometype = models.CharField(max_length=4, choices=outcome_choice)  # 支出类型
    '''people = models.ForeignKey(Member, on_delete=models.DO_NOTHING, to_field='member_name',
                               default='自己')'''
    people = models.CharField(max_length=8)
    money = models.FloatField(max_length=20)#金额
    description = models.TextField(null=True)#说明

    class Meta:
        ordering = ['date']

class Income(models.Model):#收入数据库表
    account_choice = (('现金', '现金'), ('银行卡', '银行卡'), ('支付宝', '支付宝'))
    income_choice = (('工资', '工资'), ('奖金补贴', '奖金补贴'), ('投资分红', '投资分红'), ('其他', '其他'))

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                 to_field='username', default='lyj')
    date = models.DateTimeField(auto_now_add=False)  # 日期
    account = models.CharField(max_length=4, choices=account_choice)  # 账户
    incometype = models.CharField(max_length=4, choices=income_choice) #收入类别
    '''people = models.ForeignKey(Member, on_delete=models.DO_NOTHING,
                               to_field='member_name', default='自己')'''
    people = models.CharField(max_length=8)
    money = models.FloatField(max_length=20)  # 金额
    description = models.TextField(null=True)  # 说明

    class Meta:
        ordering = ['date']

