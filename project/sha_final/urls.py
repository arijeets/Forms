"""sha_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from sha_final_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #home navigation template url
    path('',views.home),

    # training_candidate_master urls
    path('training-candidate-master', views.training_candidate_master, name="training_candidate_master"), 
    path('training-candidate-master/view_query', views.view_query_candidate_master, name="view_query_candidate_master"),
    path('training-candidate-master/delete/<int:pk>/', views.delete_candidate_master, name='delete_candidate_master'),
    path('training-candidate-master/result/', views.view_query_show_candidate_master),
    path('training-candidate-master/update/<int:pk>/', views.update_candidate_master, name='update_candidate_master'),
    
    # course master urls
    path('course-master/create', views.course_master_new, name="course_master_new"),
    path('course-master/delete/<int:pk>/', views.delete_course, name='delete_course'),
    path('course-master/view', views.view_query_course, name="view_query_course"),
    path('course-master/update/<int:pk>/',views.update_course, name="update_course"),
    path('course-master/result/',views.view_query_show_course),

    # sourse master urls
    path('source-master/create', views.source_master_new, name="source_master_new"),
    path('source-master/view', views.view_query_source, name="view_query_source"),
    path('source-master/result/',views.view_query_show_source),
    path('source-master/update/<int:pk>/',views.update_source, name="update_source"),
    path('source-master/delete/<int:pk>/', views.delete_source, name='delete_source'),

    #calling master urls
    path('calling_master_form/',views.call_mast_save,name="calling_master_form"),
    path('view_query_callmast/', views.view_query_callmast, name="view_query_callmast"),
    path('calling-master/result/',views.view_query_show_callmast),
    path('call_mast_update/<int:pk>/',views.update_calling_master,name="update_calling_master"),
    path('call_mast_delete/<int:pk>/',views.call_mast_delete,name="call_mast_delete"),

    #calling transaction urls
    path('calling_transaction_form/',views.call_trans_save,name="calling_transaction_form"),
    path('view_query_calltrans/', views.view_query_calltrans, name="view_query_calltrans"),
    path('calling-transaction/result/',views.view_query_show_calltrans),
    path('call_trans_delete/<int:pk>/',views.call_trans_delete,name="call_trans_delete"),

    #training transaction urls
    path('training_transaction_form/', views.training_trans_save,name="training_transaction_form"),
    path('view_query_trainingtrans/', views.view_query_trainingtrans, name="view_query_trainingtrans"),
    path('training-transaction/result/',views.view_query_show_trainingtrans),
    path('training_transaction_delete/<int:pk>/', views.training_trans_delete,name="training_trans_delete"),

]
