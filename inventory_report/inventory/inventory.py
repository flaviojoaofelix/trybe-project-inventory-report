from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, type: str):
        if file_path.endswith(".csv"):
            data_list = CsvImporter.import_data(file_path)

        return (
            CompleteReport.generate(data_list)
            if type == "completo"
            else SimpleReport.generate(data_list)
        )
