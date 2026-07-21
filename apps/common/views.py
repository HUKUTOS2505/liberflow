from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health(request):
    """Confirm that the Django process can serve HTTP requests."""
    return JsonResponse({"status": "ok"})
