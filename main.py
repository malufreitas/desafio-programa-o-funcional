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
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564626000, 'start': 1564647600}
]

def classify_by_phone_number(records):
    timestamp = 1545730073
    dt_object = datetime.fromtimestamp(timestamp)
    print("dt_object =", dt_object)

    start = 1564647600
    end = 1564626000

    relatorio = []
    dic_aux = {}

    for record in records:
        total = 0.0

        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])

        print('{}/{}/{} {}:{}:{}'.format(start.day, start.month, start.year, start.hour, start.minute, start.second))
        print('{}/{}/{} {}:{}:{}'.format(end.day, end.month, end.year, end.hour, end.minute, end.second))

        tempo_ligacao = end - start
        print('tempo_ligacao: ', tempo_ligacao)

        taxa_fixa = 0.36
        #total += taxa_fixa
        
        
        if (start.hour >= 6) and (start.hour <= 22) and (end.hour >= 6) and (end.hour <= 22):
            taxa_por_minuto = 0.09

            minutos = 0
            minutos += tempo_ligacao.seconds//60
            print('minutos: ', minutos)
            total = (minutos * taxa_por_minuto)
            print('total: %.2f' % (total))
        

        dic_aux = {'source': record['source'], 'total': total}
        relatorio.append(dic_aux)

        print()

    for i in relatorio:
        print(i)


def main():
    classify_by_phone_number(records)

if __name__ == "__main__":
    main()
