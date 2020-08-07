from django.urls import path
from . import views
from income.views import AddIncome
from accountsystem.views import PersonalCeneter, PersonalCenterAgain

urlpatterns = [
    path('', PersonalCeneter, name='personalcenter'),
    path('<int:pk1>/<int:pk2>', PersonalCenterAgain, name='personalcenteragain'),
    path('<int:contents_user_pk>', views.AddExpend, name='addexpend'),
    path('addcontent/<int:user_pk>', views.AddContent, name='addcontent'),
#    path('addcontent/', views.AddContent, name='addcontent'),
    path('expenddetail/<int:content_pk>', views.ExpendDetail, name='exxpenddetail'),
    path('expenddelete/<int:expenddetail_pk>', views.ExpendDelete, name='expenddelete'),
    path('saveexpend/<int:expenddetail_pk>', views.SaveExpend, name='saveexpend'),
    path('expendlist/<int:user_pk>', views.ExpendList, name='expendlist'),
   # path('returnlist/<int:user_pk>', views.ReturnList, name='returnlist'),
    path('memberexpendlist/<int:user_pk>', views.SearchExpends, name='memberexpendlist'),
]

