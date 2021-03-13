from rest_framework import routers
from todo_list_api import viewsets

router = routers.DefaultRouter()
router.register('todo', viewsets.TodoViewSet)

