
# Tabela FIPE (Fundação Instituto de Pesquisas Econômicas)

import urllib.request
import json
import re
import os

class Sistema:

	def imprimir_marca(self):
		response = urllib.request.urlopen('http://fipeapi.appspot.com/api/1/carros/marcas.json')
		dataset_marca = json.loads(response.read())

		lista_marca = []
		for marca in dataset_marca:
			lista_marca.append(marca['name'] + ' (' + str(marca['id']) + ')')
		
		lista_marca.sort()
		for marca in lista_marca:
			print(marca)

	def imprimir_veiculo(self, id):
		response = urllib.request.urlopen(f'http://fipeapi.appspot.com/api/1/carros/veiculos/{id}.json')
		dataset_veiculo = json.loads(response.read())
		
		lista_veiculo = []
		for veiculo in dataset_veiculo:
			lista_veiculo.append(veiculo['name'] + ' (' + veiculo['id'] + ')')
		
		lista_veiculo.sort()
		for veiculo in lista_veiculo:
			print(veiculo)

	def imprimir_preco(self, id_veiculo, id_modelo):
		response = urllib.request.urlopen(f'http://fipeapi.appspot.com/api/1/carros/veiculo/{id_veiculo}/{id_modelo}.json')
		dataset = json.loads(response.read())
		
		data = []
		for ano in dataset:
		    data.append(ano['id'])
		
		preco_ano = {}
		for ano in data:
		    response = urllib.request.urlopen(f'http://fipeapi.appspot.com/api/1/carros/veiculo/{id_veiculo}/{id_modelo}/{ano}.json')
		    dataset = json.loads(response.read())
		    preco_ano[dataset['ano_modelo']] = float(str(dataset['preco'])[3:].replace('.', '').replace(',', '.'))

		print('\nTabela FIPE\n')
		for ano, preco in preco_ano.items():
			print(ano.replace('32000', 'Zero KM') + ': R$ ' + str(preco))

def main():
	while True:
		sistema = Sistema()
		
		# marca
		sistema.imprimir_marca()
		opcao_marca = input('\nDigite o código: ')
		os.system('cls')

		# veiculo
		sistema.imprimir_veiculo(opcao_marca)
		opcao_veiculo = input('\nDigite o código: ')
		os.system('cls')
		
		#preco
		sistema.imprimir_preco(opcao_marca, opcao_veiculo)
		input()
		os.system('cls')

if __name__ == '__main__':
	main()