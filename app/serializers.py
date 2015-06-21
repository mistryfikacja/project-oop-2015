from rest_framework import serializers
import models

class serializer_wpisu(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.wpis
		fields = ('id', 'tytul', 'tresc', 'data')

class serializer_wpisu_pro(serializers.HyperlinkedModelSerializer):
	dodal = serializers.PrimaryKeyRelatedField(
		read_only=True, allow_null=True, default='0')
	def validate_dodal(self,value):
		return self.context['request'].user
		
	class Meta:
		model = models.wpis_pro
		fields = ('id', 'tytul', 'tresc', 'data', 'dodal')
