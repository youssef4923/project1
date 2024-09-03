from django.urls import path
from .views import (
    index, detailed_task, todo_by_status, Todo_list_Category, 
    Createtodo, createCategory, update_task, delete_task, signup
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Patterns for the URL /, /products

    # Listing all todos
    path('', index, name="home"),

    # Detail view of a specific task
    path('detailed/<int:id>/', detailed_task, name="detail"),
    path('todo/update/<int:id>/', update_task, name="update-task"),
    path('todo/delete/<int:id>/', delete_task, name="delete-task"),

    # Todos by status (e.g., pending, in progress, completed)
    path('todos/status/<str:st>/', todo_by_status, name="status"),

    # Todos by category
    path('todo/category/<int:id>/', Todo_list_Category, name="cattodo"),

    # Create new todo and category
    path('todo/create/', Createtodo, name="createtodo"),
    path('category/create/', createCategory, name='createcategory'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),  # Updated signup view
]
