from rest_framework.serializers import ModelSerializer
from api.models import Category, Entry


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = '__all__'
