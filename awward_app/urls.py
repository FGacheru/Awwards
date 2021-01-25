from django.conf import settings
from django.conf.urls.static import static
from django .urls import path,re_path,include
from . import views

urlpatterns = [
    path(r'',views.home,name='home'),
    path('project/(\d+)', views.project, name='project_results'),
    path('upload_project/',views.upload_project,name ='new_project'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('profile/',views.profile,name ='user_profile'),
    path(r'search/',views.search, name='search'),
    
      
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)