import flet as ft
from bancoDados import criar_banco, adicionar_usuario, validar_login

def main(page: ft.Page):
    criar_banco()
    
    # Define os contêineres
    left_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=1000,
        height=1000,
        content=ft.Column(
            controls=[ft.Image(src="PSI2.png", width=900, height=800)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    right_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=1000,
        height=1000,
    )

    page.add(
        ft.Row(
            controls=[left_container, right_container],
            expand=True,
        )
    )

    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    right_container.content = ft.Column(
        controls=[ola, botao_login(page)],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    page.update()  

def botao_login(page: ft.Page):
    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
            ft.TextField(label="Nome", bgcolor="white", width=850)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    senha_icon = ft.Icon(name=ft.icons.LOCK, size=20, color="blue")
    entrada_senha = ft.Row(
        controls=[
            senha_icon,
            ft.TextField(label="Senha", password=True, bgcolor="white", width=850)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: mostrar_registro(page))

    return ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            ft.Row(
                controls=[botao_entrar, botao_registrar],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def mostrar_registro(page: ft.Page):
    page.clean()

    ola = ft.Text(
        value="Tela de Registro", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
            ft.TextField(label="Nome de Usuário", bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    entrada_senha = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.LOCK, size=20, color="blue"),
            ft.TextField(label="Senha", password=True, bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: registrar_usuario(page, entrada_nome, entrada_senha))

    container_formulario = ft.Container(
        content=ft.Column(
            controls=[ola, entrada_nome, entrada_senha, botao_registrar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        width=400,
        height=400,
        alignment=ft.alignment.center
    )

    page.add(
        ft.Container(
            content=container_formulario,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.BLUE
        )
    )

    page.update()

def mostrar_opcoes(page: ft.Page):
    page.clean()

    ola = ft.Text(
        value="Menu", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    botao_opcao1 = ft.ElevatedButton("Pacientes", on_click=lambda e: print("Pacientes"))
    botao_opcao2 = ft.ElevatedButton("Anotações", on_click=lambda e: print("Anotações"))
    botao_opcao3 = ft.ElevatedButton("Horários", on_click=lambda e: print("Horários"))

    container_opcoes = ft.Container(
        content=ft.Column(
            controls=[ola, botao_opcao1, botao_opcao2, botao_opcao3],  # Incluindo os três botões
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        width=400,
        height=400,
        alignment=ft.alignment.center
    )

    page.add(
        ft.Container(
            content=container_opcoes,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.BLUE
        )
    )

    page.update()

def registrar_usuario(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    adicionar_usuario(nome, senha)
    page.add(ft.Text("Usuário registrado com sucesso!", color="green"))

    mostrar_login(page)

def validar_login_ui(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    if validar_login(nome, senha):
        mostrar_opcoes(page)  # Redireciona para a tela de opções
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))
    page.update()

ft.app(target=main)
