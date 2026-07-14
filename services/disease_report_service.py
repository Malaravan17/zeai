from sqlalchemy.orm import Session
from models.disease_report import DiseaseReport

from schemas import DiseaseReportCreate


def add_report(db: Session, report: DiseaseReportCreate):

    new_report = DiseaseReport(
        farm_id=report.farm_id,
        crop_name=report.crop_name,
        image_path=report.image_path,
        disease_name=report.disease_name,
        confidence=report.confidence,
        report_date=report.report_date
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report


def get_all_reports(db: Session):

    reports = db.query(DiseaseReport).all()

    return reports


def get_report(db: Session, report_id: int):

    report = db.query(DiseaseReport).filter(
        DiseaseReport.id == report_id
    ).first()

    return report


def delete_report(db: Session, report_id: int):

    report = db.query(DiseaseReport).filter(
        DiseaseReport.id == report_id
    ).first()

    db.delete(report)
    db.commit()

    return {
        "message": "Report Deleted Successfully"
    }