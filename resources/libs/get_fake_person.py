from faker import Faker

faker = Faker('pt_BR');

# Remove pontos de uma string de nome.
def limpar_ponto_nome(nome):
    # Remove apenas o ponto
    nome_limpo = nome.replace('.', '')
    return nome_limpo
# Remove pontos e traços de uma string de CPF.
def limpar_cpf(cpf):
    # Remove pontos e traços
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    return cpf_limpo

def limpar_cnpj(cnpj):
    cnpj_limpo = cnpj.replace('.', '').replace('-', '').replace('/', '')
    return cnpj_limpo

def limpar_zipCode(zipCode):
    zipCode_limpo = zipCode.replace('.', '').replace('-', '').replace('/', '')
    return zipCode_limpo

def gerar_telefone_sem_formatacao():
    return faker.msisdn()

def get_fake_person():
    person = {
        "name": limpar_ponto_nome(faker.name()),
         "email": faker.email(),
         "cpf": limpar_cpf(faker.cpf()),
    }
    return person


def get_fake_company():
    company = {
        "nome_empresa": faker.company(),
        "cnpj": limpar_cnpj(faker.cnpj()),
        "telefone": gerar_telefone_sem_formatacao(),
        "email": faker.company_email(),
        "zipCode": limpar_zipCode(faker.postcode()),
        "city": faker.city(),
        "state": faker.state_abbr(),
        "district": faker.street_name(),
        "street": faker.street_name(),
        "number": faker.building_number(),
        "country": faker.city(),
        "descricao": faker.job(),
        "responsavel": faker.first_name(), 
    }
    return company


#company = get_fake_company();
# print(company["email"]);
# print(company["cnpj"]);
# print(company["telefone"]);
# print(company["zipCode"]);
#print(company["descricao"]);
#print(company["responsavel"]);
# address = get_fake_address();
# print(address["city"]);
# print(address["zipCode"]);
