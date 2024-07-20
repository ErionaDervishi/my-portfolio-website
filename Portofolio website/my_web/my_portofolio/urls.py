

from django.urls import path
from . import views
from .views import project_detail
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_project_view, project_list_view
urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # About Me views
    path('about-me/', views.view_about_me, name='view_about_me'),
    path('about-me/edit/', views.about_me_edit_view, name='about_me_edit'),
    
    # Contact views
    path('contact/', views.view_contact, name='view_contact'),
    path('contact/edit/', views.contact_edit_view, name='contact_edit'),
    
    # Project views
    path('projects/', views.project_list_view, name='project_list'),
    path('projects/add/', views.add_project_view, name='add_project'),
    path('projects/<int:pk>/edit/', views.edit_project_view, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project_view, name='delete_project'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('projects/', project_list_view, name='project_list'),
    path('upload/', upload_project_view, name='upload_project')
    
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


