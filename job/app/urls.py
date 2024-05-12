from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('enroll_jobs',views.enroll_jobs,name='enroll_jobs'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
     path('logout/',views.user_logout,name="logout"),
     path('delete/<int:id>',views.delete_product,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('about_us/',views.about_us,name='about_us'),
    path('contact/',views.contact,name='contact'),
    path('search/', views.search, name='search'),
    path('price/',views.price,name='price'),
    path('learn_more/',views.learn_more,name='learn_more'),
    path('show/<int:id>',views.show,name='show')
]


