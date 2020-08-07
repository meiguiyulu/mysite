from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from datetime import datetime
from accountsystem.models import Income, Expend, Member

def AddIncome(request, contents_user_pk):
    context = {}

    user = User.objects.get(pk=contents_user_pk)
    username = user.username
    user_members = Member.objects.filter(username_id=username)
    context['user'] = user
    context['user_members'] = user_members
    return render(request, 'addincome.html', context)

def AddIncomeContent(request, user_pk):
    referer = request.META.get('HTTP_REFERER', reverse('index'))
    context = {}

    user = User.objects.get(pk=user_pk)
    context['user'] = user

    if request.method == 'POST':
        #添加数据
        username = user.username
        date = request.POST['new_date']
        account = request.POST['account']
        incometype = request.POST['incometype']
        people = request.POST['people']
        money = request.POST['money']
        description = request.POST['description']

        if date.strip() == '':
            message = '时间为空'
            context['message'] = message
            context['redirect_to'] = referer
            return render(request, 'error.html', context)

        if money.strip() == '':
            message = '金额为空'
            context['message'] = message
            context['redirect_to'] = referer
            return render(request, 'error.html', context)

        Income.objects.create(username_id=username, date=date, account=account,
            incometype=incometype, people=people, money=money, description=description)

        #return redirect(referer)

    message = '添加成功'
    context['message'] = message
    context['redirect_to'] = referer
    return render(request, 'addIncomeSuccess.html', context)

def PersonalCenterIncome(request, pk1):
    context = {}

    user = User.objects.get(pk=pk1)
    contents_expend = Expend.objects.filter(username_id=user.username)
    contents_income = Income.objects.filter(username_id=user.username)

    context['contents_user'] = user
    context['contents_expend'] = contents_expend
    context['contents_income'] = contents_income

    return render(request, 'personalcenter.html', context)

def IncomeDetail(request, content_pk):
    context = {}

    incomedetail = Income.objects.get(pk=content_pk)
    username = incomedetail.username
    user_members = Member.objects.filter(username_id=username)

    context['incomedetail'] = incomedetail
    context['user_members'] = user_members
    return render(request, 'income-detail.html', context)

def DeleteIncome(request, incomedetail_pk):#删除
    context = {}

    detail = Income.objects.get(pk=incomedetail_pk)
    username = detail.username
    user = User.objects.get(username=username)
    context['user'] = user

    Income.objects.get(pk=incomedetail_pk).delete()
    message = '删除成功'
    context['message'] = message

    return render(request, 'deleteIncomesuccess.html', context)

def SaveIncome(request, incomedetail_pk):#修改以后保存
    context = {}
    incomedetail = Income.objects.get(pk=incomedetail_pk)
    username = incomedetail.username

    if request.method == 'POST':
        # 保存数据
        username = incomedetail.username
        newtime = request.POST['new_date'] + ' ' + request.POST['new_time']
        # datetime.strptime(newtime, 'Y-m-d H:m')
        datetime.strptime(newtime, '%Y-%m-%d %H:%M')
        account = request.POST['account']
        incometype = request.POST['incometype']
        people = request.POST['people']
        money = request.POST['money']
        description = request.POST['description']

        incomedetail.username = username
        incomedetail.date = newtime
        incomedetail.account = account
        incomedetail.incometype = incometype
        incomedetail.people = people
        incomedetail.money = money
        incomedetail.description = description
        incomedetail.save()

    # context['incomedetail'] = incomedetail
    # return render(request, 'incomedetail.html', context)

    user = User.objects.get(username=username)

    income_all_list = Income.objects.filter(username_id=username)
    paginator = Paginator(income_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_incomes = paginator.get_page(page_num)
    current_page_num = page_of_incomes.number  # 当前页码
    # 当前页码以及前后两页页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加省略页
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append('...')
    # 加首页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    # 加尾页
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context['contents_user'] = user
    context['contents_income'] = page_of_incomes.object_list
    context['page_of_incomes'] = page_of_incomes
    context['page_range'] = page_range

    return render(request, 'income-list.html', context)

def IncomeList(request, user_pk):
    context = {}

    user = User.objects.get(pk=user_pk)
    username = user.username

    income_all_list = Income.objects.filter(username_id=username)
    paginator = Paginator(income_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_incomes = paginator.get_page(page_num)
    current_page_num = page_of_incomes.number  # 当前页码
    # 当前页码以及前后两页页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加省略页
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append('...')
    # 加首页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    # 加尾页
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context['contents_user'] = user
    context['contents_income'] = page_of_incomes.object_list
    context['page_of_incomes'] = page_of_incomes
    context['page_range'] = page_range

    return render(request, 'income-list.html', context)

def SearchIncome(request, user_pk):
    context = {}
    referer = request.META.get('HTTP_REFERER', reverse('index'))

    user = User.objects.get(pk=user_pk)
    username = user.username

    if request.method == 'POST':
        membername = request.POST.get('member_name')

        if membername.strip() == '':
            return render(request, 'error.html', {'message': '未输入姓名',
                                                  'redirect_to': referer})

    income_all_list = Income.objects.filter(username_id=username, people=membername)
    if income_all_list.count() == 0:
        return render(request, 'error.html', {'message': '不存在',
                                              'redirect_to': referer})

    paginator = Paginator(income_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_incomes = paginator.get_page(page_num)
    current_page_num = page_of_incomes.number  # 当前页码
    # 当前页码以及前后两页页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加省略页
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append('...')
    # 加首页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    # 加尾页
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context['contents_user'] = user
    context['contents_income'] = page_of_incomes.object_list
    context['page_of_incomes'] = page_of_incomes
    context['page_range'] = page_range
    context['membername'] = membername

    return render(request, 'memberincome-list.html', context)
