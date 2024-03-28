from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions


@permission_classes([permissions.AllowAny])
class IndexView(APIView):
    """API Index View"""

    def get_base_url(self, request):
        scheme = request.scheme  # 'http' or 'https'
        host = (
            request.get_host()
        )  # 'netrobase.com' or 'localhost:8000' or retailer_domain

        # Constructing the base URL
        base_url = f"{scheme}://{host}"
        return base_url

    def get(self, request):
        base_url = self.get_base_url(request)
        content = {
            "message": "Welcome to Quimer API!",
            "api_endpoints": f"{base_url}/api/",
            "api_admin": f"{base_url}/admin/",
            "api_graphql": f"{base_url}/graphql/",
            "api_credentials": "An admin sample credential is provided in the api_docs",
            "api_usage": "Reference the api_docs for more information on the API Usage",
            "api_docs": "https://docs.netrobase.dev/quimer-docs/",
        }
        return Response(content)
