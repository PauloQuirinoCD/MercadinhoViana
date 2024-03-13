import flet as ft

conteiner = ft.Container(

    ft.Column([
        ft.Container(
            ft.Image(
        src=f"Imagen.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
        ),
        padding=ft.padding.only(100)
        ),
        
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Login",
                border="underline",
                prefix_icon=ft.icons.EMAIL
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Senha", 
                border="underline",
                prefix_icon=ft.icons.LOCK,
                password=True
            ),
            padding=ft.padding.only(20,20)
        ),

        ft.Container(
            ft.Checkbox(
                label= "Salvar Senha",
                check_color= "Black"
            ),
            padding=ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="INICIAR",
                width=280,
                bgcolor="#28919e",
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="Novo Usuário",
                width=280,
                bgcolor="#338d94",
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.EMAIL,
                    tooltip="Email",
                    icon_size=35
                ),
                ft.IconButton(
                    icon=ft.icons.FACEBOOK,
                    tooltip="Facebook",
                    icon_size=35
                ),
                ft.IconButton(
                    icon=ft.icons.PHONE_ANDROID,
                    tooltip="Apple",
                    icon_size=35
                ),
            ], 
            alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(20,20) 
        ),
        
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),


    border_radius=20,
    width=320,
    height=500,
    gradient=ft.LinearGradient([
        '#28919e',
        '#59a4b0',
        '#338d94'
    ])
)

def main(page: ft.Page, view=ft.AppView.WEB_BROWSER):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.add(conteiner)


ft.app(target=main)
