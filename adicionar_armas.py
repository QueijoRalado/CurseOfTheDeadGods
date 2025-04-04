import json

# ABRIR O ARQUIVO JSON E CARREGAR COMO UM DICIONÁRIO
with open("armasprimarias.json", "r", encoding="utf-8") as arquivo:
    armas = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armassecundarias.json", "r", encoding="utf-8") as arquivo:
    armas_s = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armasterciarias.json", "r", encoding="utf-8") as arquivo:
    armas_t = json.load(arquivo)  # Transforma o JSON em um dicionário Python
# EXEMPLO: Mostrar todas as categorias e armas
"""
for categoria, lista_armas in armas.items():
    print(f"Categoria: {categoria}")
    for arma in lista_armas:
        icone, nome, habilidade, dano, dano_critico = arma
        print(f" - {nome} | Habilidade: {habilidade} | Dano: {dano} | Dano Crítico: {dano_critico}")
"""
with open("teste_pras_armas.html",'w', encoding="utf-8") as file:
        file.write(
        """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Armas</title>
    <style rel="styleshet">
        table, tr, td{
            border: 1px solid purple;
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
                                       file.write(f'<td><img src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
                                       print(n, "N CARALHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                else:
                                        file.write(f'<td>{dado}</td>')
                                print(dado)
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
                                       file.write(f'<td><img src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
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
                                       file.write(f'<td><img src="{dado}" alt="" referrerpolicy="no-referrer"></td>')
                                else:
                                        file.write(f'<td>{dado}</td>')
                                n+=1
                        file.write('</tr>')
        
     # print(f"Categoria: {categoria}")
      #for arma in lista_armas:
       # icone, nome, habilidade, dano, dano_critico = arma
        #print(f" - {nome} | Habilidade: {habilidade} | Dano: {dano} | Dano Crítico: {dano_critico}")
"""
        n = 0
            for m in v:
                file.write(f'<tr>')
                file.write(f'<td>{materias[n]}</td>')
                confirmação=0
                for notis in v[materias[n]]:
                    if confirmação!=4:
                        file.write(f"<td>{str(notis)}</td>")
                    print(confirmação)
                    if confirmação==4:
                        if notis>=7:
                            file.write(f"<td class = 'aprovado'>{str(notis)}</td>")
                        elif notis<6:
                            file.write(f"<td class = 'reprovado'>{str(notis)}</td>")
                        else:
                            file.write(f"<td class = 'recuperacao'>{str(notis)}</td>")
                    confirmação+=1
                n+=1
                file.write(f'</tr>')
                """