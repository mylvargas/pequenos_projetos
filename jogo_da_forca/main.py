"""
Jogo da forca
"""
from random import choice
import time
import re

class Forca():
  def __init__(self):
    self.palavra = None
    self.tamanho = 0
    self.chances = 6
    self.chutes = []
    self.p_lista = None
    self.r_lista = None
    

  def ler_palavras(self):
    with open('palavras.txt', encoding='utf8') as arq:
      linhas = arq.readlines()
      palavras = []
      for linha in linhas:
        padrao = re.compile(r'\w+')
        palavras.append(padrao.findall(linha)[0].strip().lower())
    return palavras


  def palavra_aleatoria(self):
    self.palavra = choice(self.ler_palavras())
    self.tamanho = len(self.palavra)
    self.p_lista = list(self.palavra)
    self.r_lista = ["_" for _ in range(len(self.p_lista))]


  def pergunta(self):
    return input('Escolha uma letra: ')


  def placar(self):
    print('========================')
    print("  Letras já escolhidas  ")
    print(f"{self.chutes}")
    print("  Vidas Restantes   ")
    print(f"         {self.chances}")
    print('========================')
    print(f'  {self.r_lista}')


  def tela_inicial(self):
      print("|------------")
      print("|       JOGO")
      print("|        DA")
      print("|       FORCA")
      print("|")
      print("|")
      print("|")
      print([" _ " * self.tamanho])

  def telas(self):
    pass
  
  def execucao(self):
    self.palavra_aleatoria()
    self.tela_inicial()
    while True:

      letra = self.pergunta()

      if letra in self.chutes:
        print('Essa letra já foi escolhida. Por favor, escolha outra')
        time.sleep(1)

      elif letra in self.p_lista:
        print('Acertou!')
        self.chutes.append(letra)
        time.sleep(1)
        for i,_ in enumerate(self.p_lista):
          if letra == self.p_lista[i]:
            self.r_lista[i] = letra 
      else:
        self.chutes.append(letra)
        self.chances = self.chances - 1
        print(f"Errou, você ainda tem {self.chances} vidas")
        time.sleep(1)

      self.placar()
      if self.chances == 0:
        print('========================')
        print(' Game Over')
        time.sleep(1)
        print(' Você Perdeu')
        time.sleep(1)
        print(f' A palavra era: {self.palavra.title()}\n')
        print('========================')
        time.sleep(3)
        
        break
      
      if '_' not in self.r_lista:
        print('========================')
        print(' Game Over')
        time.sleep(1)
        print(' Você Ganhou!!!')
        time.sleep(1)
        print(f' A palavra é: {self.palavra.title()}')
        print('========================')

        time.sleep(3)
        break

if __name__ == '__main__':
  f = Forca()
  f.execucao()