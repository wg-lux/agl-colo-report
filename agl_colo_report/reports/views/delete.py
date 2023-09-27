## views/delete.py

from django.http import JsonResponse
from django.urls import reverse
from ..models import Patient, Report # models to delete
from ..models import  (
    # verify that all associated models are imported
    ColonPolyp,
    ColonPolypLocation,
    Premedication,
    DrugApplication,
)

from logger.write import get_custom_logger

# import django settings
from django.conf import settings

def delete_report(request, report_id):
    """
    Delete a specific report.
    Redirect to homepage after deletion is complete.
    """

    log_dir = settings.LOG_DIR
    logger = get_custom_logger(
        "function_call",
        "delete_report", 
        log_dir=log_dir,
        include_date=False,
        overwrite=True,
    )

    logger.info(f"Starting to delete report with id {report_id}")

    # Delete report with specific id
    Report.objects.get(id=report_id).delete()

    # Verify that report is deleted
    logger.info("Verifying that report is deleted")
    assert Report.objects.filter(id=report_id).count() == 0
    logger.info("Report deleted")

    # Verify that all associated models are deleted
    logger.info("Verifying that all associated models are deleted")
    assert ColonPolyp.objects.filter(report_id=report_id).count() == 0
    assert Premedication.objects.filter(report_id=report_id).count() == 0


    return JsonResponse({"status": "success"})

def delete_all_entries(request):
    """
    Delete all entries in specific models.
    Redirect to homepage after deletion is complete.
    """

    log_dir = settings.LOG_DIR
    logger = get_custom_logger(
        "function_call",
        "delete_all_entries", 
        log_dir=log_dir,
        include_date=False,
        overwrite=True,
    )

    logger.info("Starting to delete all entries in Patient, Report")

    # Delete all entries in Model1 and Model2
    Patient.objects.all().delete()
    Report.objects.all().delete()

    # Verify that all entries are deleted
    logger.info("Verifying that all entries are deleted")
    assert Patient.objects.count() == 0
    logger.info("Patient entries deleted")
    assert Report.objects.count() == 0
    logger.info("Report entries deleted")
    assert ColonPolyp.objects.count() == 0
    logger.info("ColonPolyp entries deleted")
    assert ColonPolypLocation.objects.count() == 0
    logger.info("ColonPolypLocation entries deleted")
    assert Premedication.objects.count() == 0
    logger.info("Premedication entries deleted")
    assert DrugApplication.objects.count() == 0
    logger.info("DrugApplication entries deleted")

    logger.info("All entries deleted")

    return JsonResponse({"status": "success"})

