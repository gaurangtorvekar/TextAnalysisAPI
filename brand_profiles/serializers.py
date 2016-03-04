from django.forms import widgets
from rest_framework import serializers
from models import Reviews, Brand_Identities
from django.contrib.auth.models import User, Group

class Brand_IdentitiesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Brand_Identities
		fields = ('name', 'website', 'email', 'contact_number', 'address', 'city', 'country', )

class ReviewsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Reviews
		fields = ('brand', 'review', 'sentiment_score')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
