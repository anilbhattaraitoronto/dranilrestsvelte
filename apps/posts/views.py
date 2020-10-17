from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tag, Category, Post
from .serializers import PostSerializer, TagSerializer, CategorySerializer
from django.http import HttpResponse


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        categories = Category.objects.all()
        posts = Post.objects.filter(archived=False)[:30]
        tag_serializer = TagSerializer(tags, many=True)
        category_serializer = CategorySerializer(categories, many=True)
        product_serializer = PostSerializer(posts, many=True)
        data = [tag_serializer.data,
                category_serializer.data, product_serializer.data]
        return Response(data)
    return HttpResponse('You are not authorized to post. Sorry')
    # if request.method == 'POST':
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
