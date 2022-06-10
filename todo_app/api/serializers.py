from rest_framework import serializers
from todo_app.models import  todo_list


class todo_listSerializer(serializers.ModelSerializer):
    class Meta():
        model = todo_list
        fields = ['title','category','created']