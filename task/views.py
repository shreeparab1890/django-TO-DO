from django.shortcuts import render
from django.http import HttpResponse
from .models import task
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User


def index(request):
	if request.user.is_authenticated:
		user = request.user

	all_task = task.objects.all()
	context = {
		'all_task': all_task,
		'user':user,
	}

	
	return render(request, 'task/index.html', context)

def add(request):
	all_user = User.objects.all()
	context = {
		'all_user':all_user
	}
	return render(request, 'task/add_task.html',context)

def edit(request,task_id):
	all_user = User.objects.all()
	tasks = task.objects.filter(id=task_id)
	context = {
		'all_user':all_user,
		'tasks':tasks

	}
	return render(request, 'task/add_task.html',context)

def addt(request):
	if request.user.is_authenticated:
		user = request.user
	name = request.POST.get('name1')
	desc = request.POST.get('desc1')


	a = task()
	a.name = name
	a.desc = desc
	a.user = user
	a.save()

	all_task = task.objects.all()
	context = {
		'all_task': all_task,
		'user':user,
	}

	return render(request, 'task/index.html', context)

def editt(request,task_id):
    if request.user.is_authenticated:
        user = request.user
    u_id = user.id
    name = request.POST.get('name1')
    desc = request.POST.get('desc1')
    t_list = list(task.objects.filter(id=task_id))
    for a in t_list:
        if u_id == a.user.id:
            a.name = name
            a.desc = desc
            a.user = user
            a.save()
        else:
            all_task = task.objects.all()
            error_msg = "You Are Not Authorized To Edit This Task"
            context = {
		        'all_task': all_task,
		        'user':user,
                'error_msg':error_msg,
	        }
            return render(request, 'task/index.html', context)
    all_task = task.objects.all()
    context = {
		'all_task': all_task,
		'user':user,
	}
    return render(request, 'task/index.html', context)


def delete(request,task_id):

    if request.user.is_authenticated:
        user = request.user
    u_id = user.id



    t_list = list(task.objects.filter(id=task_id))
    for t in t_list:
        if u_id == t.user.id:
            t.delete()
        else:
            all_task = task.objects.all()
            error_msg = "You Are Not Authorized To Delete This Task"
            context = {
		        'all_task': all_task,
		        'user':user,
                'error_msg':error_msg,
	        }
            return render(request, 'task/index.html', context)

    all_task = task.objects.all()
    context = {
		'all_task': all_task,
		'user':user,
	}


    return render(request, 'task/index.html', context)
