from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.contrib.auth.forms import UserCreationForm

# Function-based views

def index(request):
    # Fetch all tasks and categories, ordered by due date
    tasks = Task.objects.all().order_by('due_date')
    categories = Category.objects.all()

    context = { 
        'tasks': tasks,
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def detailed_task(request, id):
    # Fetch a specific task by id or return 404 if not found
    task = get_object_or_404(Task, id=id)

    context = {
        'task': task
    }
    return render(request, 'main/detailed.html', context)

def todo_by_status(request, st):
    # Filter tasks by status
    todos = Task.objects.filter(status=st)
    
    context = {
        'todos': todos
    }
    return render(request, 'main/todosstatus.html', context)

def Todo_list_Category(request, id):
    # Filter tasks by category id
    todos = Task.objects.filter(category=id)
    categories = Category.objects.all()

    context = {
        "tasks": todos,
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def Createtodo(request):
    # Create a new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the record in the database
            return redirect('home')
    else:  
        form = TaskForm()
    return render(request, 'main/create_todo.html', {'form': form})

def createCategory(request):
    # Create a new category
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the record in the database
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request, 'main/createCategorys.html', {'form': form})

def update_task(request, id):
    # Update an existing task
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the record in the database
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html', {'form': form})

def delete_task(request, id):
    # Delete a task
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def signup(request):
    # Handle user sign-up
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})
