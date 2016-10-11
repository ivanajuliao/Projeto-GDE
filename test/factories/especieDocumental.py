import factory
from app.models import EspecieDocumental

class EspecieDocumentalFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = EspecieDocumental
		django_get_or_create = ('nome',)

	nome = 'especieDocumentalTeste'
