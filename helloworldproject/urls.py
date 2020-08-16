from django.contrib import admin
from django.urls import path
from .views import helloworldfunction

#'admin/'＝リクエスト
# admin.site.urls＝指示
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
]
