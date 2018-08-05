# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/5 19:34'

from rest_framework import serializers
from ..models import Tag,Subcomment,Comment,Article
from users.models import UserProfile

class AuthorSerializer(serializers.ModelSerializer):
    """
    文章作者序列化serializer
    """
    avatar_url=serializers.SerializerMethodField()
    class Meta:
        model=UserProfile
        fields=('id','username','avatar','avatar_url')

    def get_avatar_url(self,user):
        if user.socialaccount_set.count():
            return user.socialaccount_set.all()[0].get_avatar_url()
        return ""


class TagListSerializer(serializers.ModelSerializer):
    """
    标签list
    """
    class Meta:
        model=Tag
        fields="__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    """
    文章list
    """
    #author=serializers.HyperlinkedRelatedField(view_name="users_v1-detail",read_only=True)
    author=AuthorSerializer()
    tags=TagListSerializer(many=True)
    comment_count=serializers.SerializerMethodField()
    class Meta:
        model = Article
        exclude = ("content",)

    #获取评论总数
    def get_comment_count(self,article):
        sub_count=0
        for comment in article.comments.all():
            sub_count+=comment.sub_comments.count()
        return article.comments.count()+sub_count

class SubCommentListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    reply_to=AuthorSerializer()
    class Meta:
        model=Subcomment
        fields="__all__"

class CommentListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    sub_comments=SubCommentListSerializer(many=True)
    class Meta:
        model=Comment
        fields="__all__"


class TagDetailSerializer(serializers.ModelSerializer):
    """
    文章retrieve
    """
    articles=ArticleListSerializer(many=True)
    class Meta:
        model=Tag
        fields="__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    文章retrieve
    """
    author=AuthorSerializer()
    tags=TagListSerializer(many=True)
    comments=CommentListSerializer(many=True)
    class Meta:
        model = Article
        fields = "__all__"

