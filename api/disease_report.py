from fastapi import APIRouter
from schemas import DiseaseReportCreate
from services import disease_report_service

router = APIRouter()


@router.post("/disease-reports")
def create_report(report: DiseaseReportCreate):
    return disease_report_service.add_report(report)


@router.get("/disease-reports")
def get_all_reports():
    return disease_report_service.get_all_reports()


@router.get("/disease-reports/{report_id}")
def get_report(report_id: int):
    return disease_report_service.get_report(report_id)


@router.delete("/disease-reports/{report_id}")
def delete_report(report_id: int):
    return disease_report_service.delete_report(report_id)