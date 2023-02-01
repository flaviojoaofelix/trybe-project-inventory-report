# # from inventory_report.reports.report import Report
from inventory_report.reports.utils_report import HandleReportData, PrintReport


class SimpleReport:
    @staticmethod
    def generate(products: list):
        data = HandleReportData(products)
        report = PrintReport(data, False)

        return report.print()
