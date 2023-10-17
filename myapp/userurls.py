from django.contrib import admin
from django.urls import path
from . import views
from . import admin_dahsboard_calculations

urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('select_branch/', views.select_branch, name='select_branch'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

    path('branchwise_total_guest/', admin_dahsboard_calculations.branchwise_total_guest, name='branchwise_total_guest'),
    path('total_vaccant_share_choose_branches/', admin_dahsboard_calculations.total_vaccant_share_choose_branches,name='total_vaccant_share_choose_branches'),
    path('branchwise_total_collection', admin_dahsboard_calculations.branchwise_total_collection, name='branchwise_total_collection'),

    path('details_branch12/', admin_dahsboard_calculations.details_branch12, name='details_branch12'),
    path('details_branch13/', admin_dahsboard_calculations.details_branch13, name='details_branch13'),
    path('details_branch14/', admin_dahsboard_calculations.details_branch14, name='details_branch14'),

    path('logout/', views.logout, name='logout'),

]