from .models import Cheese
from rest_framework import serializers

## Class TodoSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the TodoSerializer class.
    class Meta:
        # model to serialize
        model = Cheese
        # fields to show in json
        fields = ('name', 'origin_country', 'type')