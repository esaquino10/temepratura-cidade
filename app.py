import requests

# Fazer uma requisição à API de previsão do tempo
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={b1b963270d988512e211dc01bf74948aAPI')

# Verificar o status da resposta
if response.status_code == 200:
    data = response.json()
    # Extrair os dados da previsão do tempo
    # e realizar as operações desejadas
    print(data)
else:
    print('Erro ao obter a previsão do tempo:', response.status_code)
