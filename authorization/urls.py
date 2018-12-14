from django.urls import path

from . import views as auth_views

urlpatterns = [
    path('greeting/(?P<name>\w+)/$', auth_views.greeting),
    path('grade/', auth_views.grade),
    path('filter/', auth_views.filter),
    path('list_user/', auth_views.list),

    path('users/', auth_views.UserListView.as_view(), name='users'),
    path('users/<str:pk>', auth_views.UserShowView.as_view(), name='show_user'),
    path('user/new', auth_views.UserCreateView.as_view(), name='new_user'),
    path('user/<str:pk>/edit', auth_views.UserUpdateView.as_view(), name='edit_user'),
    path('user/<str:pk>/delete', auth_views.UserDeleteView.as_view(), name='delete_user'),

    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('login_check/', auth_views.loginCheck, name='login_check'),
]