from rest_framework import renderers
import json

class GeoJSONRenderer(renderers.BaseRenderer):
    media_type = 'application/json'
    format = 'geojson'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        results = data.get("results", [])

        geo_fields = {}

        try:
            geo_fields = renderer_context["view"].geo_fields
        except AttributeError:
            pass

        for kind, fields in geo_fields.items():
            print(kind, fields)
            for result in results:
                for field in fields:
                    if field in result:
                        result[field] = float(result[field])

        return json.dumps(data)
