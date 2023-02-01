# # from inventory_report.reports.report import Report
from inventory_report.reports.handle_report_data import HandleReportData
from inventory_report.reports.print_report import PrintReport


class SimpleReport:
    @staticmethod
    def generate(products: list):
        data = HandleReportData(products)
        report = PrintReport(data, False)

        return report.print()
