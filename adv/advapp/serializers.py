from rest_framework import serializers
from .models import Advertisement


class QueryFieldsMixin(object):

    include_arg_name = 'fields'
    delimiter = ','

    def __init__(self, *args, **kwargs):
        super(QueryFieldsMixin, self).__init__(*args, **kwargs)

        try:
            request = self.context['request']
            method = request.method
        except (AttributeError, TypeError, KeyError):
            return

        if method != 'GET':
            return

        try:
            query_params = request.query_params
        except AttributeError:
            pass

        includes = query_params.getlist(self.include_arg_name)
        include_field_names = {
            name for names in includes
            for name in names.split(self.delimiter) if name
            }

        if not include_field_names:
            fields_to_drop = [
                'id', 'description', 'created', 'link_2', 'link_3'
                ]
        else:
            serializer_field_names = set(self.fields)
            fields_to_drop = serializer_field_names - include_field_names

        for field in fields_to_drop:
            self.fields.pop(field)


class AdSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
