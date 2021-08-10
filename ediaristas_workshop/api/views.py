from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import diaristas_cidade_serializer
from .service.cidade_atendimento import listar_diaristas_cidade
from .pagination import diaristas_cidade_pagination
# Create your views here.

class DiaristasCidadeList(APIView, diaristas_cidade_pagination.DiaristasCidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        diaristas = listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas, request)
        # many quer dizer que vai trazer todos os dados
        serializer = diaristas_cidade_serializer.DiaristaCidadeSerializer(resultado, many=True, context={'request':request})

        return self.get_paginated_response(serializer.data)

