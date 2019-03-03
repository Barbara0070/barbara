"""nr1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from greetings.views import hello_world,hello_name

from meth.views import add
from meth.views import sub
from meth.views import multiply
from meth.views import divide
#from meth.views import smth
from django.urls import include
from cars.views import car_list
from cars.views import car_single
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world,),
    path('hello/', hello_world,),
    path('hello/<name>', hello_name),
    path('math/add/<first>/<second>', add),
    path('math/sub/<first>/<second>', sub),
    path('math/mlt/<first>/<second>', multiply),
    path('math/div/<first>/<int:second>', divide),
    #path('math/<smth>/<first>/<second>', smth),
    path('^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path("cars/", car_list),
    path("cars/<id>", car_single)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
