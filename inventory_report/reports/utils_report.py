from collections import defaultdict


class HandleReportData:
    def __init__(self, products: list):
        self.products = products
        self.manufacturing_dates = []
        self.expiration_dates = []
        self.companies_stock = defaultdict(int)

        self.handle_data()

    def handle_data(self):
        for product in self.products:
            self.manufacturing_dates.append(product["data_de_fabricacao"])
            self.expiration_dates.append(product["data_de_validade"])
            company = product["nome_da_empresa"]
            self.companies_stock[company] += 1

    def oldest_date(self):
        return min(self.manufacturing_dates)

    def closest_date(self):
        return min(self.expiration_dates)

    def company_bigger_stock(self):
        return max(self.companies_stock, key=self.companies_stock.get)

    def companies_stock(self):
        return self.companies_stock

    def companies_stock_list(self):
        companies = self.companies_stock
        companies_stock = ""

        for company in companies:
            companies_stock += f"- {company}: {companies[company]}\n"

        return companies_stock


class PrintReport:
    def __init__(self, data, is_complete):
        self.data = data
        self.is_complete = is_complete
        self.report = ""

        self.simple_report()

    def simple_report(self):
        self.report = (
            f"Data de fabricação mais antiga: {self.data.oldest_date()}\n"
            f"Data de validade mais próxima: {self.data.closest_date()}\n"
            f"Empresa com mais produtos: {self.data.company_bigger_stock()}"
        )

        if self.is_complete:
            self.complete_report()

    def complete_report(self):
        companies_stock = self.data.companies_stock_list()

        self.report = (
            f"{self.report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_stock}"
        )

    def print(self):
        return self.report
