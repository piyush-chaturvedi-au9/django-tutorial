from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html', {'company_name': 'Freelancer'})

def contact(request):
    # data = json.loads(request.body)
    # print(json.loads('{"name": "Arkesh"}'))
    # print(data)
    contact = Contact(
        name = request.POST["name"],
        email = request.POST["email"],
        phone = request.POST["phone"],
        message = request.POST["message"],
        picture = request.FILES['picture']
    )
    contact.save()
    return JsonResponse({
        'success': True,
        'message': 'Your query has been recorded. We will get in touch with you shortly.',
    }, json_dumps_params={'indent': 2})