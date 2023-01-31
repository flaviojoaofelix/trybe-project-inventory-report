from inventory_report.inventory.product import Product
# from tests.factories.product_factory import ProductFactory

product_interface = dict(
    {
        "id": [int],
        "nome_da_empresa": [str],
        "nome_do_produto": [str],
        "data_de_fabricacao": [str],
        "data_de_validade": [str],
        "numero_de_serie": [int, str],
        "instrucoes_de_armazenamento": [str],
    }
)

product_mock = dict(
    {
        "id": 1,
        "nome_da_empresa": "Trybe",
        "nome_do_produto": "Cursos",
        "data_de_fabricacao": "14-02-2022",
        "data_de_validade": "01-02-2022",
        "numero_de_serie": "111111111111",
        "instrucoes_de_armazenamento": "Arquivo digital mantido em cloud",
    }
)


def test_cria_produto():
    created_product = Product(
        product_mock["id"],
        product_mock["nome_do_produto"],
        product_mock["nome_da_empresa"],
        product_mock["data_de_fabricacao"],
        product_mock["data_de_validade"],
        product_mock["numero_de_serie"],
        product_mock["instrucoes_de_armazenamento"],
    )

    for key, key_type in product_interface.items():
        assert type(getattr(created_product, key)) in key_type
        assert getattr(created_product, key) == product_mock[key]
