import os

# =========================
# FUNÇÕES DE USUÁRIO
# =========================

def cadastrar():

    print("""
========================
   CADASTRAR USUÁRIO
========================

0 - Voltar
""")

    usuario = input("Novo usuário: ").lower()

    if usuario == "0":
        return

    senha = input("Senha: ")

    if senha == "0":
        return

    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{usuario};{senha}\n")

    print(f"""
================================
Usuário {usuario} cadastrado!
================================
""")


def login():

    while True:

        print("""
========================
      LOGAR USUÁRIO
========================

0 - Voltar
""")

        usuario = input("Usuário: ").lower()

        if usuario == "0":
            return None

        senha = input("Senha: ")

        if senha == "0":
            return None

        try:

            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    dados = linha.strip().split(";")

                    if len(dados) != 2:
                        continue

                    u, s = dados

                    if usuario == u and senha == s:

                        print(f"""
================================
Bem-vindo {usuario}!
================================
""")

                        return usuario

                print("""
================================
Usuário ou senha incorretos!
================================
""")

        except FileNotFoundError:

            print("""
================================
Arquivo usuarios.txt não encontrado!
================================
""")


# =========================
# EXCLUIR USUÁRIO
# =========================

def excluir_usuario(usuario):

    while True:

        print(f"""
========================
     EXCLUIR USUÁRIO
========================

Usuário: {usuario}

1 - Confirmar exclusão
0 - Voltar
""")

        op = input("Escolha: ")

        if op == "0":
            return False

        elif op == "1":

            try:

                # REMOVE USUÁRIO
                novas_linhas = []

                with open("usuarios.txt", "r", encoding="utf-8") as arquivo:

                    for linha in arquivo:

                        dados = linha.strip().split(";")

                        if len(dados) != 2:
                            continue

                        u, senha = dados

                        if u != usuario:
                            novas_linhas.append(linha)

                with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
                    arquivo.writelines(novas_linhas)

                # REMOVE CURTIDAS
                if os.path.exists("curtidas.txt"):

                    novas_linhas = []

                    with open("curtidas.txt", "r", encoding="utf-8") as arquivo:

                        for linha in arquivo:

                            dados = linha.strip().split(";")

                            if len(dados) != 2:
                                continue

                            u, vid = dados

                            if u != usuario:
                                novas_linhas.append(linha)

                    with open("curtidas.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.writelines(novas_linhas)

                # REMOVE FAVORITOS
                if os.path.exists("favoritos.txt"):

                    novas_linhas = []

                    with open("favoritos.txt", "r", encoding="utf-8") as arquivo:

                        for linha in arquivo:

                            dados = linha.strip().split(";")

                            if len(dados) != 2:
                                continue

                            u, vid = dados

                            if u != usuario:
                                novas_linhas.append(linha)

                    with open("favoritos.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.writelines(novas_linhas)

                print(f"""
================================
Usuário {usuario} excluído!
================================
""")

                return True

            except FileNotFoundError:

                print("""
================================
Arquivo não encontrado!
================================
""")

        else:
            print("Opção inválida!")


# =========================
# LISTAR VÍDEOS
# =========================

def listar_videos(usuario):

    try:

        with open("videos.txt", "r", encoding="utf-8") as arquivo:

            videos = arquivo.readlines()

            if len(videos) == 0:
                print("Nenhum vídeo cadastrado!")
                return

            for linha in videos:

                dados = linha.strip().split(";")

                if len(dados) != 4:
                    continue

                id_video, nome, categoria, ano = dados

                while True:

                    print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}
================================
                    """)

                    print("1 - Curtir vídeo")
                    print("2 - Adicionar aos favoritos")
                    print("0 - Próximo vídeo")
                    print("9 - Voltar ao menu")

                    opcao = input("Escolha: ")

                    # CURTIR
                    if opcao == "1":

                        with open("curtidas.txt", "a", encoding="utf-8") as curtidas:
                            curtidas.write(f"{usuario};{id_video}\n")

                        print(f"""
================================
{nome} foi curtido com sucesso!
================================
""")

                    # FAVORITOS
                    elif opcao == "2":

                        with open("favoritos.txt", "a", encoding="utf-8") as favoritos:
                            favoritos.write(f"{usuario};{id_video}\n")

                        print(f"""
================================
{nome} foi adicionado aos favoritos!
================================
""")

                    # PRÓXIMO
                    elif opcao == "0":
                        break

                    # VOLTAR
                    elif opcao == "9":
                        return

                    else:
                        print("Opção inválida!")

    except FileNotFoundError:
        print("Arquivo videos.txt não encontrado!")


# =========================
# BUSCAR VÍDEO
# =========================

def buscar_video(usuario):

    while True:

        busca = input("""
========================
      BUSCAR VÍDEO
========================

Digite o nome do vídeo
0 - Voltar

Busca: """).lower()

        if busca == "0":
            return

        encontrou = False

        try:

            with open("videos.txt", "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    dados = linha.strip().split(";")

                    if len(dados) != 4:
                        continue

                    id_video, nome, categoria, ano = dados

                    if busca in nome.lower():

                        encontrou = True

                        # =========================
                        # VERIFICA CURTIDO
                        # =========================

                        curtido = False

                        if os.path.exists("curtidas.txt"):

                            with open("curtidas.txt", "r", encoding="utf-8") as curtidas:

                                for linha_curtida in curtidas:

                                    dados_curtida = linha_curtida.strip().split(";")

                                    if len(dados_curtida) != 2:
                                        continue

                                    u, vid = dados_curtida

                                    if u == usuario and vid == id_video:
                                        curtido = True
                                        break

                        # =========================
                        # VERIFICA FAVORITO
                        # =========================

                        favoritado = False

                        if os.path.exists("favoritos.txt"):

                            with open("favoritos.txt", "r", encoding="utf-8") as favoritos:

                                for linha_favorito in favoritos:

                                    dados_favorito = linha_favorito.strip().split(";")

                                    if len(dados_favorito) != 2:
                                        continue

                                    u, vid = dados_favorito

                                    if u == usuario and vid == id_video:
                                        favoritado = True
                                        break

                        while True:

                            print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}

Curtido: {"SIM" if curtido else "NÃO"}
Favoritado: {"SIM" if favoritado else "NÃO"}

================================
""")

                            print("1 - Curtir vídeo")
                            print("2 - Adicionar aos favoritos")
                            print("0 - Voltar")

                            opcao = input("Escolha: ")

                            # CURTIR
                            if opcao == "1":

                                with open("curtidas.txt", "a", encoding="utf-8") as curtidas:
                                    curtidas.write(f"{usuario};{id_video}\n")

                                curtido = True

                                print(f"""
================================
{nome} foi curtido com sucesso!
================================
""")

                            # FAVORITOS
                            elif opcao == "2":

                                with open("favoritos.txt", "a", encoding="utf-8") as favoritos:
                                    favoritos.write(f"{usuario};{id_video}\n")

                                favoritado = True

                                print(f"""
================================
{nome} foi adicionado aos favoritos!
================================
""")

                            # VOLTAR
                            elif opcao == "0":
                                break

                            else:
                                print("Opção inválida!")

            if not encontrou:

                print("""
================================
Nenhum vídeo encontrado!
================================
""")

        except FileNotFoundError:

            print("""
================================
Arquivo videos.txt não encontrado!
================================
""")


