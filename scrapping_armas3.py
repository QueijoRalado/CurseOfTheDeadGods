from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_armas():
    # Inicia o WebDriver
    driver = webdriver.Firefox()
    driver.get('https://curseofthedeadgods.fandom.com/wiki/Weapons')
    categorias = []
    elementos = []
    categoria = ""
    
    try:
        # Aguarda as tabelas carregarem
        tabelas_armas = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "fandom-table.wikitable"))
        )
        
        armas = {}
        for tabela in tabelas_armas:
            #Coleta todas as linhas da tabela
            linhas = tabela.find_elements(By.TAG_NAME, "tr")[1:]  # Ignorar cabeçalho

            
            for linha in linhas:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                print(f"Número de colunas encontradas: {len(colunas)}")
                if len(colunas[0].text.strip())>0:
                    categoria = (colunas[0].text.strip())
                    if categoria!= None:
                        categorias.append(categoria)
                        #print(categoria)
                #print("Categoria = ", categorias)
                
                if categoria not in armas:
                    armas[categoria] = []

                if len(colunas) >=4: #para evitar linhas em brancos
                    # Obtém o link do ícone da arma
                    icone = ""
                    try:
                        figure = colunas[-5].find_element(By.TAG_NAME, "figure")
                        link_element = figure.find_element(By.TAG_NAME, "a")
                        icone = link_element.get_attribute("href")
                    except:
                        pass  # Se não encontrar o link, mantém icone como ""              
                    #print(icone)
                    nome = colunas[-4].text.strip()
                    habilidade = colunas[-3].text.strip()
                    dano = colunas[-2].text.strip()
                    dano_critico = colunas[-1].text.strip()
                    
                    print("Categoria = ", categoria)
                    print("ICONE =", icone)
                    print("NOME = ", nome)
                    print("HABILIDADE = ", habilidade)
                    print("DANO = ", dano)
                    print("DANO CRITICO =", dano_critico)
                
                    armas[categoria].append([icone, nome, habilidade, dano, dano_critico])
                    
                    #armas[categoria].append([nome, habilidade, dano, dano_critico])
                       
            #armas[categoria].append([icone, nome, habilidade, dano, dano_critico])
        
        #print(armas)
            #SALVAR EM UM ARQUIVO
        with open("armas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{armas}")
        
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    buscar_armas()
