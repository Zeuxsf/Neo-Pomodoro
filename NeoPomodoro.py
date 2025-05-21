#Olá GitHUB!
import customtkinter as ctk
import time
import pygame
import sys
import os
from winotify import Notification


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def notificar(titulo, mensagem):
    toast = Notification(app_id="Neo-Pomodoro", title=titulo,msg=mensagem,icon=resource_path('itens/ico.ico'))
    toast.show()

pygame.init()

janela = ctk.CTk(fg_color='goldenrod')
janela.geometry('300x400')
janela.title('Neo-Pomodoro')
janela.resizable(False,False)
janela.iconbitmap(resource_path('itens/ico.ico'))

conteudo = ctk.CTkFrame(janela,280,380,fg_color='saddle brown')
conteudo.place(x=10,y=10)

def iniciar(minutos,identificador):
    global descanso_longo_contador 
    segundos = minutos * 60

    descanso_longo_contador += 1
    descanso_longo_contador_text.configure(text = descanso_longo_contador)

    if descanso_longo_contador == 4:
        descanso_longo_contador_text.configure(text = '0')
        segundos = 15 * 60
        descanso_longo_contador = 0

    iniciar_btn.configure(state = 'disabled')
    descansar_btn.configure(state = 'disabled')

    def atualizar():
        nonlocal segundos
        global descanso_longo_contador

        if segundos >=0:
            mins = segundos // 60
            segs = segundos % 60
            cronometro.configure(text=f'{mins:02d}:{segs:02d}')
            segundos -= 1
            janela.after(1000, atualizar)

            
            if segundos == 0:
                pygame.mixer.music.load(resource_path('itens/bip.mp3'))
                pygame.mixer.music.play()
                iniciar_btn.configure(state = 'normal')
                descansar_btn.configure(state = 'normal')
                
                if identificador == 0:
                    notificar('Temporizador Zerado!','Hora de dar uma Pausa! Ative o Cronômetro de DESCANSO!')
                    return 
                elif identificador == 1:
                    notificar('Temporizador Zerado!','Hora de Voltar ao FOCO!! Ative o Cronômetro Novamente!')
                    return 

    atualizar()



crono_square = ctk.CTkFrame(conteudo,200,200,fg_color='saddle brown',border_color='white',border_width=2)
crono_square.place(x=41,y=30)

cronometro = ctk.CTkLabel(crono_square,20,20,text='█ ‿ █',text_color='white',font=('Franklin Gothic',50))
cronometro.place(x=36,y=68)

iniciar_btn = ctk.CTkButton(conteudo,50,50,text='Começar', text_color='white',fg_color='saddle brown', border_color='white',border_width=1,hover_color='white', command=lambda: iniciar(25,0))
iniciar_btn.place(x=111,y=260)

descansar_btn = ctk.CTkButton(conteudo,50,50,text='Descanso', text_color='white',fg_color='saddle brown', border_color='white',border_width=1,hover_color='white', command=lambda: iniciar(5,1))
descansar_btn.place(x=107,y=320)

descanso_longo_contador = 0
descanso_longo_contador_text = ctk.CTkLabel(conteudo,text='0', text_color='white',font=('',20))
descanso_longo_contador_text.place(x=245,y=335)





janela.mainloop()