# =========================
# VER CURTIDOS
# =========================

def ver_curtidos(usuario):

    while True:

        encontrou = False
        curtidas_usuario = []

        print("""
========================
    VÍDEOS CURTIDOS
========================
""")

        try:

            with open("curtidas.txt", "r", encoding="utf-8") as curtidas:

                for linha in curtidas:

                    linha = linha.strip()

                    if linha == "":
                        continue

                    dados = linha.split(";")

                    if len(dados) != 2:
                        continue

                    u, id_video = dados

                    if u == usuario:
                        curtidas_usuario.append(id_video)

            with open("videos.txt", "r", encoding="utf-8") as videos:

                for linha in videos:

                    linha = linha.strip()

                    if linha == "":
                        continue

                    dados = linha.split(";")

                    if len(dados) != 4:
                        continue

                    id_video, nome, categoria, ano = dados

                    if id_video in curtidas_usuario:

                        encontrou = True

                        print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}
================================
                        """)

            if not encontrou:
                print("Você ainda não curtiu vídeos!")
                return

            print("Digite o ID do vídeo para mostrar as opções")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "0":
                break

            if escolha in curtidas_usuario:

                with open("videos.txt", "r", encoding="utf-8") as videos:

                    for linha in videos:

                        dados = linha.strip().split(";")

                        if len(dados) != 4:
                            continue

                        id_video, nome, categoria, ano = dados

                        if id_video == escolha:

                            while True:

                                print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}
================================
                                """)

                                print("1 - Remover curtida")
                                print("0 - Voltar")

                                op = input("Escolha: ")

                                if op == "1":

                                    novas_linhas = []

                                    with open("curtidas.txt", "r", encoding="utf-8") as arquivo:

                                        for linha in arquivo:

                                            dados = linha.strip().split(";")

                                            if len(dados) != 2:
                                                continue

                                            u, vid = dados

                                            if not (u == usuario and vid == escolha):
                                                novas_linhas.append(linha)

                                    with open("curtidas.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(novas_linhas)

                                    print("Curtida removida!")
                                    break

                                elif op == "0":
                                    break

                                else:
                                    print("Opção inválida!")

            else:
                print("ID inválido!")

        except FileNotFoundError:
            print("Arquivo não encontrado!")


# =========================
# VER FAVORITOS
# =========================

def ver_favoritos(usuario):

    while True:

        encontrou = False
        favoritos_usuario = []

        print("""
========================
       FAVORITOS
========================
""")

        try:

            with open("favoritos.txt", "r", encoding="utf-8") as favoritos:

                for linha in favoritos:

                    linha = linha.strip()

                    if linha == "":
                        continue

                    dados = linha.split(";")

                    if len(dados) != 2:
                        continue

                    u, id_video = dados

                    if u == usuario:
                        favoritos_usuario.append(id_video)

            with open("videos.txt", "r", encoding="utf-8") as videos:

                for linha in videos:

                    linha = linha.strip()

                    if linha == "":
                        continue

                    dados = linha.split(";")

                    if len(dados) != 4:
                        continue

                    id_video, nome, categoria, ano = dados

                    if id_video in favoritos_usuario:

                        encontrou = True

                        print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}
