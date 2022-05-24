from api_connect import BrasilIO

class BuscaApi:

    def __init__(self, cidade, data):

        self.cidade = cidade
        self.data = data

    def Busca(self, cidade, data_pesquisa):
        user_agent = "seu-usuario"
        auth_token = "a835b732c90861eb8344542df051729da01deb05"
        api = BrasilIO(user_agent, auth_token)
        dataset = "covid19"
        table_name = "caso_full"

        filters = {"search": "{}".format(cidade.replace(
        " ", "+")), "date": "{}".format(data_pesquisa)}
        data = api.data(dataset, table_name, filters)

        for row in data:
            cidade = row['city']
            estado = row['state']
            data = row['date']
            populacao = row['estimated_population']
            total_confirm = row['last_available_confirmed']
            mortes = row['last_available_deaths']
            novas_mortes = row['new_deaths']
            novo_confirm = row['new_confirmed']
        casos = {'cidade': cidade, 'estado': estado, 'data': data, 'populacao': populacao, 'total_confirm': total_confirm, 'mortes': mortes, 'noavas_mortes': novas_mortes, 'novo_confirm': novo_confirm}
        return casos
