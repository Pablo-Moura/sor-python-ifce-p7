#!usr/bin/python
import requests
import cgitb, cgi

def pegar_info(poke):
	stringInfo = ""
	stringInfo = stringInfo + f'Informações Gerais do {pokemon}<br>'
	stringInfo = stringInfo + f'Id Pokedex: {poke["id"]}<br>'
	stringInfo = stringInfo + f'EXP base: {poke["base_experience"]}<br>'
	stringInfo = stringInfo + f'Altura: {poke["height"]}<br>'
	stringInfo = stringInfo + f'Peso: {poke["weight"]}<br>'
	return print(f"""<p>{stringInfo}</p>""")

def pegar_habilidades(poke):
	print(f'<br>Habilidades do {pokemon}')
	stringHab = ""
	for i in poke['abilities']:
		stringHab = stringHab + f"{i['ability']['name']}<br>"
		if i == poke['abilities'][len(poke['abilities']) - 1]:
			return print(f"""<p>{stringHab}</p>""")

def pegar_stats(poke):
	print(f'<br>Atributos base do {pokemon}')
	stringStats = ""
	for i in poke['stats']:
		stringStats = stringStats + f"{i['stat']['name']}: {i['base_stat']}<br>"
		if i == poke['stats'][len(poke['stats']) - 1]:
			return print(f"""<p>{stringStats}</p>""")

def pegar_ev(poke):
	print(f"<br>Ev's do {pokemon}")
	stringEv = ""
	for i in poke['stats']:
		stringEv = stringEv + f"{i['stat']['name']}: {i['effort']}<br>"
		if i == poke['stats'][len(poke['stats']) - 1]:
			return print(f"""<p>{stringEv}</p>""")

def pegar_type(poke):
	print(f'<br>Tipagem do {pokemon}')
	stringType = ""
	for i in poke['types']:
		stringType = stringType + f"{i['type']['name']}<br>"
		if i == poke['types'][len(poke['types'])-1]:
			return print(f"""<p>{stringType}</p>""")

def main():
	try:
		api = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon).lower()
		res = requests.get(api)
		resJs = res.json()
		pegar_info(resJs)
		pegar_type(resJs)
		pegar_stats(resJs)
		pegar_ev(resJs)
		pegar_habilidades(resJs)
	except:
		print("""<p>Pokemon não encontrado.<br>
					Tente novamente.</p>""")

def print_inicial():
	print(f"""
	    <!DOCTYPE html>
	    <html lang="pt-br">
	    	<head>
	    		<link rel="stylesheet" type="text/css" href="../style/style.css" media="screen">
	        	<title>Pokédex Web - {poke}</title>
	    	</head>
	    	<body>
	    		<form>
	    			<main class="search">
	    				<h4>""")

def print_final():
	print("""
						</h4>
					</main>
				</form>
			</body>
		</html>""")

cgitb.enable()
form = cgi.FieldStorage()
poke = form.getvalue('pokemon')
pokemon = poke

print_inicial()
main()
print_final()