from django.conf.urls import url
urlpatterns =[
	url(r'^$', views.home),
	url(r'^admin/', admin.site.urls),
	]