from datetime import datetime


records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821}
    ]

# {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564626000, 'start': 1564647600}



'''
records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821}
]
'''


def classify_by_phone_number(records):
    # Exemplo utilizando timestamp para compreender
    # timestamp = 1545730073
    # dt_object = datetime.fromtimestamp(timestamp)
    # print("dt_object =", dt_object)

    relatorio = []  # Relatorio que armazena o valor a ser cobrado a cada número: [{'source': 27-99999999, 'total': 2.50}, ...]
    dic_aux = {}    # Dicionario para auxiliar a estrutura de dados a ser inserido na lista relatorio depois

    for record in records:  # Loop dentro da lista com as informações das chamadas de cada telefone
        total = 0.0
        
        taxa_fixa = 0.36    # Taxa fixa que é cobrada
        total += taxa_fixa  # em todas as ligações

        inicial = datetime.fromtimestamp(record['start'])  # Pega tempo inicial da ligação
        final = datetime.fromtimestamp(record['end'])      # Pega tempo final da ligação

        tempo_ligacao = final - inicial  # Calcula tempo de duração da ligação

        print('número: ', record['source'])
        print('{}/{}/{} 0{}:0{}:0{}'.format(inicial.day, inicial.month, inicial.year, inicial.hour, inicial.minute, inicial.second))

        print('{}/{}/{} 0{}:0{}:0{}'.format(final.day, final.month, final.year, final.hour, final.minute, final.second))

        print('tempo_ligacao: ', tempo_ligacao)

        # Se a chamada foi realizada entre 06h e 22h, há uma outra forma de cobrança
        if (inicial.hour >= 6) and (inicial.hour <= 22) and (final.hour >= 6) and (final.hour <= 22):
            taxa_por_minuto = 0.09  # Taxa cobrada a cada ciclo de 60 segundos
            minutos = 0

            print('tempo_ligacao.seconds: ', tempo_ligacao.seconds)
            minutos += tempo_ligacao.seconds//60
            total += (minutos * taxa_por_minuto)

            print('minutos: ', minutos)

        print('total: %.2f' % (total))

        # Dic auxiliar a ser armazenado ou atualizado na lista
        dic_aux = {'source': record['source'], 'total': round(total, 2)}

        igual = False  # Variavel para validar se o número já foi armazenado

        # Se a lista relatorio estiver vazia, é o primeiro elemento da lista record que está sendo lido
        # Logo, não entra no loop para validar se o número já está na lista
        # Para não dar erro de len
        if relatorio != []:
            for dic in relatorio:  # Loop para validar se o número já está na lista
                print('dic: ', dic)

                if dic_aux['source'] == dic['source']:      # Se o número já foi validado antes:
                    print('é igual: ', dic_aux['source'])
                    dic['total'] += dic_aux['total']        # soma o total dessa ligação com o valor total do dic
                    dic['total'] = round(dic['total'], 2)
                    igual = True
        
        if not igual:                   # Se não for igual
            relatorio.append(dic_aux)   # Armazena o número e o total daquela ligação
            
        print('relatorio: ', relatorio)
        print()

    # Ordena a lista de forma descrescente, de acordo com chave 'total' dos dicionarios
    relatorio_ordenado = sorted(relatorio, key=lambda k: k['total'], reverse=True) 

    return relatorio_ordenado


def main():
    relatorio = classify_by_phone_number(records)
    print(relatorio)
    print()

    #for i in relatorio:
    #    print(i)


if __name__ == "__main__":
    main()
