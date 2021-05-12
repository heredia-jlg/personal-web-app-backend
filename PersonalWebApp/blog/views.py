from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from datetime import datetime as date

# Create your views here.

class PostList(APIView):
    def get(self, request):
        print('in get request function')
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['date'] = str(date.today().strftime("%B %d, %Y"))
        print('in post request function :' + str(request.data) )
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Valid")
        else:
            print("Not valid" + str(serializer.errors))
        return Response(serializer.data)