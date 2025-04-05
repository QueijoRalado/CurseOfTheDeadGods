import json

# ABRIR O ARQUIVO JSON E CARREGAR COMO UM DICIONÁRIO
with open("armasprimarias.json", "r", encoding="utf-8") as arquivo:
    armas = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armassecundarias.json", "r", encoding="utf-8") as arquivo:
    armas_s = json.load(arquivo)  # Transforma o JSON em um dicionário Python

with open("armasterciarias.json", "r", encoding="utf-8") as arquivo:
    armas_t = json.load(arquivo)  # Transforma o JSON em um dicionário Python
# EXEMPLO: Mostrar todas as categorias e armas

with open("lista_de_armas.html",'w', encoding="utf-8") as file:
        file.write(
        """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="../img/icone.webp" type="image/webp">
    <title>Lista De Armas</title>
    <link rel="stylesheet" type="text/css" href="../css/estilo.css">
<style>
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
}

table {
    border-collapse: collapse;
    width: 90%;
    max-width: 1000px;
    margin: 20px 0;
    text-align: center;
    border: 3px solid #6a0dad;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 0 15px rgba(106, 13, 173, 0.2);
}

tr {
    height: 80px;
}



th, td {
    border: 1px solid #c084fc;
    padding: 15px 20px;
    min-width: 150px;
    word-wrap: break-word;
    white-space: normal;
    vertical-align: middle;
    font-size: 1.1em;
}

th {
    background-color: #6a0dad;
    color: white;
    font-weight: bold;
    font-size: 1.2em;
}
</style>

</head>
<body>
    <p class="armas_aura">ARMAS PRIMÁRIAS</p>
"""
)
        
        for categoria, lista_armas in armas.items():
                file.write(
        f'''
        <table>
        <caption style="font-size: xx-large;">{categoria}</caption>
        <tr>
                <th>ÍCONE</th>
                <th>NOME</th>
                <th>HABILIDADE</th>
                <th>DANO</th>
                <th>CUSTO</th>
        </tr>
        '''
        )
                file.write(
                       f"""
                <img src="../img/separador.webp" alt="">
                <p class="armas_aura">{categoria}</p>
                """
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
                <th>ÍCONE</th>
                <th>NOME</th>
                <th>HABILIDADE</th>
                <th>DANO</th>
                <th>CUSTO</th>
        </tr>
        '''
                )
                if categoria=="Pistolas":
                        file.write("""
                <p class="armas_aura">ARMAS SECUNDÁRIAS</p>
                """)
                        
                file.write(
                       f"""
                <img src="../img/separador.webp" alt="">
                <p class="armas_aura">{categoria}</p>
                """
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
                <th>ÍCONE</th>
                <th>NOME</th>
                <th>HABILIDADE</th>
                <th>DANO</th>
                <th>CUSTO</th>
        </tr>
        '''
        )
                if categoria=="Lanças":
                        file.write("""
                <p class="armas_aura">ARMAS DE DUAS MÃOS</p>
                """)
                
                file.write(
                       f"""
                <img src="../img/separador.webp" alt="">
                <p class="armas_aura">{categoria}</p>
                """
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
                file.write(
                       """
                </table>
"""
                )
        
        file.write(
            """
    <div style="text-align: center; margin: 50px 0;">
        <a href="armas.html">
            <img src="../img/logobss.webp" alt="Voltar à página principal" style="width: 200px;">
        </a>
    </div>
</body>
</html>
"""
        )

