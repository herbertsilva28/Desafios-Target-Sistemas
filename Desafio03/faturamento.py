import json

# Função para carregar e processar o arquivo JSON
def processar_faturamento(meu_json):
    with open(meu_json, 'r') as file:
        data = json.load(file)

    faturamentos = data.get('faturamento', [])

    # Filtrar valores de faturamento, ignorar 0
    faturamentos_validos = [f for f in faturamentos if f > 0]

    if not faturamentos_validos:
        return {
            "menor_faturamento": None,
            "maior_faturamento": None,
            "dias_acima_da_media": 0
        }

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    dias_acima_da_media = sum(1 for f in faturamentos_validos if f > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

# Função principal para executar o script
def main():
    resultado = processar_faturamento('faturamento.json')
    print(f"Menor valor de faturamento: R${resultado['menor_faturamento']:.2f}")
    print(f"Maior valor de faturamento: R${resultado['maior_faturamento']:.2f}")
    print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_da_media']}")

if __name__ == "__main__":
    main()
