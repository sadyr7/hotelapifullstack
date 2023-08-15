from rest_framework import serializers
from restourant.models import Category_restourant, Product, Like

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category_restourant
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        product = attrs['product']
        if user.likes.filter(product=product).exists():
            raise serializers.ValidationError(
                'you have already liked this product!'
            )
        return attrs


class LikedUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['user', 'user_username']