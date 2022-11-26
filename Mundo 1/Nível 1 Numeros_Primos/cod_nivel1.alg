algoritmo "primo"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

var
c, i, n, p, s:inteiro
inicio
escreva("Digite um numero:")
leia(n)
para c de 1 ate n faca
    p<-0
    para i de 1 ate c faca
       se(c mod i=0) entao
           p<-p+1
       fimse
    fimpara
    se(p=2)entao

       escreval(" O numero ", c, " é primo ")
       s<-s+(c)
    fimse
fimpara
    escreval(" A soma de todo os numeros primos menores iguais a", i, " é:", s)
fimalgoritmo