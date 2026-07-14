from schemas import DiseaseReportCreate


def add_report(report: DiseaseReportCreate):

    return {
        "message": "Disease Report Added",
        "report": report
    }


def get_all_reports():

    return {
        "message": "All Disease Reports",
        "data": []
    }


def get_report(report_id: int):

    return {
        "message": "Disease Report Found",
        "report_id": report_id
    }


def delete_report(report_id: int):

    return {
        "message": "Disease Report Deleted",
        "report_id": report_id
    }