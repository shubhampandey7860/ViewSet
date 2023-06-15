from django.shortcuts import render

# Create your views here.
from app.models import Product
from app.serializers import Product_Serializer
from rest_framework import status


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ProductViewset(ViewSet):
    
    def list(self,request):
        obj = Product.objects.all()
        PMS = Product_Serializer(obj,many = True)
        return Response(PMS.data)
    
    def create(self,request):
        PMS = Product_Serializer(data = request.data)
        if PMS.is_valid():
            PMS.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=Product_Serializer(SPO)
        return Response(SPD.data)   
        
        
    def update(self,request,pk):
        PO = Product.objects.get(pk = pk)
        PMS = Product_Serializer(PO,data = request.data)
        if PMS.is_valid():
            PMS.save()
            return Response({"Success":"product is updated"})  
        else:
            return Response({"Failed":"product updation is failed"})  
    
    def partial_update(self,request,pk):
        PO = Product.objects.get(pk = pk)
        PMS = Product_Serializer(PO,data = request.data,partial = True)
        if PMS.is_valid():
            PMS.save()
            return Response({"Updated":"product is updated"})  
        else:
            return Response({"Failed":"product updation is failed"})
        
        
    def destroy(self,request,pk):
       obj = Product.objects.get(pk = pk).delete()
       return Response({"deleted":"Product is deleted"})         

        
        
        