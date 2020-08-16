
from django.urls import path
from .views import hellofunction

#'admin/'＝リクエスト
# admin.site.urls＝指示
urlpatterns = [
    path('world/', hellofunction),
]
