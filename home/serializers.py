from rest_framework import fields, serializers
from .models import BookEntry


class BookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookEntry
        fields = ['id', 'name', 'book','author', 'desc', 'date' ]
        

# This is the serializer class this will converting complex data such as querysets
# and modelto native phythin data types. that can 
# easily rendered intiO JSON