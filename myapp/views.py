from django.shortcuts import render, redirect

from myapp.form import UploadFileForm
from myapp.models import ExcelData
from myapp.task import process_excel_data, add
from celery.result import AsyncResult


def home(request):
    return render(request, "home.html")


def about(request):
    result = add.delay(10, 20)
    return render(request, "about.html", {"result": result})


def check_result(request, task_id):
    result = AsyncResult(task_id)
    return render(request, "result.html", {"result": result})


def contact(request):
    return render(request, "contact.html")


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the Excel file using pandas
            excel_file = request.FILES["file"]

            file_path = "C:\\Temp\\{}".format(excel_file.name)
            with open(file_path, "wb") as destination:
                for chunk in excel_file.chunks():
                    destination.write(chunk)

            process_excel_data.delay(file_path)

            return redirect("/")
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form})
