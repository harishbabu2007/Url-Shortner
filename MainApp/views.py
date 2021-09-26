from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Urls

# Create your views here.
def index(request):
  params = {
    'messages' : "",
    'error' : False
  }
  
  if request.method == 'POST':
    url = request.POST.get('url')
    short_name = request.POST.get('name')

    try:
      Urls.objects.get(slug_shortcut=short_name)
      params['messages'] = "The short name already exist try another name" 
      params['error'] = True
    except:
      short_name_url = slugify(short_name, allow_unicode=True)

      data = Urls(
        site_url = url,
        slug_shortcut = short_name,
        slug_url = short_name_url
      )

      data.save()
      params['messages'] = "Success! url created"
      params['url'] = url
      params['url_name'] = short_name_url
  return render(request, "main/index.html", params)


def redirection(request, url_slug):
  try:
    a = Urls.objects.get(slug_url=url_slug)
    return redirect(a.site_url)
  except:
    return render(request, "main/404.html")