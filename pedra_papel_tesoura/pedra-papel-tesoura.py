import random
import time

class Jogo():
  """
  Jogo:
  Pedra Papel Tesoura
  """
  def __init__(self):
    """
    Inicializando os atributos da classe
    """
    self.opcoes = {'0':'Pedra', "1":'Papel', "2": 'Tesoura'}
    self.escolhas = list(self.opcoes.keys())
    self.placar = {'Vitorias':0, "Derrotas":0, "Empates":0}
  
  def escolha_aleatoria(self):
    return random.choice(self.escolhas)

  def escolha_usuario(self):
    while True:
      e_usuario = input("Escolha: <0> Pedra <1> Papel <2> Tesoura:  ")
      if e_usuario in self.escolhas:
        return e_usuario
      print('Valor inválido, tente novamente')

  def mostra_placar(self):
    print("=================================")
    print('= Vitórias:', self.placar['Vitorias'])
    print('= Derrotas:', self.placar['Derrotas'])
    print('= Empates:', self.placar['Empates'])
    print("=================================")

  def rodada(self):
    voce = self.escolha_usuario()
    pc = self.escolha_aleatoria()
    print(f'Voce escolheu {self.opcoes.get(voce)}, eu escolhi {self.opcoes.get(pc)}')
    lista_vitoria = [1,-2]
    lista_derrota = [2,-1]
    res = int(voce) - int(pc)

    if res in lista_derrota:
      self.placar['Derrotas'] = self.placar.get('Derrotas') + 1 
      print('\nVocê Perdeu!')
    elif res in lista_vitoria:
      self.placar['Vitorias'] = self.placar.get('Vitorias') + 1 
      print('Você Venceu!')
    else:
      self.placar['Empates'] = self.placar.get('Empates') + 1
      print('É um Empate!!!')

  def jogar_novamente(self):
    escolha = input('Deseja jogar Novamente? [s/n]  ')
    if escolha.strip().lower() in ['s','si','sm','sim']:
      return True
    else:
      print('Fim de jogo!!!')
      return False


if __name__ == "__main__":
  loop = True
  jogo = Jogo()
  while loop:    
    
    jogo.rodada()
    time.sleep(2)
    jogo.mostra_placar()
    loop = jogo.jogar_novamente()