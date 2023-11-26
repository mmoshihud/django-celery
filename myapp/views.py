import pandas as pd
from django.shortcuts import render, redirect

from myapp.form import UploadFileForm
from myapp.models import ExcelData


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the Excel file using pandas
            excel_file = request.FILES["file"]
            df = pd.read_excel(excel_file)

            # Loop through the DataFrame and save each row to the database
            for index, row in df.iterrows():
                ExcelData.objects.create(
                    name=row["name"],
                    designation=row["designation"],
                )

            return redirect("/")
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form})
