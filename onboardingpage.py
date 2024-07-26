import flet as ft
from utils import *


def welcome_page(page: ft.Page):
    page.title = "NexaVM - Welcome"
    icon_path = "assets/trlogo.png"
    custom_icon = ft.Image(src=icon_path, width=32, height=32)
    page.add(custom_icon)
    page.update()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    # Header
    header = ft.Text(
        "Run Any OS Natively \n on NexaVM",
        size=40,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=maincolor,
    )

    description = ft.Text(
        "Perfectly Native | Boundlessly Versatile",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color=text_color,
    )

    version = ft.Text(
        "Version 0.0.1",
        size=15,
        text_align=ft.TextAlign.CENTER,
        color=text_color,
    )

    
    signup_button = ft.OutlinedButton(
        on_click=lambda _: page.go("/home"),
        text="Start",
        icon=ft.icons.ARROW_FORWARD,
        style=ft.ButtonStyle(
            side=ft.BorderSide(color=ft.colors.WHITE, width=1.5),
            color=ft.colors.WHITE, shape=ft.StadiumBorder(), bgcolor=maincolor
        ),
    )

    buttons = ft.Row(
        controls=[signup_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # Layout
    layout = ft.Container(
        image_src="assets/backg.jpg",
        image_fit=ft.ImageFit.FILL,
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Image(
                    src="assets/logo.png",
                    width=100,
                    height=100,
                ),
                description,
                header,
                buttons,
                version,
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
    return layout
