from sys import argv

script_name, production_in_hourse, rate_in_hourse, prize=argv

def salary_payment(production_in_hourse, rate_in_hourse, prize):
	'''
	метод определяет зароботную плату сотрудника
	production_in_hourse ->  int выроботка в часах
	rate_in_ hourse-> int зароботная плата в час
	prize -> int премия
	
	'''
	result=int(production_in_hourse) * int(rate_in_hourse)+int(prize)
	return result
	
result=salary_payment(production_in_hourse, rate_in_hourse, prize)

print('\tзароботная плата сотрудника',result)

