import customtkinter
import serial

# Tenta contato com o Arduino
try:
    arduino = serial.Serial('COM3', 9600)
except serial.SerialException:
    arduino = None
    print("Arduino não conectado. Algumas funcionalidades necessitam dele.")

def exibir_tela_login(janela, callback):
    for widget in janela.winfo_children():
        widget.destroy()
    
    janela.title("Tela de login")
    janela.geometry("500x300")

    def clique():
        callback(janela)

    texto = customtkinter.CTkLabel(janela, text="Fazer Login")
    texto.pack(padx=10, pady=10)

    email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
    email.pack(padx=10, pady=10)

    senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
    senha.pack(padx=10, pady=10)

    checkbox = customtkinter.CTkCheckBox(janela, text="Lembre de mim")
    checkbox.pack(padx=10, pady=10)

    botao = customtkinter.CTkButton(janela, text="Login", command=clique)
    botao.pack(padx=10, pady=10)

def exibir_tela_principal(janela):
    janela.geometry("600x400")
    janela.title("Segurança em um clique")

    abas = customtkinter.CTkTabview(janela)
    abas.pack(expand=1, fill="both", padx=10, pady=10)

    contato = abas.add("Contato")
    testes = abas.add("Testes")
    sobre = abas.add("Sobre")
    configuracoes = abas.add("Configurações")

    # Aba "Contato"
    customtkinter.CTkLabel(contato, text="Selecione os contatos que devem ser avisados:").pack(padx=10, pady=10)

    frame_contatos = customtkinter.CTkFrame(contato)
    frame_contatos.pack(padx=10, pady=10, fill="x")

    global contato_entry
    contato_entry = customtkinter.CTkEntry(frame_contatos, placeholder_text="Nome do Contato")
    contato_entry.pack(side="left", padx=5, pady=5, expand=True, fill="x")

    adicionar_contato_button = customtkinter.CTkButton(frame_contatos, text="Adicionar", command=adicionar_contato)
    adicionar_contato_button.pack(side="left", padx=5, pady=5)

    global frame_contatos_checkboxes
    frame_contatos_checkboxes = customtkinter.CTkFrame(contato)
    frame_contatos_checkboxes.pack(padx=10, pady=10, fill="both", expand=True)

    global contatos
    contatos = []

    # Aba "Testes"
    customtkinter.CTkLabel(testes, text="Testar funcionalidades do acessório").pack(padx=10, pady=10)
    customtkinter.CTkButton(testes, text="Testar Buzzer", command=testar_buzzer).pack(padx=10, pady=10)
    customtkinter.CTkButton(testes, text="Ligar LED", command=ligar_led).pack(padx=10, pady=10)
    customtkinter.CTkButton(testes, text="Desligar LED", command=desligar_led).pack(padx=10, pady=10)
    customtkinter.CTkButton(testes, text="Mostrar Localização", command=mostrar_localizacao).pack(padx=10, pady=10)

    # Aba "Sobre"
    customtkinter.CTkLabel(sobre, text="Segurança em um clique: Inovação em segurança para mulheres").pack(padx=10, pady=10)
    customtkinter.CTkLabel(sobre, text="Desenvolvido por alunos do 2º informática da escola RCR,\n"
                                      "o projeto tem o intuito de inovar na segurança feminina,\n"
                                      "garantindo uma segurança a mais para todas.").pack(padx=10, pady=10)

    # Configurações"
    customtkinter.CTkLabel(configuracoes, text="Configurações do Aplicativo").pack(padx=10, pady=10)
    customtkinter.CTkLabel(configuracoes, text="Escolha as ações a serem realizadas após o botão ser pressionado:").pack(padx=10, pady=10)

    frame_acoes = customtkinter.CTkFrame(configuracoes)
    frame_acoes.pack(padx=10, pady=5, fill="x")

    enviar_localizacao_cb = customtkinter.CTkCheckBox(frame_acoes, text="Enviar Localização")
    enviar_localizacao_cb.pack(anchor="w", padx=10, pady=5)
    
    ativar_alarme_cb = customtkinter.CTkCheckBox(frame_acoes, text="Ativar Alarme")
    ativar_alarme_cb.pack(anchor="w", padx=10, pady=5)

    customtkinter.CTkButton(configuracoes, text="Salvar Configurações", command=lambda: print("Configurações salvas")).pack(padx=10, pady=10)
    customtkinter.CTkButton(configuracoes, text="Sair", command=lambda: exibir_tela_login(janela, exibir_tela_principal)).pack(padx=10, pady=10)

def adicionar_contato():
    nome = contato_entry.get()
    if nome:
        contatos.append(nome)
        atualizar_checkboxes()
        contato_entry.delete(0, 'end')

def atualizar_checkboxes():
    for widget in frame_contatos_checkboxes.winfo_children():
        widget.destroy()
    for contato in contatos:
        checkbox = customtkinter.CTkCheckBox(frame_contatos_checkboxes, text=contato)
        checkbox.pack(anchor="w", padx=10, pady=5)

def testar_buzzer():
    if arduino:
        arduino.write(b"BUZZER\n")
    else:
        print("Arduino não conectado.")

def ligar_led():
    if arduino:
        arduino.write(b"LED_ON\n")
    else:
        print("Arduino não conectado.")

def desligar_led():
    if arduino:
        arduino.write(b"LED_OFF\n")
    else:
        print("Arduino não conectado.")

def mostrar_localizacao():
    if arduino:
        arduino.write(b"LOCATION\n")
        location = arduino.readline().decode('utf-8').strip()
        print(f"Localização recebida: {location}")
    else:
        print("Arduino não conectado.")
