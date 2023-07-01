from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.coronavstech.companies.models import Company
from api.coronavstech.companies.serializers import CompanySerializer
from fibonacci.dynamic import fibonacci_dynamic


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    """
    sends email with request payload
    sender: stanislav.osipov89@gmail.com
    reciever: badlolpro@gmail.com
    """
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="stanislav.osipov89@gmail.com",
        recipient_list=["badlolpro@gmail.com"],
    )
    return Response(
        {"status": "success", "info": "email sent successfully"}, status=200
    )


@api_view(http_method_names=["GET"])
def get_fibonacci(request: Request) -> Response:
    try:
        n = int(request.GET.get('n', ''))
    except (TypeError, ValueError):
        return Response(
            {"error": "n must be an integer"}, status=400
        )

    if n < 0:
        return Response(
            {"error": "n must be non-negative"}, status=400
        )

    result = fibonacci_dynamic(n)
    return Response({"fibonacci": result}, status=200)