# Importando as bibliotecas necessárias
import PySimpleGUI as sg
from random import randint
from time import sleep


class Dado:
    def iniciar(self):
        self.tentativas = 0
        # Variável que será usada para guardar os valores que o usuário digitar
        self.valores = list()
        
        # Definindo um tema para a janela
        sg.theme('DarkTeal6')
        
        # Gerando um valor aleatório para o dado
        self.valor_dado = randint(1, 6)
        
        # Gerando o layout da tela
        layout = [
            [sg.Text('Chute um valor para o dado:'), 
             sg.Input(size=(5,1), key='chute')],
            [sg.Text(size=(1, 2))],
            [sg.Output(size=(60, 6), key='output', text_color='Blue')],
            [sg.Text(size=(1, 1))],
            [sg.Button('Testar valor', size=(len('Testar valor')+4, 1)),
             sg.Button('Reiniciar jogo', size=(len('Reiniciar Jogo') + 4, 1)), 
             sg.Button('Sair', size=(len('Sair') + 4, 1))],
        ]
        # Criando uma variável para a janela
        self.janela = sg.Window('Dado Aleatório', layout)
        
        try:
            while True:
                self.evento, self.valor = self.janela.Read()
                
                if self.evento == sg.WINDOW_CLOSED or self.evento == 'Sair':
                    break
                
                if self.evento == 'Testar valor':
                    # Chamando o método que verifica se o valor do usuário é 
                    # igual ao valor do dado gerado
                    self.verificar_resposta_usuario()
                
                if self.evento == 'Reiniciar jogo':
                    self.janela.close()
                    self.iniciar()
                          
        except:
            print('Ocorreu um erro no game! Tente novamente!')
    
        self.janela.close()
        
    def verificar_resposta_usuario(self):
        try:
            a = self.valor['chute']
            
            if int(a) > 6 or int(a) < 1:
                print('Você deve inserir algum valor entre 1 e 6.')
            else:
                if self.verificar_repeticao(int(a)) == 0:
                    print(f'Você já inseriu o número {a}! Tente outro número!')
                    self.janela['chute'].update('')
                else:
                    # Limpa a tela que o usuário insere o chute
                    self.janela['chute'].update('')
                    self.tentativas += 1
                    
                    # if e else, para verificar se o usuário acertou ou não
                    if self.valor_dado == int(a):
                        self.analisar_as_tentativas_usuario()
                    else:
                        print(f'Você digitou {a} e errou, tente novamente!')
                
        except:
            print('Você deve inserir algum valor entre 1 e 6.')
            
    def fechar_janela_e_reiniciar(self):
        # Fecha a janela
        self.janela.close()
        # Chama o método que inicia o game
        self.iniciar()

    def analisar_as_tentativas_usuario(self):
        if self.tentativas == 1:
            self.vitoria_primeira()
        else:
            self.vitoria_demorada()
         
    def verificar_repeticao(self, novo_valor):
        # Verificar se esse número já existe na lista que guarda o que o 
        # usuário digitar
        if novo_valor in self.valores:
            return 0
        # Se não estiver na lista, ele insere esse valor na lista
        else:
            self.valores.append(novo_valor)
            return 1           
        
    def vitoria_primeira(self):
        self.janela.hide()
        sg.theme('DarkBlue12')
        sg.PopupNoTitlebar('Parabéns: Você acertou de primeira!')
        self.fechar_janela_e_reiniciar()
        
    def vitoria_demorada(self):
        self.janela.hide()
        sg.theme('DarkRed2')
        sg.PopupNoTitlebar(f'Parabéns: Você acertou, mas precisou de '
                           f'{self.tentativas} tentativas para isso.')
        self.fechar_janela_e_reiniciar()

 
dado = Dado()
dado.iniciar()
