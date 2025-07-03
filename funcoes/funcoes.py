from selenium import webdriver
import time
import random
from datetime import datetime

from selenium import webdriver
import time
import random
from datetime import datetime

# Configurações iniciais
navegador = webdriver.Chrome()
count_comentario = 0

def log(mensagem):
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + mensagem)

def login():
    log("Acessando página do Instagram")
    navegador.get("https://www.instagram.com/")
    navegador.maximize_window()
    time.sleep(3)
    
    try:
        navegador.find_element('xpath', '//a[@href="/"]')
        log("Já está logado")
    except:
        log("Fazendo login")
        login = navegador.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        login.send_keys("login")
        senha = navegador.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        senha.send_keys("senha")
        botao_login = navegador.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[3]/button')
        botao_login.click()
        time.sleep(10)

def pagina_alvo():
    log("Acessando página do sorteio")
    navegador.get("https://www.instagram.com/p/teste/")
    time.sleep(5)

def comentar():
    global count_comentario
    
    try:
        comentario = navegador.find_element('css selector', 'textarea[placeholder="Adicione um comentário..."]')
        comentario.click()
        comentario.send_keys("Estou dentro! @pessoa1 @pessoa2 @pessoa3")
        
        botao_postar = navegador.find_element('xpath', '//div[@role="button" and contains(., "Postar")]')
        botao_postar.click()
        
        count_comentario += 1
        log(f"Comentário {count_comentario} postado com sucesso")
        
        delay = random.uniform(120, 300) 
        log(f"Próximo comentário em {int(delay/60)} minutos...")
        time.sleep(delay)
        
    except Exception as e:
        log(f"{str(e)}")
        time.sleep(60)