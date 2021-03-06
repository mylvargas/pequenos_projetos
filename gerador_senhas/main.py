"""
Código para a geração de uma senha aleatória
Retorna a senha no terminal e escreve em um arquivo txt
@author: Maycol M. Vargas
"""
from os import write
import string
import random as rnd

class GeraSenha():
  def __init__(self):
    self.ncaracteres = 0
    self.nnumeros = 0
    self.nsimbolos = 0
    self.cont = True

  @staticmethod
  def mensagem_intro():
    print("=================================")
    print("= Bem Vindo ao Gerador de Senha =")
    print("=================================")
  
  @staticmethod
  def l_alf():
    return list(string.ascii_letters)

  @staticmethod  
  def l_dig():
    return list(string.digits)# ['1','2','3','4','5','6','7','8','9']

  @staticmethod
  def l_sim():
    return [x for x in list(string.printable[62:94]) if x not in ['ç','´','`','^',',','.','"',"'",";"] ]

  def inputs(self):
    mensagem = """\n ERRO: Somente numeros inteiros são aceitos. Por favor, tente novamente!
     ou Pressione <CTRL + C> para interromper a execução\n"""
    while True:  
      try:
        self.ncaracteres = abs(int(input("Digite o número de Letras em sua senha:  ")))
      except Exception:
        print(mensagem)
      else:
        break

    while True:
      try:
        self.ndigitos = abs(int(input("Digite a quantidade de Números em sua senha:  ")))
      except Exception:
        print(mensagem)
      else:
        break
    
    while True:
      try:
        self.nsimbolos=abs(int(input("Digite quantos Simboloas deseja em sua senha:  ")))
      except Exception:
        print(mensagem)
      else:
        break

  def gerar(self):
    self.mensagem_intro()
    self.inputs()
    lista_completa = []

    if self.ncaracteres > 0:
      for _ in range(self.ncaracteres):
        lista_completa.append(rnd.choice(self.l_alf()))

    if self.ndigitos > 0:
      for _ in range(self.ndigitos):
        lista_completa.append(rnd.choice(self.l_dig()))

    if self.nsimbolos > 0:
      for _ in range(self.nsimbolos):
        lista_completa.append(rnd.choice(self.l_sim()))
    #Embaralhando sua lista com os elementos da senha
    rnd.shuffle(lista_completa)
    #Escrevendo sua senha em um arquivo
    with open('senha.txt','w') as arq:
      s = ''.join(lista_completa)
      arq.write(s)
      print("Sua senha é: ", s)



if __name__ == "__main__": 
  senha = GeraSenha()
  while senha.cont:
    senha.gerar()
    confirma = input("Deseja gerar outra senha? [s/n]")
    if confirma.strip().lower() in ['s','im','sim','sm','ssim','siim',"sin",'y','yes']:
      pass
    else:
      print("Até mais!")
      break
