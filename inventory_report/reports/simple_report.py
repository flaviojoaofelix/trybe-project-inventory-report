from collections import defaultdict


class SimpleReport:
    oldest_date = None
    closest_date = None
    company_bigger_stock = None

    @classmethod
    def generate(cls, products: list) -> str:
        cls.treat_data(products)

        return (
            f"Data de fabricação mais antiga: {cls.oldest_date}\n"
            f"Data de validade mais próxima: {cls.closest_date}\n"
            f"Empresa com mais produtos: {cls.company_bigger_stock }"
        )

    @classmethod
    def treat_data(cls, products: list):
        manufacturing_dates = []
        expiration_dates = []
        companies = defaultdict(int)

        for product in products:
            manufacturing_dates.append(product["data_de_fabricacao"])
            expiration_dates.append(product["data_de_validade"])
            company = product["nome_da_empresa"]
            companies[company] += 1

        cls.oldest_date = min(manufacturing_dates)
        cls.closest_date = min(expiration_dates)
        cls.company_bigger_stock = max(companies, key=companies.get)
