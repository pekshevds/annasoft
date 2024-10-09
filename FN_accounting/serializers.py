from rest_framework import serializers
from .models import Point_of_sale, FN_type, FN, KKT
from crmapp.models import Customer

class Point_of_saleSerializer(serializers.ModelSerializer):
    customer_uid = serializers.CharField(source='customer.uid', required=False)
    class Meta:
        model = Point_of_sale
        fields = (
            'uid',
            'postcode',
            'title',
            'region',
            'area',
            'city',
            'locality',
            'street',
            'house',
            'customer_uid',
        )

    def create(self, validated_data):
        try:
            customer_uid = validated_data.pop('customer')
        except:
            customer_uid = None
        instance = Point_of_sale.objects.create(**validated_data)
        try:
            customer = FN_type.objects.get(uid=customer_uid.get('uid'))
        except:
            customer = None

        instance.customer = customer
        instance.save()
        return instance

    def create(self, instance, validated_data):
        try:
            customer_uid = validated_data.pop('customer')
        except:
            customer_uid = None
        instance = super().update(instance, validated_data)
        try:
            customer = Customer.objects.get(uid=customer_uid.get('uid'))
        except:
            customer = None

        instance.customer = customer
        instance.save()
        return instance    
 

class FNSerializer(serializers.ModelSerializer):
    fn_type_uid = serializers.CharField(source='fn_type.uid', label="Тип ФН", required=False)

    class Meta:
        model = FN
        fields = (
            'uid',
            'fn_model',
            'fn_type_uid',
            'fn_mn',
            'installation_date',
            'active',
            )

    def create(self, validated_data):
        try:
            fn_type_uid = validated_data.pop('fn_type')
        except:
            fn_type_uid = None
        instance = FN.objects.create(**validated_data)
        try:
            fn_type = FN_type.objects.get(uid=fn_type_uid.get('uid'))
        except:
            fn_type = None

        instance.fn_type = fn_type
        instance.save()
        return instance

    def update(self, instance, validated_data):
        try:
            fn_type_uid = validated_data.pop('fn_type')
        except:
            fn_type_uid = None
        instance = super().update(instance, validated_data)
        try:
            fn_type = FN_type.objects.get(uid=fn_type_uid.get('uid'))
        except:
            fn_type = None

        instance.fn_type = fn_type
        instance.save()
        return instance    

class KKTFullSerializer(serializers.ModelSerializer):
    fn = FNSerializer(read_only=True)
    class Meta:
        model = KKT
        fields = (
        'uid',
        'rn_kkt',
        'mn_kkt',
        'model_kkt',
        'fiscalization_date',
        'fn',
        )


class KKTSerializer(serializers.ModelSerializer):
    customer_uid = serializers.CharField(source='customer.uid', required=False)
    point_of_sale_uid = serializers.CharField(source='point_of_sale.uid', required=False)
    fn_uid = serializers.CharField(source='fn.uid', required=False)
    class Meta:
        model = KKT

        fields = (
            'uid',
            'rn_kkt',
            'mn_kkt',
            'model_kkt',
            'fiscalization_date',
            'customer_uid',
            'point_of_sale_uid',
            'customer_uid',
            'fn_uid',
            )

    def create(self,validated_data):
        try:
            customer_uid = validated_data.pop('customer')
        except:
            customer_uid = None
        try:       
            point_of_sale_uid = validated_data.pop('point_of_sale')
        except:
            point_of_sale_uid = None
        try:         
            fn_uid = validated_data.pop('fn')
        except:
            fn_uid = None    
        instance = KKT.objects.create(**validated_data)
        try:
            customer = Customer.objects.get(uid=customer_uid.get('uid'))
        except:
            customer = None

        try:
            point_of_sale = Point_of_sale.objects.get(uid=point_of_sale_uid.get('uid'))
        except:
            point_of_sale = None

        try:
            fn = FN.objects.get(uid=fn_uid.get('uid'))
        except:
            fn = None        

        instance.customer = customer
        instance.point_of_sale = point_of_sale
        instance.fn = fn
        instance.save()
        return instance

    def update(self, instance, validated_data):
        try:
            customer_uid = validated_data.pop('customer')
        except:
            customer_uid = None
        try:       
            point_of_sale_uid = validated_data.pop('point_of_sale')
        except:
            point_of_sale_uid = None
        try:         
            fn_uid = validated_data.pop('fn')
        except:
            fn_uid = None
        instance = super().update(instance, validated_data)
        try:
            customer = Customer.objects.get(uid=customer_uid.get('uid'))
        except:
            customer = None

        try:
            point_of_sale = Point_of_sale.objects.get(uid=point_of_sale_uid.get('uid'))
        except:
            point_of_sale = None

        try:
            fn = FN.objects.get(uid=fn_uid.get('uid'))
        except:
            fn = None

        instance.customer = customer
        instance.point_of_sale = point_of_sale
        instance.fn = fn
        
        instance.save()
        return instance 