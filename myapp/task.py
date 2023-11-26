from time import sleep

from celery import shared_task
import pandas as pd

from myapp.models import ExcelData


@shared_task
def add(x, y):
    return x + y


@shared_task
def process_excel_data(file_content):
    df = pd.read_excel(file_content)

    for index, row in df.iterrows():
        ExcelData.objects.create(
            name=row["name"],
            designation=row["designation"],
        )