================================
                        """)

            if not encontrou:
                print("Você não possui favoritos!")
                return

            print("Digite o ID do vídeo para mostrar as opções")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "0":
                break

            if escolha in favoritos_usuario:

                with open("videos.txt", "r", encoding="utf-8") as videos:

                    for linha in videos:

                        dados = linha.strip().split(";")

                        if len(dados) != 4:
                            continue

                        id_video, nome, categoria, ano = dados

                        if id_video == escolha:

                            while True:

                                print(f"""
================================
ID: {id_video}
Nome: {nome}
Categoria: {categoria}
Ano: {ano}
================================
                                """)

                                print("1 - Remover favorito")
                                print("0 - Voltar")

                                op = input("Escolha: ")

                                if op == "1":

                                    novas_linhas = []

                                    with open("favoritos.txt", "r", encoding="utf-8") as arquivo:

                                        for linha in arquivo:

                                            dados = linha.strip().split(";")

                                            if len(dados) != 2:
                                                continue

                                            u, vid = dados

                                            if not (u == usuario and vid == escolha):
                                                novas_linhas.append(linha)

                                    with open("favoritos.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(novas_linhas)

                                    print("Favorito removido!")
                                    break

                                elif op == "0":
                                    break

                                else:
                                    print("Opção inválida!")

            else:
                print("ID inválido!")

        except FileNotFoundError:
            print("Arquivo não encontrado!")


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("""
========================
        FEItv
========================

1 - Cadastrar
2 - Login
0 - Sair
""")

    opcao = input("Escolha: ")

    # CADASTRAR
    if opcao == "1":
        cadastrar()

    # LOGIN
    elif opcao == "2":

        usuario_logado = login()

        if usuario_logado:

            while True:

                print(f"""
========================
      MENU FEItv
========================

Usuário logado: {usuario_logado}

1 - Listar vídeos
2 - Buscar vídeo
3 - Ver favoritos
4 - Ver curtidos
5 - Excluir usuário
0 - Logout
""")

                op = input("Escolha: ")

                # LISTAR
                if op == "1":
                    listar_videos(usuario_logado)

                # BUSCAR
                elif op == "2":
                    buscar_video(usuario_logado)

                # FAVORITOS
                elif op == "3":
                    ver_favoritos(usuario_logado)

                # CURTIDOS
                elif op == "4":
                    ver_curtidos(usuario_logado)

                # EXCLUIR USUÁRIO
                elif op == "5":

                    excluido = excluir_usuario(usuario_logado)

                    if excluido:
                        break

                # LOGOUT
                elif op == "0":
                    print("Logout realizado!")
                    break

                else:
                    print("Opção inválida!")

    # SAIR
    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")