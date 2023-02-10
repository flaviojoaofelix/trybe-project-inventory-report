from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path: str, report_type: str):
        if file_path.endswith(".csv"):
            data_list = CsvImporter.import_data(file_path)

        elif file_path.endswith(".json"):
            data_list = JsonImporter.import_data(file_path)

        elif file_path.endswith(".xml"):
            data_list = XmlImporter.import_data(file_path)

        else:
            raise ValueError("Arquivo inválido")

        return cls.get_report(data_list, report_type)

    def get_report(self, report_type: str):
        if report_type == "completo":
            report = CompleteReport.generate(self)

        elif report_type == "simples":
            report = SimpleReport.generate(self)

        else:
            raise ValueError("Tipo de relatório desconhecido")

        return report
