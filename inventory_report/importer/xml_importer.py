# Reference:
# https://www.digitalocean.com/community/tutorials/python-xml-to-json-dict

from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path: str):
        if file_path.endswith(".xml"):
            with open(file_path) as file:
                file_data = file.read()
                data_list = xmltodict.parse(file_data)

            return data_list["dataset"]["record"]

        else:
            raise ValueError("O arquivo não é .xml")
