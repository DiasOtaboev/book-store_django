from rest_framework.serializers import ModelSerializer

from store.models import Book


class BooksSerializer(ModelSerializer): #Создаем сериализатор с родительским классом ModelSerialiazer он будет использоваться во view
    class Meta:
        model = Book
        fields = '__all__'
