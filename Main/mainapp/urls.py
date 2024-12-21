from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main),
    path('play/<id>', views.play),

    path('create', views.create),
    path('login', views.login),
    path('account/<id>/music/play_all', views.account_play_all),
    path('account/<id>/music', views.account_music),
    path('account/<id>/play/<music_id>', views.account_play),
    path('account/<id>', views.account_main),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
