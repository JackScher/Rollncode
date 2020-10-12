from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer, UserSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = BookSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
