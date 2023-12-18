from rest_framework import serializers

from apps.categories.models import Catigory

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigory
        fields = "__all__"
