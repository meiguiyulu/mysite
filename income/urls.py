from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:contents_user_pk>', views.AddIncome, name='addincome'),
    path('addincomecontent/<int:user_pk>', views.AddIncomeContent, name='addincomecontent'),
    path('personalcenterincome/<int:pk1>', views.PersonalCenterIncome, name='personalcenterincome'),
    path('incomedetail/<int:content_pk>', views.IncomeDetail, name='incomedetail'),
    path('deleteincome/<int:incomedetail_pk>', views.DeleteIncome, name='deleteincome'),
    path('saveincome/<int:incomedetail_pk>', views.SaveIncome, name='saveincome'),
    path('incomelist/<int:user_pk>', views.IncomeList, name='incomelist'),
    path('memberincomelist/<int:user_pk>', views.SearchIncome, name='memberincomelist'),
]
