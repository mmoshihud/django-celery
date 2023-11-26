from celery import shared_task


@shared_task
def process_excel_file(file_name, file_content):
    """"""
