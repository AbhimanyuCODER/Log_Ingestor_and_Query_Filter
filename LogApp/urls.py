# LogApp/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('ingest/', views.ingest_logs, name='ingest_logs'),
    path('query/', views.query_logs, name='query_logs'),
    path('display-logs/', views.display_logs, name='display_logs'),
    # Other URL patterns...
]
