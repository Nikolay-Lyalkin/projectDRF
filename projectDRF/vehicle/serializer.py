from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Car, Moto, Milage
from .service import convert_rub_in_usd
from .validators import NumCharactersValidator


# class NumCharactersValidator:
#     def __call__(self, value):
#         if len(value) > 6:
#             raise serializers.ValidationError("Количество символов превышает макисмально допустимое значение!")


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    milage = MilageSerializer(many=True, read_only=True)
    usd_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_usd_price(self, instance):
        return convert_rub_in_usd(instance.amount)


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True, required=False)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [
            NumCharactersValidator(fields='title'),
            UniqueTogetherValidator(
                queryset=Moto.objects.all(),# Выборка данных, для которых будет применяться валидация
                fields=['title',]# Определение поля для валидации
            )
        ]

    def create(self, validated_data):

        key = [key for key in validated_data.keys()]
        if "milage" in key:

            milage = validated_data.pop('milage')
            moto = Moto.objects.create(**validated_data)
            for m in milage:
                Milage.objects.create(**m, moto=moto)
            return moto

        moto = Moto.objects.create(**validated_data)
        return moto
