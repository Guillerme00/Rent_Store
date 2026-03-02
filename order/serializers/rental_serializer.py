from rest_framework import serializers
from ..models import RentalModel

class RentSerializer(serializers.Serializer):
    class Meta:
        model = RentalModel
        fields = "__all__"