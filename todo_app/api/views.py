from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from todo_app.models  import todo_list
from todo_app.api.serializers import  todo_listSerializer




@api_view(["GET"])
def task_list(request):
    if request.method == "GET":
        query = todo_list.objects.all()
        serializer = todo_listSerializer(query,many=True)
        return Response(serializer.data)


@api_view()
def task_dateil(request,id):
    try:
        task = todo_list.objects.get(pk=id)
    except todo_list.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = todo_listSerializer(task)
        return Response(serializer.data)