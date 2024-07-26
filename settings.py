import flet as ft


def settings_page(page: ft.Page):
    page.title = "Vectras Desktop - Settings"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    page_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        on_click=lambda _: page.go("/home"),
                                        left=True,
                                    ),
                                    ft.Container(
                                        expand=True,
                                        content=ft.Text(
                                            "Settings",
                                            size=30,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE_500,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ),
                                ],
                            ),
                            ft.Lottie(
                                src="https://lottie.host/a919da33-583c-4c58-81fc-292b6a9d9169/gViyJ5O8mP.json",
                                height=500,
                                width=500,
                                repeat=True,
                            ),
                            ft.Text("Page Under Construction", size=30),
                        ]
                    )
                ),
            ]
        )
    )
    return page_container
