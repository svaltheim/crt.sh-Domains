import requests
from bs4 import BeautifulSoup

def get_subdomains(domain):
    # Consulta a crt.sh con el dominio dado
    url = f"https://crt.sh/?q={domain}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error al realizar la solicitud a crt.sh: {response.status_code}")
        return []
    
    # Analiza el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encuentra todas las filas de la tabla de resultados
    table_rows = soup.find_all('tr')
    
    subdomains = set()
    
    # Itera sobre las filas para extraer los subdominios
    for row in table_rows:
        cells = row.find_all('td')
        if len(cells) > 4:
            domain_entry = cells[4].text.strip()
            if domain_entry.endswith(domain):
                subdomains.add(domain_entry)
    
    return list(subdomains)

# Ejemplo de uso
dominio = "example.com"
subdominios = get_subdomains(dominio)
print(f"Subdominios encontrados para {dominio}:")
for subdominio in subdominios:
    print(subdominio)
