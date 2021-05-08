from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.insurance_form,name='insurance_insert'),
    path('<int:id>/', views.insurance_form,name='insurance_update'),
    path('delete/<int:id>/',views.insurance_delete,name='insurance_delete'),
    path('list/',views.insurance_list,name='insurance_list')
]