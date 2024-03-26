import flet as ft

def main(page: ft.Page):
    page.title='Mercadinho Viana'
    page.bgcolor=ft.colors.BLACK

    linha1 = ft.Container(
       bgcolor='#87CEFA',
       width=1000,
       height=150,
       content=ft.Row(
           [
               ft.Image(
                src='Imagen.jpg',
                border_radius=50,
                width=100,
                height=100
            ),
    
                ft.Text('Aqui ficarão as informações do cabeçalhos do sitema, e tasl ...')
           ],
           alignment=ft.MainAxisAlignment.SPACE_AROUND
        )     
    )

    coluna1 = ft.Container(
        alignment=ft.alignment.center,
        width=150,
        height=500,
        bgcolor='#87CEFA',
        content=ft.Column(
            [
                ft.TextButton('OPERADORA'),
                ft.TextButton('PRODUTO'),
                ft.TextButton('ESTOQUE'),
                ft.TextButton('CAIXA'),
                ft.TextButton('RELATÓRIO')
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )     
    )
    coluna2 = ft.Container(
        alignment=ft.alignment.center,
        width=845,
        height=500,
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            [
                ft.Text('AQUI FICA O CORPO DO SISTEMA...')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    linha2 = ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        width=1000,
        height=500,
        content=ft.Row(
            [
                coluna1,
                coluna2
            ]
        )
    )

    page.add(linha1, linha2)

ft.app(target=main)