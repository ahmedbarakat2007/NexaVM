import flet as ft
from utils import *


def team_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_team_card(name: str, role: str, image: str, portfolio_link: str):
        return ft.Card(
            show_border_on_foreground=True,
            variant=ft.CardVariant.OUTLINED,
            shape=ft.RoundedRectangleBorder(radius=15),
            width=200,
            elevation=10,
            color=page_color,
            height=250,
            content=ft.Column(
                tight=True,
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src=image,
                        width=100,
                        height=100,
                    ),
                    ft.Text(
                        value=name,
                        style=ft.TextStyle(
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ),
                    ft.Text(
                        value=role,
                        style=ft.TextStyle(
                            size=12,
                        ),
                    ),
                    ft.OutlinedButton(
                        text="Visit Portfolio",
                        url=portfolio_link,
                        style=ft.ButtonStyle(
                            color=ft.colors.WHITE,
                            side=ft.BorderSide(color=maincolor, width=1),
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                ],
            ),
        )

    ali_card = create_team_card(
        name="Ali Khan",
        role="Senior Developer/Designer",
        image="assets/alikhan.jpg",
        portfolio_link="https://portfoalio.vercel.app",
    )

    ahemad_card = create_team_card(
        name="Ahmed Barakat",
        role="Head/Programmer",
        image="assets/ahemad.png",
        portfolio_link="https://ahmedbarakat2007.github.io",
    )

    basedcat_card = create_team_card(
        name="BasedCat",
        role="Developer",
        image="assets/based.png",
        portfolio_link="https://portfoalio.vercel.app",
    )

    return ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                controls=[
                    ft.Container(
                        content=(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        on_click=lambda _:page.go("/home"),
                                        icon=ft.icons.ARROW_BACK,
                                    )
                                ]
                            )
                        )
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="The Minds Behind NexaVM",
                                    style=ft.TextStyle(
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    color=maincolor
                                ),
                                ft.Text(
                                    value="We are a team of passionate developers and designers who love to create beautiful and functional applications.",
                                    style=ft.TextStyle(
                                        size=17,
                                    ),
                                ),
                                ft.Row(
                                    controls=[ahemad_card, ali_card, basedcat_card],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Container(height=50)
                            ]
                        ),
                    ),
                ],
            )
        ),
    )
