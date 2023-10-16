import threading
from time import sleep
import customtkinter
import sys
from tkVideoPlayer import TkinterVideo
from back import Bloquear_IP


def Start_Bloqueio():
    start = Bloquear_IP()
    if start == 'sim':
        sleep(5)
        janela.destroy()
        sys.exit()


def Loop(e):
    videoplayer.play()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("400x500")
janela.title("FEVOX WI-FI")


# JANELA MONITORAMENTO_WI-FI *****************
tabview = customtkinter.CTkTabview(
    master=janela,
    segmented_button_fg_color='black',
    text_color='black',
    segmented_button_selected_color='#ffffff',
    segmented_button_selected_hover_color='#ffffff',
    fg_color='white'
    )
tabview._segmented_button.configure(font=('DejaVu Sans Mono', 30, 'bold'))
tabview.pack(fill='both', expand=1, padx=10, pady=10)

tabview.add("ANALYSIS")

texto_arq = customtkinter.CTkLabel(
    master=tabview.tab("ANALYSIS"),
    text='ANÁLISE DE LOGS',
    font=("", 20, 'bold'),
    text_color='black'
    )
texto_arq.pack(ipady=10, padx=10, pady=10)

p = threading.Thread(target=Start_Bloqueio)
p.start()
videoplayer = TkinterVideo(scaled=True, master=tabview.tab("ANALYSIS"))
videoplayer.load(r'GIF4.gif')
videoplayer.pack(expand=True, fill="both")
videoplayer.play()
videoplayer.bind("<<Ended>>", Loop)

janela.mainloop()
