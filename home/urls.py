from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("emails",views.emails,name="emails"),
    path("compose", views.compose, name="compose"),
    path("inbox", views.inbox, name="inbox"),
    path("download", views.download, name="download"),
    path("logout", views.logout, name="logout"),

]
