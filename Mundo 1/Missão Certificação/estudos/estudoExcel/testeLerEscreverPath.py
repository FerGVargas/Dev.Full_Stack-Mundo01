

from pathlib import Path

def escreverPatnTxt(): 
    data_folder = Path("planilhas/")
    new_path = data_folder / "testfile.txt"
    with open(new_path, 'w') as f:
        f.write('foi escreverPatn')

def escreverTxtPatnParam(sPath): 
    data_folder = Path(sPath)
    new_path = data_folder / "testfile.txt"
    with open(new_path, 'w') as f:
        f.write('foi escreverTxtPatnParam2') 

def getPathPlanilhas(sPath,nomeArquivo):

    if (sPath!=''):
      data_folder = Path(sPath)
      new_path = data_folder / nomeArquivo
    else:
      new_path=''  

    return new_path

def createTxt(new_path):
    with open(new_path, 'w') as f:
        f.write('foi usando parametros') 
#escreverPatnTxt()               

#definindo path
pathPlanilhas='planilhas/'

#salva txt no diretorio abaixo
#escreverTxtPatnParam(pathPlanilhas)

#retorna caminho do arquivo a ser lido/ salvo
#print(getPathPlanilhas(pathPlanilhas,'newFileText.txt'))

#teste final antes de incorporar a rotina a classe
createTxt(getPathPlanilhas(pathPlanilhas,'newFileText.txt'))
