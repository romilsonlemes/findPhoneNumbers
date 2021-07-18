import phonenumbers as tel
from phonenumbers import carrier as oper

# Ajuste do telefone
pais = "55"
ddd = "16"
numero = "997253825"
telefone = f"+{pais}{ddd}{numero}"
telefone_ajustado = tel.parse(telefone)
print(telefone_ajustado)


# Descobrir a Localização do telefone
from phonenumbers import geocoder as geotel

telefone_formulario = telefone[3:]
telefone_formulario_ajustado = tel.parse(telefone_formulario, "BR")
telefone_formatado = tel.format_number(telefone_formulario_ajustado,
                     tel.PhoneNumberFormat.NATIONAL)


print(f'Telefone Formatado: {telefone_formatado}')

cidade_telefone = geotel.description_for_number(telefone_ajustado, 'pt-br')
regiao = geotel.region_code_for_number(telefone_ajustado)
print(f'Cidade do Telefone: {cidade_telefone}')
operadora = oper.name_for_number(telefone_ajustado, "pt-br")
print(f'Operadora: {operadora}')
print(f'Região...: {regiao}')