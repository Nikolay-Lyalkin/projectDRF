import re
from rest_framework import serializers


class NumCharactersValidator:

    def __init__(self, fields):
        self.fields = fields


    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9\.\-\ ]+$')
        tmp_value = dict(value).get(self.fields)
        print(tmp_value)
        if len(tmp_value) > 6:
            raise serializers.ValidationError("Количество символов превышает макисмально допустимое значение!")
        if not bool(reg.match(tmp_value)):
            raise serializers.ValidationError("Необходимо заменить символы")
