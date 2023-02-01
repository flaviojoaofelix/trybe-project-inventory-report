from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

from tests.product_report.test_product_report import MockProductReport
from tests.product.test_product import product_mock


class MockReport(MockProductReport):
    def __init__(self, mocked_product):
        super().__init__(mocked_product)
        self.color_blue = "\033[36m"
        self.color_green = "\033[32m"
        self.color_red = "\033[31m"
        self.color_end = "\033[0m"

    def get_mocked_list(self):
        mocked_list = [
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

        return mocked_list

    def __repr__(self):
        return (
            f"{self.color_green}Data de fabricação mais antiga:{self.color_end} {self.color_blue}{self.manufacturing_date}{self.color_end}\n"
            f"{self.color_green}Data de validade mais próxima:{self.color_end} {self.color_blue}{self.expiration_date}{self.color_end}\n"
            f"{self.color_green}Empresa com mais produtos:{self.color_end} {self.color_red}{self.company_name}{self.color_end}"
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
