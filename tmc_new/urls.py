"""tmc_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    # АВТОРИЗАЦИЯ
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # КОНЕЦ АВТОРИЗАЦИИ
    path('card/', Card.as_view(), name='card'),
    path('card/<int:id>', Card_id.as_view(), name='card_id'),
    # path('add_form/<int:id>', additional_form, name='form'),

    #ЧЕК ЛИСТЫ
    path('card/checklist/save/<int:id>', CheckListSaveView.as_view(), name='checklist-save'),
    path('card/checklists/<int:id>', CheckListJournalView.as_view(), name='checklists-journal'),
]
