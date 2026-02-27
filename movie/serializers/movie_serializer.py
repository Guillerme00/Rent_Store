from rest_framework import serializers
from ..models import Movie

class MovieSerializer(serializers.ModelSerializer):
    def validate_release_year(self, value):
        if value < 1888 or value > 2100:
            raise serializers.ValidationError("Invalid Release Year")
        return value
    
    class Meta:
        model = Movie
        fields = "__all__"