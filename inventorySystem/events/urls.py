"""
URL configuration for inventorySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.appOverview, name='events'),
    path('event-list/', views.eventList, name='event-list'),
    path('event-datail/<str:id>', views.viewByID, name='event-datails'),
    path('create-event/', views.createEvent, name='create-event'),
    path('update-event/<str:id>', views.updateEvent, name='update-event'),
    path('delete-event/<str:id>', views.deleteEvent, name='delete-event'),
]