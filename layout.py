import flet as ft


lado1 = ft.Container(
    bgcolor=ft.colors.WHITE,
    width=400,
    height=400,
    content=ft.Text('aqui um lado')
)

lado2 = ft.Container(
    bgcolor=ft.colors.WHITE,
    width=400,
    height=400,
    content=ft.Text('aqui o outro lado')
)


def main(page: ft.Page):
    page.title='MercadinhoViana'
    page.bgcolor=ft.colors.BLACK
    page.update()

    layout = ft.Container(
        width=900,
        height=400,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=1,
            controls=[
                lado1, lado2
            ]
        )
    )


    page.add(
        layout
        )

ft.app(target=main)