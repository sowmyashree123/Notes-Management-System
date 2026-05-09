from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_note),
    path('view-notes/', views.view_notes),
    path('delete/<int:id>/', views.delete_note),
    path('edit/<int:id>/', views.edit_note),
    
     # API URLs
    path('api/notes/', views.api_get_notes),
    path('api/notes/add/', views.api_add_note),
    path('api/notes/delete/<int:id>/', views.api_delete_note),
    path('api/notes/update/<int:id>/', views.api_update_note),
   path('api/notes/search/', views.api_search_notes),
]