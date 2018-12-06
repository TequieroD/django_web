from django.urls import path

from . import views as activity_views

urlpatterns = [
    path('summary/$', activity_views.summary),
    path('info/$', activity_views.info),

    path('activities/', activity_views.list_activities),
    path('activity/<str:pk>', activity_views.show_activity),
    path('activity/', activity_views.create_activity),
    path('activity/<str:pk>/edit', activity_views.update_activity),
    path('activity/<str:pk>/delete', activity_views.delete_activity),
]