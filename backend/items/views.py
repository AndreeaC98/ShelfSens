from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ItemViewSet(APIView):
    def get(self, request, id=None):
        if id:
            object = models.Item.objects.get(id=id)
            serializer = serializers.ItemSerializer(object)
            return Response({"status": "succes", "data" : serializer.data}, status=status.HTTP_200_OK)

        objects = models.Item.objects.all()
        serializer = serializers.ItemSerializer(object, many=True)
        return Response({"status": "succes", "data" : serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        object = models.Item.objects.get(id=id)
        serializer = serializers.ItemSerializer(object, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        object = models.Item.objects.filter(id=id)
        print(object)
        object.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_200_OK)





    

