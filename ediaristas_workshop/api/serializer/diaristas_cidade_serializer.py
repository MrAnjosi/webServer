from rest_framework import serializers
from web.models import Diaristas

import random

class DiaristaCidadeSerializer(serializers.ModelSerializer):
    # pode poder um metodo de retorno sem a existencia do mesmo no banco ou outro local
    reputacao = serializers.SerializerMethodField()
    class Meta:
        model = Diaristas
        fields = ('nome_completo', 'foto_usuario', 'cidade', 'reputacao')


    def get_reputacao(self, obj):
        return random.randint(0, 5)