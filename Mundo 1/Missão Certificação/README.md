## Projeto de certificação M1 - Estácio - Grupo DEV30 / Full Stack
 
 Periodo - 2022.3


### Apresentação 

 Se trata de um projeto voltado para uma aplicação desktop que tem como objetivo criar controle ficticio de aquisição de ferramentas assim como alocação das mesmas para equipes da empresa que fosse adquirir o software 

 Uma particularidade é a de persistência dos dados que devem ser em planilhas excel conforme especificado

 As planilhas de cadastro são 'ferramentes.xlsx','funcionarios.xlsx' e 'solicitacoes.xlsx', estas podem ser removidas que o sistema criará novas porem vazias. As demais são usadas para as listas dos formulários de cadastro.

 Nosso projeto foi desenvolvido seguindo a seguinte visão, autenticação e seleção do modulo (ferramentas,funcionários,solicitações) 

 Outra observação é a de que por trabalharmos em sistemas operacionais diferentes, algumas telas tiveram renderização diferentes, no caso a tela de solicitações vista na gravação no ubuntu renderiza de forma diferente no windows 10. Infelizmente nosso tempo estava muito reduzido pois nosso grupo conseguiu iniciar no dia 31/10 e a entrega em 27//11  onde surgiu uma segunda dificuladade, a disponibilidade individual de tempo para o desenvolvimento que devido estar em função da vida cotidiana de cada um, influenciava diretamente no tempo de resposta e por sua vez nos resultados que estariam definindo os rumos do projeto.

 Sendo assim era necessário primeiro concluir a parte funcional para posteriores reviões.

 Por fim a autênticação que poderia ser um dicionario de usuarios e senha, para fins de desenvolvimento, ficou com usuario 'xxx' e senha '12345'

### Tecnologias utilizadas

Python,tkinter
 
### Requisitos 

Python3.8.10 ou superior

### Bibliotecas

* pip install Pillow
* pip install openpyxl
* pip install reportlab
* pip install tkcalendar

### Executando o projeto

Executar o arquivo main.py

### Definição dos campos
   
    Campos Ferramentas
     
      - codigo : edição livre  (campo unico)
      - descrição : edição livre 
      - fabricante : pré definido em 'listasFerramentas.xlsx' worksheet 'fabricante'   
      - voltagem  : pré definido em 'listasFerramentas.xlsx' worksheet 'voltagem' 
      - part number : edição livre 
      - unidade de medida :pré definido em 'listasFerramentas.xlsx' worksheet 'unidade de medida' 
      - tipo de ferramenta : pré definido em 'listasFerramentas.xlsx' worksheet 'tipo de ferramentas'
      - material : pré definido em 'listasFerramentas.xlsx' worksheet 'material'
               
      obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de  
           todos os campos assim como a verificado se a chave primaria(campo único) estar repetido
           
    Campos Funcionários 

      - nome completo : edição livre (campo unico) 
      - cpf : edição livre  (campo unico)
      - telefone : edição livre 
      - turno : pré definido em 'listasFuncionarios.xlsx' worksheet 'turno' 
      - equipe : pré definido em 'listasFuncionarios.xlsx' worksheet 'equipes' 
               
      obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de  
           todos os campos assim como a verificado se a chave primaria(campo único) estar repetido
        
    Campos Solicitações
      
      - nome : pré definido em lista vindo da planilha funcionarios.xlsx 
      - cpf : pré definido em lista vindo da planilha funcionarios.xlsx 
      - equipe : pré definido em lista vindo da planilha funcionarios.xlsx
      - codigo da ferramenta : pré definido em lista vindo da planilha ferramentas.xlsx 
                
      obs: esse campo é verificado na planilha de solicitações afim de saber se a ferramenta 
            ja se encontra alocada ou reservada onde e apresentado com quem está e qual a previsão 
            de entrega ou saida
      
      - data da saida : fornecida por um calendário usando data atual 
      - hora da saida :pré definido em 'listasSolicitacoes.xlsx' worksheet 'horario'
      - data da devolução : fornecida por um calendário usando data atual 
      - hora da devolução : pré definido em 'listasSolicitacoes.xlsx' worksheet 'horario'
     
      obs : no optar por reservar, data da saida e devolução serão acrescidas de um dia considerando a
            data autal 
      
      - motivo : pré definido em 'listasSolicitacoes.xlsx' worksheet 'motivo'
        
### As Consultas 
      
   As consultas ou filtros, são feitas diretamente na respectiva planilha dependendo do assunto. Cada consulta contem 
   filtros especificos por assunto ou seja 
     
     ferramentas : codigo,descricao,fabricante e material
     
     funcionarios : nome,cpf,turno e equipe
     
     solicitações : nome,equipe, codigo da ferramenta e reservada
   
   Todas as funcionalidades de consulta deveriam ter as opçôes de listagens,edição e remoção
   
   obs: no caso da remoção e edição estas deixadas para o final devido a falta de tempo. A remoção foi implementada apenas ferramentas 
        onde é verificado se existe alguma solicitação podendo a mesma se encontrar alocada ou reservada. A ideia era ter o mesmo conceito 
        em consulta de funcionários. Já em solicitações seria uma remoção direta. No caso da edição deveria ter sido aplicado o mesmo
        conceito de verificação de deleção em ferramentas e funcionários porem no caso das solicitaçoes campos como nome,cpf,equipe e codigo da 
        ferramenta não estariam habilitados para edição pois são consideradas chaves estrangeiras ou seja informações que precisam existir nas
        planilhas de ferramentas e funcionários.
       


### Video do projeto

https://youtu.be/Mtfv4Wa3tLw

