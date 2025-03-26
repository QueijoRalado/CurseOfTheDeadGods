from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





def buscar_armas():
    # Inicia o WebDriver
    driver = webdriver.Firefox()    
    driver.get('https://curseofthedeadgods.fandom.com/wiki/Weapons')    
    try:
        # Aguarda a div carregar
        tabela_armas = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fandom-table.wikitable "))
        )

        linhas = tabela_armas.find_elements(By.TAG_NAME, "tr")
        
        colunas = [th.text.strip() for th in linhas[0].find_elements(By.TAG_NAME, "th")]

        armas = []

        for linha in linhas:
            dados = [td for td in linha.find_elements(By.TAG_NAME, "td")]
           
            for dado in dados:
                armas.append((dado))

        print(armas)
        for arma in armas:
            if arma=="":
                pass
            else:
                print(arma)
                print("-----------")
            


    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    buscar_armas()