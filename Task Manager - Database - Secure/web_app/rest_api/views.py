from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import NotFound

from .models import Tasks
from .serializers import AppSerializer, UserSerializer

class AppView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        tasks = Tasks.objects.all() if user.is_superuser else Tasks.objects.filter(user=user)
        serializer = AppSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed', False),
            'description': request.data.get('description', ''),
            'user': request.user.id
        }

        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": "Database Integrity Error: " + str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, app_id, user):
        try:
            return Tasks.objects.get(id=app_id) if user.is_superuser else Tasks.objects.get(id=app_id, user=user)
        except Tasks.DoesNotExist:
            raise NotFound(f"Task with id {app_id} not found.")

    def get(self, request, app_id, *args, **kwargs):
        task = self.get_object(app_id, request.user)
        serializer = AppSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, app_id, *args, **kwargs):
        task = self.get_object(app_id, request.user)
        data = {
            'task': request.data.get('task', task.task),
            'completed': request.data.get('completed', task.completed),
            'description': request.data.get('description', task.description),
            'user': task.user.id
        }
        serializer = AppSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, app_id, *args, **kwargs):
        task = self.get_object(app_id, request.user)
        task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)

class UserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

def index(request):
    return render(request, 'index/home.html')