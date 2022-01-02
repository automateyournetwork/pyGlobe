import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
pyGlobe_template = env.get_template('pyGlobe.j2')
pyGlobe_Country_template = env.get_template('pyGlobe_Country.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# All Countries
# -------------------------
allCountries = requests.request("GET", "https://restcountries.com/v3.1/all", headers=headers)
allCountriesJSON = allCountries.json()

parsed_all_output = pyGlobe_template.render(allCountries = allCountriesJSON)

with open("pyGlobe.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()    
# -------------------------
# Per Country
# -------------------------
for country in allCountriesJSON:
    singleCountry = requests.request("GET", f"https://restcountries.com/v3.1/name/{ country['name']['common'] }", headers=headers)
    singleCountryJSON = singleCountry.json()

    parsed_single_output = pyGlobe_Country_template.render(oneCountry = singleCountryJSON)

    with open(f"pyGlobe_{ country['name']['common'] }.md", "w") as fh:
        fh.write(parsed_single_output)               
        fh.close()