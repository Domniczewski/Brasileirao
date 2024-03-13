import unittest
import json
from pprint import pprint


'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirão) para estudar como acessar listas, dicionarios,
e estruturas encadeadas (listas dentro de dicionários
dentro de listas)

Os dados estão fornecidos em um arquivo (ano2018.json) que você
pode abrir no firefox, para tentar entender melhor
(aperte alt para aparecer o menu, depois, no canto superior
esquerdo, arquivo > "abrir arquivo")

Vale a pena instalar o firefox, porque o leitor de arquivo
json dele é muito melhor, mas também existem extensões pro
chrome que fazem a mesma coisa.
'''

'''
DICA VSCODE: para poder executar o arquivo py a partir do VSCODE,
é importante ter aberto a pasta certa

Se voce tem a seguinte estrutura de diretorios
distribuidos > brasileirão > brasileirão.py
                             ano2018.json

Deve selecionar no VSCODE File > Open folder
e escolher a pasta brasileirão.
Se escolher distribuidos, o python nao vai achar o arquivo ano2018.json
'''

'''
Se quiser ver os dados dentro do python,
pode chamar a funcao pega_dados()
Nao se preocupe com como ela foi definida,
ela só está lendo o arquivo json pra voce
'''


def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados


'''
não dá muito certo imprimir todos os dados, porque o python
dá pau ao imprimir uma quantidade tao grande de informações,
mas podemos ver algumas coisas.

Descomente cada um dos exemplos abaixo para ver o que ele faz.
Verifique a correspondencia do que está sendo impresso pelo
python com o que aparece no firefox

Repare que além do print, você também verá o resultado dos testes
No caso, você não passou nenhum teste ainda.
As primeiras linhas no cmd tem o seu print,
as outras tem o resultado dos testes.
'''

dados2018 = pega_dados()
print("\n\n\n")  # apenas uns espaços pra te ajudar a ler. Deixe descomentado

# print('todas as chaves do dicionario principal', dados2018.keys())

# print('dados do time athletico')
# pprint(dados2018['equipes']['3'])

# pprint(dados2018['equipes'])
# print('esses foram os dados de todos os times')
# print('repare que cada time tem uma id. A id do corintians é 6')

# print('faixas de classificacao e rebaixamento')
# print(dados2018['fases']['2700']['faixas-classificacao'])

# print('classificacao dos times no fim do campeonato')
# print(dados2018['fases']['2700']['classificacao']['grupo']['Único'])

# print('podemos ver também os dados de um jogo, por exemplo,')
# print('os dados do jogo 192094:')
# pprint(dados2018['fases']['2700']['jogos']['id']['102094'])

print("\n\n\n")  # apenas uns espaços pra te ajudar a ler

'''
Como você viu nos prints acima, cada time tem uma id numérica,
e pode ser acessado em dados['equipes'][id_numerica]
'''


'''
#######################################################################
############## EXERCÍCIOS COMEÇAM A PARTIR DAQUI!! ####################
#######################################################################

Lembre-se de usar a variavel dados, que foi passada para a funcao.
Nao use dados2018, a variavel global que tinha sido definida antes

USAR A VARIÁVEL GLOBAL dados2018 DAQUI PRA FRENTE IRÁ ZERAR AS QUESTÕES

