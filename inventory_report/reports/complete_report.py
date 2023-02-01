from inventory_report.reports.utils_report import HandleReportData, PrintReport


class CompleteReport:
    @staticmethod
    def generate(products: list):
        data = HandleReportData(products)
        report = PrintReport(data, True)

        return report.print()
