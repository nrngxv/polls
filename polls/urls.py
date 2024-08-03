from django.contrib import admin
from django.urls import path

from main import views as poll_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", poll_view.home, name = "home"),
    path("create/", poll_view.create, name = "create"),
    path("results/<poll_id>", poll_view.results, name = "results"), #displays results with poll id
    path("vote/<poll_id>", poll_view.vote, name = "vote"), #displays vote with poll id
]