#######################################################################
'''


def nome_do_time(dados, id_numerica):
    '''Função que rebece o dicionário dos dados do brasileirão e uma ID
    e retorna o nome do time cuja ID foi recebido no segundo parâmetro
    '''
    return dados['equipes'][str(id_numerica)]['nome-comum']


def id_campeao(dados):
    '''Função que recebe o dicionario dos dados do brasileirão e
    retorna a ID do time que foi campeao.
    '''
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0]


def nome_campeao(dados):
    '''Funcao que recebe o dicionario dos dados do brasileirão e
    retorna o nome-comum do time que foi campeao.
    '''
    id_campeao = dados['fases']['2700']['classificacao']['grupo']['Único'][0]
    return dados['equipes'][id_campeao]['nome-comum']


def qtos_libertadores(dados):
    '''funcao que recebe o dicionario dos dados do brasileirão e
    retorna o número de times que o brasileirão qualifica para a libertadores,
    obtido a partir dos dados do arquivo JSON.
    '''
    faixas = dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    return int(faixas.split('-')[1])


def ids_dos_melhor_classificados(dados, n):
    '''Função que recebe o dicionário de dados e um número inteiro N e
    retorna uma lista com os IDs dos N times melhor classificados
    '''
    classificacao = dados['fases']['2700']['classificacao']['grupo']['Único']
    return classificacao[:n]


def classificados_libertadores(dados):
    '''Função que recebe o dicionário de dados do brasileirão e
    retorna uma lista com os ids dos times classificados para a
    libertadores pelo brasileirão

    DICA: use as duas funções anteriores
    '''
    num_libertadores = qtos_libertadores(dados)
    return ids_dos_melhor_classificados(dados, num_libertadores)


def nomes_classificados_libertadores(dados):
    '''Função que recebe o dicionário de dados do brasileirão e
    retorna uma lista com os nomes dos times classificados para a
    libertadores pelo brasileirão

    DICA: use a função anterior
    '''
    ids_libertadores = classificados_libertadores(dados)
    return [dados['equipes'][id]['nome-comum'] for id in ids_libertadores]

def ids_dos_times_de_um_jogo(dados, id_jogo):
    '''Função que recebe o dicionário de dados do brasileirão e a ID de um jogo e
    retorna uma tupla com as IDs dos dois times participantes no jogo
    '''
    jogo = dados['fases']['2700']['jogos']['id'][id_jogo]
    return jogo['time1'], jogo['time2']


def nomes_dos_times_de_um_jogo(dados, id_jogo):
    '''Função que recebe o dicionário de dados e a ID de um jogo e
    retorna o nome dos dois times participantes no jogo
    '''
    id_time1, id_time2 = ids_dos_times_de_um_jogo(dados, id_jogo)
    nome_time1 = dados['equipes'][id_time1]['nome-comum']
    nome_time2 = dados['equipes'][id_time2]['nome-comum']
    return nome_time1, nome_time2


def id_do_time(dados, nome_time):
    '''Função que recebe o dicionário de dados e o nome comum de um time e
    retorna a ID do respectivo time.

    Se o nome comum não existir, retorna a string 'nao encontrado'
    '''
    for id, info_time in dados['equipes'].items():
        if info_time['nome-comum'] == nome_time:
            return id
    return 'nao encontrado'


def datas_de_jogo(dados):
    '''Função que recebe o dicionário de dados e
    retorna uma lista com todas as datas em que houveram jogos.

    DICA: Mantenha as datas no mesmo formato em que se encontram no
    dicionário de dados e busquem em dados['fases']
    '''
    return list(dados['fases']['2700']['jogos']['data'].keys())


def data_de_um_jogo(dados, id_jogo):
    '''Função que recebe o dicionario de dados e uma ID de jogo e
    retorna a data em que o jogo ocorreu.

    Se a ID não for válida, retorna a string 'nao encontrado'
    '''
    jogo = dados['fases']['2700']['jogos']['id'].get(id_jogo)
    if jogo:
        return jogo['data']
    else:
        return 'nao encontrado'


def dicionario_id_estadio_e_nro_jogos(dados):
    '''Função que recebe o dicionário de dados e
    retorna outro dicionário contendo a contagem de jogos por estádio.

    Ou seja, as chaves do dicionário de retorno são as IDs dos estádios
    e o valores associados a elas são o número de jogos que ocorreram
    no respectivo estádio.
    '''
    jogos = dados['fases']['2700']['jogos']['id']
    estadios = {}
    for id_jogo, info_jogo in jogos.items():
        estadio_id = info_jogo['estadio_id']
        estadios[estadio_id] = estadios.get(estadio_id, 0) + 1
    return estadios


def busca_imprecisa_por_nome_de_time(dados, nome_parcial_time):
    '''Função que recebe o dicionário de dados e o nome parcial de um time e
    retorna uma lista com os IDs dos times que corresponderem ao nome

    Essa função implementa uma busca "fuzzy", isto é, queremos procurar por 'Fla'
    e achar o flamengo. Ou por 'Paulo' e achar o São Paulo.

    Nessa busca, a função recebe um nome, e verifica os campos
        'nome-comum', 'nome-slug', 'sigla' e 'nome',
    adicionando à lista de retorno os times que tiverem o nome parcial
    contido em um dos campos.

    Caso não seja encontrado nenhuma time correspondente,
    retorna uma lista vazia
    '''
    times_encontrados = []
    for id, info_time in dados['equipes'].items():
        for campo in ['nome-comum', 'nome-slug', 'sigla', 'nome']:
            if nome_parcial_time.lower() in info_time[campo].lower():
                times_encontrados.append(id)
                break  # encontrou, não precisa continuar procurando nos outros campos
    return times_encontrados


def ids_de_jogos_de_um_time(dados, time_id):
    '''Função que recebe o dicionário de dados e a ID de um time e
    retorna uma lista com as IDs de todos os jogos em que o time participou
    '''
    jogos_time = []
    for id_jogo, info_jogo in dados['fases']['2700']['jogos']['id'].items():
        if info_jogo['time1'] == time_id or info_jogo['time2'] == time_id:
            jogos_time.append(id_jogo)
    return jogos_time


def datas_de_jogos_de_um_time(dados, nome_time):
    '''Função que recebe o dicionário de dados e o nome comum de um time e
    retorna uma lista com as datas em que o time jogou
    '''
    time_id = id_do_time(dados, nome_time)
    jogos_time = ids_de_jogos_de_um_time(dados, time_id)
    datas_time = [data_de_um_jogo(dados, id_jogo) for id_jogo in jogos_time]
    return datas_time


def dicionario_de_gols(dados):
    '''Função que recebe o dicionário de dados e
    retorna um dicionário com a contagem de gols feitos por cada time.

    Ou seja, as chaves do dicionário de retorno serão os IDs dos times,
    e os valores associados a elas serão a quantidade de gols feitos
    pelo respectivo time.
    '''
    dic_gols = {}
    for id_jogo, info_jogo in dados['fases']['2700']['jogos']['id'].items():
        time1_id, time2_id = info_jogo['time1'], info_jogo['time2']
        
        placar1 = int(info_jogo['placar1'])
        placar2 = int(info_jogo['placar2'])
        
        dic_gols[time1_id] = dic_gols.get(time1_id, 0) + placar1
        dic_gols[time2_id] = dic_gols.get(time2_id, 0) + placar2
    return dic_gols




def time_que_fez_mais_gols(dados):
    '''Função que recebe o dicionário de dados e
    retorna a ID do time que fez o maior número de gols no campeonato'''
    dic_gols = dicionario_de_gols(dados)
    return max(dic_gols, key=dic_gols.get)


def rebaixados(dados):
    '''Função que recebe o dicionário de dados e
    retorna uma lista com as IDs dos times rebaixados para a série B
    '''
    faixa_rebaixamento = dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']
    rebaixados = []
    print("Faixa de rebaixamento:", faixa_rebaixamento)
    for id, info_time in dados['equipes'].items():
        print("Time ID:", id)
        if 'classificacao' in info_time and 'grupo' in info_time['classificacao'] and 'Único' in info_time['classificacao']['grupo']:
            print("Classificação do time:", info_time['classificacao']['grupo']['Único'])
            if info_time['classificacao']['grupo']['Único'] > int(faixa_rebaixamento.split('-')[0]):
                rebaixados.append(id)
    print("Times rebaixados:", rebaixados)
    return rebaixados


def classificacao_do_time_por_id(dados, time_id):
    '''Função que recebe o dicionario de dados e uma ID de time e
    retorna a classificacao desse time no campeonato.

    Se a ID não for válida, retorna a string 'nao encontrado'
    '''
    classificacao = dados['equipes'][time_id]['classificacao']['grupo']['Único']
    if classificacao:
        return classificacao
    else:
        return 'nao encontrado'



class TestStringMethods(unittest.TestCase):
    def test_000_nome_do_time(self):
        dados = pega_dados()
        global dados2018
        dados2018 = pega_dados()

        time1 = nome_do_time(dados, '1')
        self.assertEqual(time1, 'Flamengo')
        time2 = nome_do_time(dados, '695')
        self.assertEqual(time2, 'Chapecoense')

    def test_001_id_campeao(self):
        dados = pega_dados()
        try:
            self.assertEqual(id_campeao(dados), '17')
        except NameError as e:
            if 'dados2018' in str(e):
                self.fail(
                    "lembre-se de não usar a variavel dados2018, "
                    "mas sim a variavel dados que a função recebeu")
            else:
                raise e
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(id_campeao(dados), '1')

    def test_002_nome_campeao(self):
        dados = pega_dados()
        self.assertEqual(nome_campeao(dados), 'Palmeiras')
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(nome_campeao(dados), 'Flamengo')

    def test_003_qtos_libertadores(self):
        dados = pega_dados()
        # self.assertEqual('banana','bamana')

        self.assertEqual(qtos_libertadores(dados), 6)
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(qtos_libertadores(dados), 8)

    def test_004_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados, 10), [
                         "17", "1", "15", "13", "24", "4", "3", "9", "5", "22"])
        self.assertEqual(ids_dos_melhor_classificados(
            dados, 5), ["17", "1", "15", "13", "24"])
        self.assertEqual(ids_dos_melhor_classificados(
            dados, 3), ["17", "1", "15"])

    def test_005_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(classificados_libertadores(dados),
                         ["17", "1", "15", "13", "24", "4"])
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(classificados_libertadores(dados), [
                         "17", "1", "15", "13", "24", "4", "3", "9"])

    def test_006_nomes_classificados_libertadores(self):
        dados = pega_dados()
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-3'
        self.assertEqual(nomes_classificados_libertadores(dados), [
                         "Palmeiras", "Flamengo", "Internacional"])

    def test_007_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = ids_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['5', '17'])
        self.assertTrue(t2 in ['5', '17'])
        t1, t2 = ids_dos_times_de_um_jogo(dados, '102109')
        self.assertTrue(t1 in ['1', '26'])
        self.assertTrue(t2 in ['1', '26'])

    def test_008_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = nomes_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['Botafogo', 'Palmeiras'])
        self.assertTrue(t2 in ['Botafogo', 'Palmeiras'])
        t1, t2 = nomes_dos_times_de_um_jogo(dados, '102106')
        self.assertTrue(t1 in ['Chapecoense', 'Vasco'])
        self.assertTrue(t2 in ['Chapecoense', 'Vasco'])

    def test_009_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados, 'Cruzeiro'), '9')
        self.assertEqual(id_do_time(dados, 'Athletico'), '3')

    def test_010_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_011_datas_de_jogo_teste_2(self):
        dados = pega_dados()
        # deleto a data '14 de abril'
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        # e todos os jogos que ocorreram nela
        del dados['fases']['2700']['jogos']['id']['102094']
        del dados['fases']['2700']['jogos']['id']['102097']
        del dados['fases']['2700']['jogos']['id']['102101']
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_012_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados, '102132'), '2018-05-06')
        self.assertEqual(data_de_um_jogo(dados, '102187'), '2018-06-06')
        self.assertEqual(data_de_um_jogo(dados, '102540'), 'nao encontrado')

    def test_013_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 16)
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id'] = '72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 17)

    def test_014_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'anto')
        self.assertTrue('22' in ids_times)

    def test_015_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = ids_de_jogos_de_um_time(dados, '695')
        self.assertEqual(len(jogos_chapeco), 38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = ids_de_jogos_de_um_time(dados, '22')
        self.assertEqual(len(jogos_santos), 38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)

    def test_016_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = datas_de_jogos_de_um_time(dados, 'Santos')
        self.assertEqual(len(datas_santos), 38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = datas_de_jogos_de_um_time(dados, 'Chapecoense')
        self.assertEqual(len(datas_chapeco), 38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)

    def test_017_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = dicionario_de_gols(dados)

        # Modificando o placar do jogo '102422' para um valor inteiro
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = str(int(dados['fases']['2700']['jogos']['id']['102422']['placar2']) + 1)
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 35)

    def test_018_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time, '17')
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 120
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time, '695')

    def test_019_rebaixados(self):
        dados = pega_dados()
        self.assertEqual(rebaixados(dados), ['76', '26', '21', '18'])
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa'] = '15-20'
        self.assertEqual(rebaixados(dados), [
                         '33', '25', '76', '26', '21', '18'])

    def test_020_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados, '17'), 1)
        self.assertEqual(classificacao_do_time_por_id(dados, '30'), 11)
        self.assertEqual(classificacao_do_time_por_id(dados, '695'), 14)
        self.assertEqual(classificacao_do_time_por_id(
            dados, '1313'), 'nao encontrado')

    # as próximas funcões nao são testes
    def setUp(self):
        global dados2018
        del dados2018
        return super().setUp()

    def tearDown(self):
        global dados2018
        dados2018 = pega_dados()
        return super().tearDown()


def run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    run_tests()
