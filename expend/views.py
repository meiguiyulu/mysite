from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.urls import reverse
from accountsystem.models import Expend, Income, Member


def AddExpend(request, contents_user_pk):
    context = {}

    user = User.objects.get(pk=contents_user_pk)
    username = user.username
    user_members = Member.objects.filter(username_id=username)
    context['user'] = user
    context['user_members'] = user_members
    return render(request, 'addexpend.html', context)

def AddContent(request, user_pk):
    referer = request.META.get('HTTP_REFERER', reverse('index'))
    context = {}
    user = User.objects.get(pk=user_pk)
    context['contents_user'] = user

    if request.method == 'POST':
        # 添加数据
        username = user.username
        time = request.POST['new_add_time']
        account = request.POST['account']
        outcometype = request.POST['outcometype']
        people = request.POST['people']
        money = request.POST['money']
        description = request.POST['description']

        if time.strip() == '':
            message = '时间为空'
            context['message'] = message
            context['redirect_to'] = referer
            return render(request, 'error.html', context)

        if money.strip() == '':
            message = '金额为空'
            context['message'] = message
            context['redirect_to'] = referer
            return render(request, 'error.html', context)

        Expend.objects.create(username_id=username, date=time, account=account,
                           outcometype=outcometype, people=people, money=money,
                           description=description)

    #return render(request, 'login.html', context)
    #return redirect(referer)
    message = '添加成功'
    context['user'] = user
    context['message'] = message
    context['redirect_to'] = referer
    return render(request, 'addExpendSuccess.html', context)

def ExpendDetail(request, content_pk):
    context = {}

    expenddetail = Expend.objects.get(pk=content_pk)
    username = expenddetail.username
    user = User.objects.get(username=username)
    user_members = Member.objects.filter(username_id=username)

    context['user'] = user
    context['expenddetail'] = expenddetail
    context['user_members'] = user_members

    return render(request, 'expend-detail.html', context)

def ExpendDelete(request, expenddetail_pk):#删除开销
    context = {}

    detail = Expend.objects.get(pk=expenddetail_pk)
    username = detail.username_id
    user = User.objects.get(username=username)

    detail.delete()

    message = '删除成功'
    context['message'] = message
    context['user'] = user
    return render(request, 'deleteExpendsuccess.html', context)

def SaveExpend(request, expenddetail_pk):
    context = {}

    expenddetail = Expend.objects.get(pk=expenddetail_pk)
    username = expenddetail.username

    if request.method == 'POST':
        # 添加数据
        newtime = request.POST['new_date'] + ' ' + request.POST['new_time']
        #datetime.strptime(newtime, 'Y-m-d H:m')
        datetime.strptime(newtime, '%Y-%m-%d %H:%M')
        account = request.POST['account']
        outcometype = request.POST['outcometype']
        people = request.POST['people']
        money = request.POST['money']
        description = request.POST['description']

        expenddetail.username = username
        expenddetail.date = newtime
        expenddetail.account = account
        expenddetail.outcometype = outcometype
        expenddetail.people = people
        expenddetail.money = money
        expenddetail.description = description
        expenddetail.save()

    #context['expenddetail'] = expenddetail
    #return render(request, 'enxpenddetail.html', context)

    user = User.objects.get(username=username)

    expend_all_list = Expend.objects.filter(username_id=username)
    paginator = Paginator(expend_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_expends = paginator.get_page(page_num)
    current_page_num = page_of_expends.number  # 当前页码
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
    context['contents_expend'] = page_of_expends.object_list
    context['page_of_expends'] = page_of_expends
    context['page_range'] = page_range

    return render(request, 'expend-list.html', context)

def ExpendList(request, user_pk):
    context = {}

    user = User.objects.get(pk=user_pk)
    username = user.username

    expend_all_list = Expend.objects.filter(username_id=username)
    paginator = Paginator(expend_all_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_expends = paginator.get_page(page_num)
    current_page_num = page_of_expends.number  #当前页码
    # 当前页码以及前后两页页码
    page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    #加省略页
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append('...')
    #加首页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    #加尾页
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context['contents_user'] = user
    context['contents_expend'] = page_of_expends.object_list
    context['page_of_expends'] = page_of_expends
    context['page_range'] = page_range

    return render(request, 'expend-list.html', context)

def SearchExpends(request, user_pk):
    context = {}
    referer = request.META.get('HTTP_REFERER', reverse('index'))

    user = User.objects.get(pk=user_pk)
    username = user.username

    if request.method == 'POST':
        membername = request.POST.get('member_name')

        if membername.strip() == '':
            return render(request, 'error.html', {'message': '未输入姓名',
                                                  'redirect_to': referer})

    expend_details_list = Expend.objects.filter(username_id=username, people=membername)

    if expend_details_list.count() == 0:
        return render(request, 'error.html', {'message': '不存在',
                                              'redirect_to': referer})

    paginator = Paginator(expend_details_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_expends = paginator.get_page(page_num)
    current_page_num = page_of_expends.number  # 当前页码
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
    context['contents_expend'] = page_of_expends.object_list
    context['page_of_expends'] = page_of_expends
    context['page_range'] = page_range
    context['membername'] = membername

    return render(request, 'memberepend-list.html', context)
