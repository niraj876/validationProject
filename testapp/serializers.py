from rest_framework import serializers
from .models import StudentModel


#  validators level validation
def start_with_n(value):
    if value[0].lower() != 'n':
        raise serializers.ValidationError('Name must be started with N')


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_n])
    roll = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    # # field level validation
    # # This method is automatically invoked, when is_valid() method is called
    # def validate_roll(self, value):
    #     # print(value)
    #     # print(type(value))
    #     if value >= 1000:
    #         raise serializers.ValidationError('seats full')
    #     return value

    # #  Object level validation
    # #  data is a python dictinary of field value
    # def validate(self, data):
    #     name = data.get('name')
    #     roll = data.get('roll')
    #     email = data.get('email')
    #
    #     if name.lower() =='niraj' and roll != 42 :
    #         raise serializers.ValidationError('roll must be 42')
    #     return data

