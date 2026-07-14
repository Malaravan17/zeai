from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import DiseaseReportCreate
from services import disease_report_service
from database.database import get_db

router = APIRouter()


@router.post("/disease-reports")
def create_report(report: DiseaseReportCreate,
                  db: Session = Depends(get_db)):
    return disease_report_service.add_report(db, report)


@router.get("/disease-reports")
def get_all_reports(db: Session = Depends(get_db)):
    return disease_report_service.get_all_reports(db)


@router.get("/disease-reports/{report_id}")
def get_report(report_id: int,
               db: Session = Depends(get_db)):
    return disease_report_service.get_report(db, report_id)


@router.delete("/disease-reports/{report_id}")
def delete_report(report_id: int,
                  db: Session = Depends(get_db)):
    return disease_report_service.delete_report(db, report_id)