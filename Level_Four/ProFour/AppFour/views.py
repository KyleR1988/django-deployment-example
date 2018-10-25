from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello world!', 'number':100}
    return render(request,'AppFour/index.html', context_dict)

def other(request):
    return render(request,'AppFour/other.html')

def relative_url_templates(request):
    return render(request,'AppFour/relative_url_templates.html')
