import requests
import jsons
import pandas as pd

def main():
#    multas = multas_acre()
    print("Acessando lista de multas...")



#
# def multas_acre(url = "http://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.json"):
#     response = requests.get(url)
#     if response.status_code == 200:
#         print("Conseguiu se conectar...")

    response = requests.get("http://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.json")
    if response.status_code == 200:
        list_of_processes = response.json()
        amount = len(list_of_processes['data'])
        print("Foram encontrados %d processos..." % amount)
        list_municipio = []
        list_nomeRazaoSocial = []
        list_valorAuto = []
        list_dataAuto = []
        list_situcaoDebito = []
        categories = ["Fauna", "Flora", "Pesca", "Outras"]

        for category in categories:
            print("Acessando multas sobre as %s ..." % category)
            for process in list_of_processes['data']:
                if process["tipoInfracao"] == category:
                    list_municipio.append(process["municipio"])
                    list_nomeRazaoSocial.append(process["nomeRazaoSocial"])
                    list_valorAuto.append(process["valorAuto"])
                    list_dataAuto.append(process["dataAuto"])
                    list_situcaoDebito.append((process["situcaoDebito"]))

            row = {'municipio': list_municipio, 'nomeRazaoSocial': list_nomeRazaoSocial, 'dataAuto': list_dataAuto, 'situcaoDebito': list_situcaoDebito}
            df = pd.DataFrame(row, columns=['municipio', 'nomeRazaoSocial', 'valorAuto', 'dataAuto', 'situacaoDebito'])
            df.to_csv('%s.csv' % category)
            print("Multas relacionadas a %s foram salvas na tabela!" % category)
        list_municipio.clear()
        list_nomeRazaoSocial.clear()
        list_valorAuto.clear()
        list_dataAuto.clear()
        list_situcaoDebito.clear()
    else:
        print("Algum problema com o link")

#Pede para que o programa execute a nossa função main
if __name__ == '__main__':
    main()
