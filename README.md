# Documentação do projeto Segurança em um clique: Inovação em segurança para mulheres

## Visão Geral

Este aplicativo é uma ferramenta focada em segurança, projetada para melhorar a segurança pessoal, particularmente para mulheres. Ele apresenta um sistema de login, gerenciamento de contatos, capacidades de teste de dispositivos e opções de configuração. O aplicativo é construído usando Python com a biblioteca CustomTkinter para a interface gráfica do usuário e inclui integração com um dispositivo Arduino para funcionalidades de hardware.

## Estrutura de Arquivos

O aplicativo consiste em dois arquivos Python principais:

1. `login.py`: O ponto de entrada do aplicativo
2. `telas.py`: Contém a funcionalidade principal, incluindo as telas de login e principal

## Script Principal (`login.py`)

```python
import customtkinter
from telas import exibir_tela_login

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def exibir_tela_principal(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    from telas import exibir_tela_principal
    exibir_tela_principal(janela)

janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("500x300")

exibir_tela_login(janela, exibir_tela_principal)
janela.mainloop()
```

### Funcionalidade

- Define o modo de aparência como "dark" e o tema de cor como "dark-blue"
- Define uma função `exibir_tela_principal` para mudar para a tela principal
- Cria a janela principal do aplicativo
- Chama `exibir_tela_login` para exibir a tela de login
- Inicia o loop de eventos principal

## Módulo Telas (`telas.py`)

### Importações e Configuração

```python
import customtkinter
import serial

try:
    arduino = serial.Serial('COM3', 9600)
except serial.SerialException:
    arduino = None
    print("Arduino não conectado. Algumas funcionalidades necessitam dele.")
```

- Importa os módulos necessários
- Tenta estabelecer uma conexão com um dispositivo Arduino

### Tela de Login

```python
def exibir_tela_login(janela, callback):
    # ... (configuração da interface de login)
```

- Limpa a janela atual
- Configura a interface de login com campos de e-mail e senha
- Inclui uma caixa de seleção "Lembre de mim"
- Fornece um botão de login que chama a função `callback` (tela principal)

### Tela Principal

```python
def exibir_tela_principal(janela):
    # ... (configuração da interface principal)
```

- Configura a interface principal com múltiplas abas:
  1. Contato
  2. Testes
  3. Sobre
  4. Configurações
- Implementa funcionalidades para cada aba

### Gerenciamento de Contatos

```python
def adicionar_contato():
    # ... (lógica de adição de contato)

def atualizar_checkboxes():
    # ... (lógica de atualização de checkboxes)
```

- Permite adicionar e exibir contatos
- Atualiza a lista de contatos dinamicamente

### Funções de Comunicação com Arduino

```python
def testar_buzzer():
    # ... (lógica de teste do buzzer)

def ligar_led():
    # ... (lógica para ligar LED)

def desligar_led():
    # ... (lógica para desligar LED)

def mostrar_localizacao():
    # ... (lógica de exibição de localização)
```

- Implementa funções para testar vários recursos de hardware:
  - Ativação do buzzer
  - Controle de LED
  - Recuperação de localização

## Uso

1. Execute `login.py` para iniciar o aplicativo
2. Faça login usando a tela de login
3. Navegue pelas abas na tela principal para acessar diferentes recursos
4. Use a aba "Configurações" para configurar o comportamento do aplicativo
5. Use a aba "Testes" para verificar a funcionalidade do hardware (requer conexão com Arduino)

## Dependências

- Python 3.x
- CustomTkinter
- pyserial (para comunicação com Arduino)

## Configuração

1. Instale as dependências necessárias:
   ```
   pip install customtkinter pyserial
   ```
2. Certifique-se de que um dispositivo Arduino esteja conectado (opcional, necessário para recursos de hardware)
3. Execute `login.py` para iniciar o aplicativo

## Notas

- O aplicativo tenta se conectar a um dispositivo Arduino na porta COM3. Ajuste a porta se necessário.
- Alguns recursos requerem um dispositivo Arduino conectado para funcionar corretamente.

