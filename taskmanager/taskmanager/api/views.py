from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory storage
tasks = []
task_id_counter = 1

@api_view(['GET', 'POST'])
def tasks_handler(request):
    global task_id_counter
    if request.method == 'GET':
        return Response(tasks)

    elif request.method == 'POST':
        data = request.data
        new_task = {
            "id": task_id_counter,
            "title": data.get("title"),
            "completed": False
        }
        tasks.append(new_task)
        task_id_counter += 1
        return Response(new_task, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def task_detail(request, id):
    global tasks
    for task in tasks:
        if task["id"] == id:
            if request.method == 'PUT':
                task["completed"] = True
                return Response(task)
            elif request.method == 'DELETE':
                tasks = [t for t in tasks if t["id"] != id]
                return Response({"message": "Task deleted"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
