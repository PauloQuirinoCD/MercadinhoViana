import flet as ft

def main(page: ft.Page):
    page.title='Mercadinho Viana'
    page.bgcolor=ft.colors.BLACK

    menu = ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        width=550,
        height=400,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    ft.Image(
                        src="Imagen.jpg"
                    ),
                    ft.ElevatedButton("PRIMEIRO BOTÃO", icon=ft.icons.PHONE_IN_TALK_ROUNDED)
                ),
            ]
        )
        
    )

    page.add(menu)

ft.app(target=main)