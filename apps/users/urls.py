from django.urls import path, include

from apps.users.views import CabinetIndexView, CabinetUpdateUserInfo

app_name = 'users'

urlpatterns = [
    path('cabinet/',
         include(([
                      path('', CabinetIndexView.as_view(), name='index'),
                      path('update-info/', CabinetUpdateUserInfo.as_view(), name='update_user_info'),
                  ], 'cabinet'))),
]
