from django.shortcuts import render, redirect
from .models import Collage

def form(request):
    if request.method == "POST":
        fn = request.POST.get("Fullname")
        eml = request.POST.get("Email")
        phn = request.POST.get("Phone_number")
        dob = request.POST.get("Birthdate")
        gn = request.POST.get("Gender")
        hs = request.POST.get("High_school")
        esy = request.POST.get("Essay")
        images = request.FILES.get("image")

        print(fn, eml, phn, dob, gn, hs, esy, images.name)
        data = Collage(Fullname=fn,
                       Email=eml,
                       Phone_number=phn,
                       Birthdate=dob,
                       Gender=gn,
                       High_school=hs,
                       Essay=esy,
                       img=images)
        data.save()
        return render(request, 'collage.html', context={'Fullname': fn,
                                                        'Email': eml,
                                                        'Phone_number': phn,
                                                        'Birthdate': dob,
                                                        'Gender': gn,
                                                        'High_school': hs,
                                                        'Essay': esy,
                                                        'image': images})
    return render(request, 'collage.html')

def table(request):
    data = Collage.objects.all()
    return render(request, 'table.html', context={'data': data})

def edit(request, id):
    data = Collage.objects.get(id=id)
    if request.method == "POST":
        data.Fullname = request.POST.get("Fullname")
        data.Email = request.POST.get("Email")
        data.Phone_number = request.POST.get("Phone_number")
        data.Birthdate = request.POST.get("Birthdate")
        data.Gender = request.POST.get("Gender")
        data.High_school = request.POST.get("High_school")
        data.Essay = request.POST.get("Essay")
        data.img = request.FILES.get("image")
        data.save()
        return redirect('table')
    return render(request, 'edit.html', context={'data': data})

def delete(request, id):
    Collage.objects.get(id=id).delete()
    data = Collage.objects.all()
    return redirect('table')
