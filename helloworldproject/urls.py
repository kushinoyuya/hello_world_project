from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldView

#'admin/'＝リクエスト
# admin.site.urls＝指示
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworldapp.urls'))
]
