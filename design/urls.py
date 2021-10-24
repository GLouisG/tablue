from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^new/proj$', views.new_proj, name='new_proj'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/',  views.search, name='search'),
    url(r'^update/profile$', views.update_profile, name='update_profile'),
    url(r'^project/(\d+)', views.single, name='single'),
    url(r'^you/', views.you, name="you"), 
    url(r'^api/proj/$', views.ProjList.as_view(),name = "apiproj" ),
    url(r'^api/prof/$', views.ProfList.as_view(),name="apiprof" ),      

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)