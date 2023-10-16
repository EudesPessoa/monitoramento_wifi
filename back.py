from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


lista_comparar = []
lista_atual = []
permitidos = {'pc_01': 'IP',
              'celular_01': 'IP',
              'celular_02': 'IP',
              'celular_03': 'IP',
              'pc_02': 'IP',
              'tv_01': 'IP',
              'tv_02': 'IP',
              'pc_03': 'IP',
              'repetidor': 'IP',
              'celular_04': 'IP'
              }


for x,y in permitidos.items():
    lista_atual.append(y)


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5)/20)


def iniciar_driver():	
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000']
    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.add_experimental_option('prefs', {
        # Notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos download
        'profile.default_content_setting_values.automatic_downloads': 1,
        # Remover todos os erros e avisos, 
        "excludeSwitches": ['disable-logging'],
    })
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


def Bloquear_IP():
    driver = iniciar_driver()
    driver.get(" ") # <<< COLOQUE O ENDEREÇO DO SEU MODEM 
    sleep(3)
    login = 'SEU LOGIN' # <<< COLOQUE O LOGIN DO SEU MODEM 
    password = 'SUA SENHA' # <<< COLOQUE A SENHA DO SEU MODEM 
    campo_login = driver.find_element(By.XPATH, "//input[@id='login']")
    sleep(3)
    campo_login.click()
    sleep(2)
    digitar_naturalmente(login, campo_login)
    sleep(4)
    campo_senha = driver.find_element(By.XPATH, "//input[@id='senha']")
    sleep(2)
    campo_senha.click()
    sleep(3)
    digitar_naturalmente(password, campo_senha)
    sleep(2)
    btn_entrar = driver.find_element(By.XPATH, "//button[@class='button icon']")
    btn_entrar.click()
    sleep(15)	
    print('acabou')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    end_mac = driver.find_elements(By.XPATH, "//table[@class='table']//tbody/tr")
    print(f'Tem {len(end_mac)} conectados')
    sleep(6)
    for element in end_mac:
        mac = element.find_element(By.XPATH, './td[4]').text
        lista_comparar.append(mac)
    lista_final = set(lista_comparar) - set(lista_atual)    
    qts_lista = len(lista_final)
    if qts_lista == 0:
        print('Sem Intrusos')
        sleep(2)
        driver.execute_script('window.scrollTo(0, 0);')
        sleep(3)
    else:
        for x in lista_final:
            print(f'Não tem acesso: {x}  BLOQUEAR')
        sleep(2)
        driver.execute_script('window.scrollTo(0, 0);')
        sleep(3)
        config_avan = driver.find_element(By.XPATH, "//a[@class='next config']")
        config_avan.click()
        sleep(5)
        btn_menu = driver.find_element(By.XPATH, "//span[@class='icon']")
        btn_menu.click()
        print('clicou no botão menu')
        sleep(3)
        btn_wifi = driver.find_element(By.XPATH, "//div[@class='wrapper-header']//div[@class='wrapper-menu']//ul/li/label[@for='menu-wi-fi']")
        btn_wifi.click()
        print('clicou no botão wifi')
        sleep(4)
        btn_wifi_conectados = driver.find_element(By.CSS_SELECTOR , "a[href*='page-wifi-connected-equip']")
        btn_wifi_conectados.click()
        print('clicou no botão conectados')
        sleep(5)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(3)
        num_conectados = driver.find_elements(By.XPATH, "//ul[@class='list']/li")
        range_conctados = int(len(num_conectados))
        for y1 in lista_final:
            print(y1)
            for y2 in range(range_conctados):
                ip_mac = num_conectados[y2].text.split('\n')[0].split(' ')[2]
                if ip_mac == y1:
                    print(f'Bloqueando {ip_mac}')
                    btn_bloquear = driver.find_element(
                        By.XPATH, f"//ul[@class='list']/li/strong//label[@for='select-check{y2}']")
                    btn_bloquear.click()
                    sleep(2)
                else:
                    pass
        sleep(5)
        btn_remover = driver.find_element(
            By.XPATH, f"//button[@id='remove-device']")
        btn_remover.click()
        sleep(60)
        driver.execute_script('window.scrollTo(0, 0);')
        sleep(3)
        btn_menu.click()
        print('clicou no botão menu')
        sleep(5)
        btn_config_rapida = driver.find_element(By.CSS_SELECTOR , "a[href*='page-quick-setup']")
        btn_config_rapida.click()
        print('clicou no btn_config_rapida')
        sleep(5)

    btn_sair = driver.find_element(By.XPATH, "//a[@class='next close']")
    btn_sair.click()
    sleep(5)
    driver.close

    fechar_programa = 'sim'

    return fechar_programa
