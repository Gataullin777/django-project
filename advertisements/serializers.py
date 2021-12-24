from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        print()
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        print()
        return super().create(validated_data)




    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        method_request = self.context['request'].stream.method
        user_name = self.context['request'].user

        user_ads = Advertisement.objects.filter(creator=user_name, status='OPEN')

        print()
        if method_request == 'POST':

            if len(user_ads) >= 10:
                raise ValidationError('you must not have more than 10 open ads, close some advertisements')

        elif method_request == 'PATCH':
            creater = self.instance.creator

            if user_name != creater:
                raise ValidationError('update and delete advertisement can only the author !!!!')

            if len(user_ads) >= 10:
                raise ValidationError('you must not have more than 10 open ads, close some advertisements')

        return data










