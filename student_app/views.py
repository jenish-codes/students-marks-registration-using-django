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
    
        #pass or fail
        pass_fail = None

        if int(tamil) < 35 or int(english) < 35 or int(maths) < 35 or int(science) < 35 or int(social):
            pass_fail = "F"
        else:
            pass_fail = "P"


        # grade
        grade = None
        if pass_fail == "P":
            if average >= 95:
                grade = "O+"
            elif average >= 90:
                grade = "O"
            elif average >= 80:
                grade = "A+"
            elif average >= 70:
                grade = "A"
            elif average >= 60:
                grade = "B+"
            elif average >= 50:
                grade = "B"
            elif average >= 35:
                grade = "c"
        else:
            grade = "RA"

        details = StudentDetails(
            name = name,
            email = email,
            tamil = tamil,
            english=english,
            maths=maths,
            science=science,
            social=social,
            total=total,
            average=average,
            pass_fail=pass_fail,
            grade=grade
        )
        details.save()
        return redirect("add")
    
  

class Details(View):
    def get(self, request):
        details = StudentDetails.objects.all()
        return render(request, "student_app/details.html", {'details':details})

class Update(View):
    def get(self, request, id):
        return render(request, "student_app/update.html")
    


def delete(request, id):
    data = StudentDetails.objects.get(id=id)
    data.delete()
    return redirect("details")

