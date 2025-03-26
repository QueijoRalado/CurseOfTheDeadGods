from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_armas():
    # Inicia o WebDriver
    driver = webdriver.Firefox()
    driver.get('https://curseofthedeadgods.fandom.com/wiki/Weapons')  # Verifique o link correto
    
    try:
        # Aguarda a tabela carregar
        tabela_armas = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fandom-table.wikitable"))
        )
        
        # Coleta todas as linhas da tabela
        linhas = tabela_armas.find_elements(By.TAG_NAME, "tr")
        
        armas = {}
        estilo_atual = None
        
        # Percorre as linhas ignorando o cabeçalho
        for linha in linhas[1:]:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            
            if len(colunas) == 5:  # Linha completa com Fighting Style
                estilo_atual = colunas[0].text
                nome = colunas[1].text
                habilidade = colunas[2].text
                dano = colunas[3].text
                dano_critico = (colunas[4].text) 
            
            elif len(colunas) == 4:  # Linha sem Fighting Style (continuação do estilo anterior)
                nome = colunas[0].text
                habilidade = colunas[1].text
                dano = (colunas[2].text) 
                dano_critico = (colunas[3].text) 
            
            else:
                continue  # Ignora linhas com formato inesperado
            
            # Adiciona ao dicionário
            if estilo_atual not in armas:
                armas[estilo_atual] = []
            
            armas[estilo_atual].append([nome, habilidade, dano, dano_critico])
        
        print(armas)

    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    buscar_armas()
