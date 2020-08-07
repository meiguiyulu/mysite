"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accountsystem import views
from income.views import AddIncome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('personalcenter/', include('expend.urls')),
    path('addincome/', include('income.urls')),
    path('logout/', views.UserLogout, name='logout'),
    path('updateinformation/<int:user_pk>', views.UpdateInformation, name='updateinformation'),
    path('update/<int:user_pk>', views.Update, name='update'),
    path('memberlist/<int:user_pk>', views.MemberList, name='memberlist'),
    path('addmember/<int:user_pk>', views.AddMember, name='addmember'),
    path('savemember/<int:user_pk>', views.SaveMember, name='savemember'),
    path('memberdetail/<int:pk>', views.MemberDetail, name='memberdetail'),
    path('updatemember/<int:pk>', views.UpdateMember, name='updatemember'),
    path('deletemember/<int:pk>', views.DeleteMember, name='deletemember'),
    path('searchmember/<int:user_pk>', views.SearchMember, name='searchmember'),
]
