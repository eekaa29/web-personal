from django.urls import path
from .views import HomeView, ProjectsView, CommunityView, ContactView, ContentView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("comunity/", CommunityView.as_view(), name="community"),
    path("content/", ContentView.as_view(), name="content"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("api/contact/", views.contact_api, name="contact_api"),
]