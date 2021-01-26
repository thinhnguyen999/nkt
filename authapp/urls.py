from django.urls import path
from .views import signin, signup, signout
from .import views


urlpatterns = [
    path('base_main/', views.base_main, name='base_main'),
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('info_NKT/', views.info_NKT, name='info_NKT'),
    path('ds_NKT/', views.ds_NKT, name='ds_NKT'),
    path('ds_NKT/delete', views.ds_NKT_delete, name='ds_NKT_delete'),
    path('report/', views.report, name='report'),
    path('report_bd/', views.report_bd, name='report_bd'),
    path('phe_duyet/', views.phe_duyet_thong_tin, name='phe_duyet'),
    path('repair_info_nkt/<int:pk>', views.repair_info_nkt, name='repair_info_nkt'),
    
    path('insertTab1', views.insertTab1, name='insertTab1'),
    path('insertKhuyetTatForm', views.insertKhuyetTatForm, name='insertKhuyetTatForm'),
    
    path('insertNhuCauForm', views.insertNhuCauForm, name='insertNhuCauForm'),
    path('insertNhuCauDNForm', views.insertNhuCauDNForm, name='insertNhuCauDNForm'),
    path('removeTTNKT', views.removeTTNKT, name='removeTTNKT'),
]