from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(APIView):
    def get(self, request, id=None):
        if id:
            object = models.User.objects.get(id=id)
            serializer = serializers.UserSerializer(object)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        objects = models.User.objects.all()
        serializer = serializers.UserSerializer(objects, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        object = models.User.objects.get(id=id)
        serializer = serializers.UserSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        object = models.User.objects.filter(id=id)
        print(object)
        object.delete()
        return Response({"status": "success", "data": "User Deleted"}, status=status.HTTP_200_OK)