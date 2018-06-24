from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.home,name = 'home'),
	url(r'^restaurant/', views.restaurant,name = 'Food Map'),
	url(r'^comment/(\d{1,157})/$',views.comment,name="comment"),
	url(r'^add/', views.add_restaurant,name='add_restaurant'),
	url(r'^bus/', views.bus,name = 'Bus Map'),
	url(r'^building/', views.building,name = 'Building Map'),
	#url(r'^weather/', views.weather,name = ' Map'),
	url(r'^store/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.UPLOAD_ROOT}),
]