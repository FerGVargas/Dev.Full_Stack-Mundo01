from dadosXLSX import Dados

ls=['carro','moto','barco','bicicleta','pedalinho']
ls=['EUW-993', 'FERRAMENTA4', 'DEWALT ', 220, 'SOW0', '65X6', 'PESAGEM', 'CHAVE BIELA', 'LIGAS FUNDIDAS']
c=Dados()

c.saveFileTemp(ls)
ls2=c.readFileTemp()
print('retorno -->>>>',ls2)