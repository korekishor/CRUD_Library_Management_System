from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('add.html', views.add,name="add"),
    path('login.html', views.login,name="login"),
    path('view.html', views.view,name="view"),

    path('signup.html', views.signup,name="signup"),
    path('signin.html', views.signin,name="signin"),
    path('books.html', views.books,name="books"),
    path('delete/<int:id>/', views.delete_data,name="deletedata"),
    path('<int:id>/', views.update_data,name="updatedata"),

    # path('', views.home,name="home"),

    path('hirebook',views.hire1,name="hire"),
    path('hdeletedata/<int:id>',views.hdelete_data, name="/hdeletedata"),
    path('<int:id>/', views.hupdate_data, name="/hupdatedata"),
    path('login1.html', views.login1,name="login1"),

]

