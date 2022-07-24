from django.shortcuts import render, redirect
from django.views import View
from student_app.models import StudentDetails


class AddDetails(View):
    def get(self, request):
        return render(request, "student_app/index.html")

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        tamil = int(request.POST['tamil'])
        english = int(request.POST['english'])
        maths = int(request.POST['maths'])
        science = int(request.POST['science'])
        social = int(request.POST['social'])

        # total and avg calculation
        total = tamil + english + maths + science + social
        average = total/5
    
        #pass or fail
        pass_fail = None

        if tamil < 35:
            pass_fail = "F"
        elif english < 35:
            pass_fail = "F"
        elif maths < 35:
            pass_fail = "F"
        elif science < 35:
            pass_fail = "F"
        elif social <35:
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
        data = StudentDetails.objects.get(id=id)
        return render(request, "student_app/update.html", {'data':data})
    def post(self, request, id):
        name = request.POST['name']
        email = request.POST['email']
        tamil = int(request.POST['tamil'])
        english = int(request.POST['english'])
        maths = int(request.POST['maths'])
        science = int(request.POST['science'])
        social = int(request.POST['social'])

        
         # total and avg calculation
        total = tamil + english + maths + science + social
        average = total/5
    
        #pass or fail
        pass_fail = None

        if tamil < 35:
            pass_fail = "F"
        elif english < 35:
            pass_fail = "F"
        elif maths < 35:
            pass_fail = "F"
        elif science < 35:
            pass_fail = "F"
        elif social <35:
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

        data = StudentDetails.objects.get(id=id)
        data.name = name
        data.email = email
        data.tamil = tamil
        data.english = english
        data.maths = maths
        data.science = science
        data.social = social
        data.total = total
        data.average = average
        data.pass_fail = pass_fail
        data.grade = grade

        data.save()

        return redirect("details")


def delete(request, id):
    data = StudentDetails.objects.get(id=id)
    data.delete()
    return redirect("details")

