from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    path('contact/<int:contact_id>/', views.contact, name='contact'), #Read (ler o contato informacoes sobre)
    path('contact/create/', views.create, name='create'),  #Create
    path('contact/<int:contact_id>/update/', views.update, name='update'),  #Update
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),  #delete

    #User
    path('user/create/', views.register, name='register'),  #Create
    path('user/login/', views.login_view, name='login'),  
    path('user/logout/', views.logout_view, name='logout'),  

]
    
