from django.urls import include,path
from . import views

urlpatterns = [

	path(r"", views.index, name = 'index'),
	path('add',views.add , name = 'add_task'),
	path('edit/<int:task_id>',views.edit , name = 'edit'),
	path('editt/<int:task_id>',views.editt , name = 'editt'),
	path('delete/<int:task_id>',views.delete , name = 'delete'),
	path('mark_done/<int:task_id>',views.mark_done , name = 'mark_done'),
	path('hide_done',views.hide_done , name = 'hide_done'),
	path('addt',views.addt , name = 'addt')
	

]
