from django.shortcuts import render
from .models import Category, Image, Location
# from django.views.generic import TemplateView, View
# from django.core import serializers
# from django.http import JsonResponse


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'photos/results.html', {"message": message, "images": searched_images})
    else:
        message = ""
        return render(request, 'photos/results.html', {"message": message})



def gallery(request):
    category = request.GET.get('category')
    if category == None:
       photos = Image.objects.all()    
    else:
        photos = Image.objects.filter(category__name=category)

    categories = Category.objects.all()
    
    location = Location.objects.all()
    context = {'categories': categories, 'photos': photos, 'location': location}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Image.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


# end of function

# classes
# class HomeView(TemplateView):
#     template_name = 'photos/galery.html'

# class PictureView(View):
#     def get(self, request):
#         qs = Image.objects.all()
#         data = serializers.serialize('json', qs)
#         return JsonResponse({'data':data}, safe=False)