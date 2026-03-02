from rest_framework import serializers
from ..models import RentalModel

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalModel
        fields = "__all__"