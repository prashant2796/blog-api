from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)
from posts.models import Post


class PostCreateUpdateAPIView(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			#'id',
			'title',
			#'slug',
			'content',
			'publish',

		]

class PostDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	html = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
			'id',
			'user',
			'title',
			'slug',
			'content',
			'html',
			'publish',
			'image'

		]
	def get_html(self,obj):			
		return obj.get_markdown()

	def get_user(self,obj):
		return str(obj.user.username)

	def get_image(self,obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image
		



class PostListSerializer(ModelSerializer):
	user = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='slug'
		)
	
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish',

		]

	def get_user(self,obj):
		return str(obj.user.username)

