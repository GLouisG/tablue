from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^new/post$', views.new_proj, name='new_proj'),
    url(r'^profile/(\d+)', views.profile, name='profile'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)