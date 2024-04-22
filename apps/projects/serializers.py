from rest_framework import serializers
from .models import Project, Task, Comment
from datetime import datetime

from pytz import timezone

class ProjectSerializerModel(serializers.ModelSerializer):
    def validate_name(self,value):
        if "sair" in value:
            raise serializers.ValidationError("El nombre sair no puede estar en el nombre del proyecto")
        return value
    class Meta:
        model=Project
        fields="__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    
    def validate_content(self,value):
        groserias = ["puto","imbecil","cabron","te amo"]
    
        for groseria in groserias:
            if groseria in value:
                raise serializers.ValidationError("Se encontró lenguaje inapropiado.")
        return value
    
    class Meta:
        model=Comment
        fields="__all__"
   

class ProjectSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=60)
    init_date=serializers.DateTimeField(required=False)
    end_date=serializers.DateTimeField()

    def validate_name(self,value):
        if "sair" in value:
            raise serializers.ValidationError("El nombre sair no puede estar en el nombre del proyecto")
        return value

    def validate(self, attrs):
        """ Investigar
        
            if attrs.get("end_date").replace()<datetime.now(tzinfo=timezone('UTC')):
            raise serializers.ValidationError("La fecha final debe ser mayor que la fecha inicial") """
        return super().validate(attrs)
    
    def create(self, validated_data):
        Project(**validated_data).save()
        return self.data