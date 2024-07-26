import flet as ft 
import time

def main(page: ft.Page):
    page.title = "Boost VPN"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 700
    page.window.width = 400
    appbar = ft.AppBar(
        title=ft.Text("BOOST VPN"),
        center_title=True,
        actions=(
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                content=ft.Text("Settings"),
                on_click=lambda _: print("Settings Pressed"),
            ),
        )
    )
    page.appbar = appbar
    
    animation = ft.Ref[ft.Lottie]()
    def boost(e):
        if animation.current.animate == False:
            animation.current.animate = True
            animation.current.update()

    container = ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=(
                ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Lottie(
                            ref=animation,
                            src="https://lottie.host/6fd72989-844c-46bf-9a56-e0ccf7ea3fbc/3jKjt0ORHb.json",
                            height=150,
                            width=150,
                            repeat=False,
                            animate=False
                        ),
                        ft.IconButton(
                            content=ft.Text("Boost"),
                            on_click=boost, 
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            height=50,
                            border=ft.border.all(color=ft.colors.RED, width=1),
                            bgcolor=ft.colors.with_opacity(color=ft.colors.RED, opacity=0.2),
                            content=ft.Text("Note: This is a Note", color=ft.colors.RED)
                        )
                    ]
                )
            )
        )
    page.add(container)

ft.app(target=main)