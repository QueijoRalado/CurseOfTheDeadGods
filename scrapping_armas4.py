from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def buscar_armas():
    # Inicia o WebDriver
    driver = webdriver.Firefox()
    driver.get('https://curseofthedeadgods.fandom.com/wiki/Weapons')

    try:
        # Aguarda as tabelas carregarem completamente
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "fandom-table"))
        )

        # Força a rolagem para carregar todas as tabelas (caso haja lazy loading)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Espera um pouco para garantir que carregou

        tabelas_armas = driver.find_elements(By.CLASS_NAME, "fandom-table")
        
        armas = {}
        categoria_atual = None  # Categoria em andamento

        for tabela in tabelas_armas:
            linhas = tabela.find_elements(By.TAG_NAME, "tr")[1:]  # Ignorar cabeçalho
            
            for linha in linhas:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                print(f"Número de colunas encontradas: {len(colunas)}")

                # Se houver pelo menos 5 colunas (considerando o padrão da tabela)
                if len(colunas) >= 5:
                    # Caso a primeira célula não esteja vazia, significa que há uma nova categoria
                    if colunas[0].text.strip():
                        categoria_atual = colunas[0].text.strip()
                        if categoria_atual not in armas:
                            armas[categoria_atual] = []

                    # Verifica se há uma categoria válida antes de prosseguir
                    if categoria_atual is None:
                        continue  # Pula essa linha se não houver uma categoria válida definida

                    # Obtém o link do ícone da arma (se existir)
                    icone = ""
                    try:
                        figure = colunas[-5].find_element(By.TAG_NAME, "figure")
                        link_element = figure.find_element(By.TAG_NAME, "a")
                        icone = link_element.get_attribute("href")
                    except:
                        pass  # Se não encontrar o link, mantém icone como ""

                    # Coleta os outros dados (com verificação para evitar IndexError)
                    nome = colunas[-4].text.strip() if len(colunas) >= 4 else "Desconhecido"
                    habilidade = colunas[-3].text.strip() if len(colunas) >= 3 else "Nenhuma"
                    dano = colunas[-2].text.strip() if len(colunas) >= 2 else "0"
                    dano_critico = colunas[-1].text.strip() if len(colunas) >= 1 else "0"

                    # Exibe os dados para verificação
                    print("Categoria =", categoria_atual)
                    print("ICONE =", icone)
                    print("NOME =", nome)
                    print("HABILIDADE =", habilidade)
                    print("DANO =", dano)
                    print("DANO CRITICO =", dano_critico)
                    print("-" * 40)

                    # Adiciona a arma à sua respectiva categoria
                    armas[categoria_atual].append([icone, nome, habilidade, dano, dano_critico])

        # SALVAR EM UM ARQUIVO
        with open("armas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(str(armas))  # Usa `str()` para evitar problemas de formatação

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    buscar_armas()
