import json

# ABRIR O ARQUIVO JSON E CARREGAR COMO UM DICIONÁRIO
with open("armasprimarias.json", "r", encoding="utf-8") as arquivo:
    armas = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armassecundarias.json", "r", encoding="utf-8") as arquivo:
    armas_s = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armasterciarias.json", "r", encoding="utf-8") as arquivo:
    armas_t = json.load(arquivo)  # Transforma o JSON em um dicionário Python
# EXEMPLO: Mostrar todas as categorias e armas

with open("teste_pras_armas.html",'w', encoding="utf-8") as file:
        file.write(
        """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Armas</title>
    <style>
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
        font-family: Arial, sans-serif;
    }

    table {
        border-collapse: collapse;
        width: 80%;
        max-width: 800px;
        margin: 20px 0;
        text-align: center;
    }

    th, td {
        border: 1px solid purple;
        padding: 10px;
    }
        </style>
</head>
<body>
    <h2>ARMAS PRIMÁRIAS</h2>
    <hr>
"""
)
        
        for categoria, lista_armas in armas.items():
                file.write(
        f'''
        <table>
        <caption style="font-size: xx-large;">{categoria}</caption>
        <tr>
                <th>Ícone</th>
                <th>Nome</th>
                <th>Habilidade</th>
                <th>Dano</th>
                <th>Custo</th>
        </tr>
        '''
        )
                for arma in lista_armas:
                        file.write('<tr>')
                        n=1
                        for dado in arma:
                                if n==1:
                                       file.write(f'<td><img style="width: 130px" src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
                                else:
                                        file.write(f'<td>{dado}</td>')
                                n+=1
                        file.write('</tr>')
        
        for categoria, lista_armas in armas_s.items():
                file.write(
        f'''
        <table>
        <caption style="font-size: xx-large;">{categoria}</caption>
        <tr>
                <th>Ícone</th>
                <th>Nome</th>
                <th>Habilidade</th>
                <th>Dano</th>
                <th>Custo</th>
        </tr>
        '''
        )
                for arma in lista_armas:
                        file.write('<tr>')
                        n=1
                        for dado in arma:
                                if n==1:
                                       file.write(f'<td><img style="width: 130px" src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
                                else:
                                        file.write(f'<td>{dado}</td>')
                                n+=1
                        file.write('</tr>')
        
        for categoria, lista_armas in armas_t.items():
                file.write(
        f'''
        <table>
        <caption style="font-size: xx-large;">{categoria}</caption>
        <tr>
                <th>Ícone</th>
                <th>Nome</th>
                <th>Habilidade</th>
                <th>Dano</th>
                <th>Custo</th>
        </tr>
        '''
        )
                for arma in lista_armas:
                        file.write('<tr>')
                        n=1
                        for dado in arma:
                                if n==1:
                                       file.write(f'<td><img style="width: 130px" src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
                                else:
                                        file.write(f'<td>{dado}</td>')
                                n+=1
                        file.write('</tr>')