from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import*
from.serializers import*

class CreatesView(APIView):
    def get(self,request,*args,**kwargs):
        ab=Create.objects.all()
        if 'product_num' in request.query_params:
            ss=request.query_params.get('product_num')
            ab=ab.filter(product_num=ss)
        if 'regular_price__lte' in request.query_params:
            ss=request.query_params.get('regular_price__lte')
            ab=ab.filter(regular_price__lte=ss)
        ss=ProductSerializer(ab,many=True)
        return Response(data=ss.data)
    def post(self,request,*args,**kw):
        serial=AllSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            # ab=Create.objects.create(**serial.validated_data)
            return Response(data=serial.data)
        else:
            return Response(data=serial.errors)
class UpdateView(APIView):
    def get(self,request,*args,**kw):
        id=kw.get('id')
        ss=Create.objects.filter(id=id)
        serial=ProductSerializer(ss,many=True)
        return Response(data=serial.data)
    def delete(self,request,*args,**kw):
        id=kw.get('id')
        ss=Create.objects.get(id=id)
        ss.delete()
        return Response(data='deleted')
    def put(self,request,*args,**kw):
        id=kw.get('id')
        ss=Create.objects.get(id=id)
        serial=AllSerializer(data=request.data,instance=ss)
        if serial.is_valid():
            serial.save()
            # ss=Create.objects.filter(id=id).update(**serial.validated_data)
            return Response(data=serial.data)
        else:
            return Response(data=serial.errors)
        



