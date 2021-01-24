from django.conf import settings
from django.conf.urls.static import static
from django .urls import path
from . import views

urlpatterns = [
    path(r'',views.home,name='home'),
    url(r'^project/$',views.project,name ='project'),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)