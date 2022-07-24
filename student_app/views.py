from django.shortcuts import render, redirect
from django.views import View
from student_app.models import StudentDetails


class AddDetails(View):
    def get(self, request):
        return render(request, "student_app/index.html")

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        tamil = request.POST['tamil']
        english = request.POST['english']
        maths = request.POST['maths']
        science = request.POST['science']
        social = request.POST['social']

        # total and avg calculation
        total = int(tamil)+int(english)+int(maths)+int(science)+int(social)
        average = total/5
        marks = [int(tamil),int(english),int(maths),int(science),int(social)]
    
        pass_fail = None
        for x in marks:
            if x < 35:
                pass_fail = "F"
            else:
                pass_fail = "P"
        grade = None

        print(type(tamil), tamil, total, average, "pass or fail", pass_fail)


        return redirect("add")
    
  

class Details(View):
    def get(self, request):
        return render(request, "student_app/details.html")