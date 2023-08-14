from Book.models import Book
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.response import Response


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'description', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if title.isdigit():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )
        
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )
        
        return data
    
    def validate_price(self, price):
        if price > 0:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )