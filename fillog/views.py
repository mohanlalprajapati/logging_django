from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    try:
        1/0
    except:
        logger.warning("My Mesagge",exc_info=True)
    return HttpResponse("Hello, world. You're at the polls index.")
