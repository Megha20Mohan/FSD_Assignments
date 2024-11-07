from django.contrib import admin
from django.urls import path,include
from recommendation import views

urlpatterns = [
    path("new/",views.register,name="r"),
    path("registration/",views.registration,name="r"),
    path("hobbies/",views.hobbies,name="r")

    # path('admin/', admin.site.urls),
    # path('register/', include('recommendation.urls')),
    # path('recommendation/', include('recommendation.urls'))
]