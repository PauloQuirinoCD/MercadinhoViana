import flet as ft


#imagen = 'Imagen.jpg'

lado_esquerdo = ft.Image(
        src=f"Imagen.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
)
lado_direito = ft.Container()


def menu(page: ft.Page):
    page.title = "Mercadinho Viana"
    page.bgcolor = '#338d94'
    
    layout = ft.Container(
        width=900,
        height=200,
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                lado_direito,
                lado_esquerdo
            ]
        )
    )



    page.add(layout)

    
ft.app(target=menu)
