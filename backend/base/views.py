from rest_framework.response import Response
from django.shortcuts import render
from base.models import Book
from base.serializers import BookSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username
        token['superuser?'] = user.is_superuser
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	return Response("im protected")




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def books_currentuser(req):
    if req.method =='GET':
        user= req.user
        temp_task=user.book_set.all()
        return Response (BookSerializer(temp_task,many=True).data)







@api_view(['GET'])
def index(request):
    return Response('hello')



@api_view(['GET','POST','DELETE','PUT','PATCH'])
def books(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_book=Book.objects.get(id=id)
                return Response (BookSerializer(temp_book,many=False).data)
            except Book.DoesNotExist:
                return Response ("not found")
        all_books=BookSerializer(Book.objects.all(),many=True).data
        return Response ( all_books)
    if req.method == 'POST':
        # Ensure the request is made by an authenticated user
        if not req.user.is_authenticated:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        
        # Assign the user ID to the book being created
        # req.data['user'] = req.user.id

        # ser = BookSerializer(data=req.data)
        ser = BookSerializer(data=req.data, context={'user': req.user})
        if ser.is_valid():
            ser.save()
            return Response("posted")
        else:
            return Response(ser.errors)
    if req.method =='DELETE':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_book.delete()
        return Response ("deleted")
    if req.method =='PUT':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")

        ser = BookSerializer(data=req.data)

        if ser.is_valid():
            ser.update(temp_book, req.data)
            serialized_data = ser.data
            return Response(serialized_data)
        else:
            return Response(ser.errors)



# register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")