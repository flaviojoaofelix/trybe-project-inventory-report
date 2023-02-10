from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

from tests.product_report.test_product_report import MockProductReport
from tests.product.test_product import product_mock


class MockReport(MockProductReport):
    def __init__(self, mocked_product):
        super().__init__(mocked_product)
        self.cb = "\033[36m"
        self.cg = "\033[32m"
        self.cr = "\033[31m"
        self.ce = "\033[0m"

    def get_mocked_list(self):
        return [
            {
                "id": self.product_id,
                "nome_do_produto": self.product_name,
                "nome_da_empresa": self.company_name,
                "data_de_fabricacao": self.manufacturing_date,
                "data_de_validade": self.expiration_date,
                "numero_de_serie": self.serial_number,
                "instrucoes_de_armazenamento": self.storage_instructions,
            }
        ]

    def __repr__(self):
        return (
            f"{self.cg}Data de fabricação mais antiga:{self.ce} "
            f"{self.cb}{self.manufacturing_date}{self.ce}\n"
            f"{self.cg}Data de validade mais próxima:{self.ce} "
            f"{self.cb}{self.expiration_date}{self.ce}\n"
            f"{self.cg}Empresa com mais produtos:{self.ce} "
            f"{self.cr}{self.company_name}{self.ce}"
        )


def test_decorar_relatorio():
    mock = MockReport(product_mock)

    simple_report = ColoredReport(SimpleReport).generate(
        mock.get_mocked_list()
    )
    complete_report = ColoredReport(CompleteReport).generate(
        mock.get_mocked_list()
    )

    assert str(mock.__repr__()) in simple_report
    assert str(mock.__repr__()) in complete_report
