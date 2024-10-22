from rest_framework import serializers
from.views import*
from.models import*

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    product_num=serializers.IntegerField()
    regular_price=serializers.IntegerField()
    sales_price=serializers.IntegerField()

class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model=Create 
        fields=['id','name','product_num','regular_price','sales_price']