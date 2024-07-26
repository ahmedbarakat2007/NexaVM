import flet as ft


def roms_page(page: ft.Page):

    rom_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                "Download", on_click=lambda _: page.go("/home")
                            ),
                            ft.TextButton("Install"),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    WindowsTab = ft.Tab(
        text="Windows",
        content=ft.Container(
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        rom_card,
                        col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                    ),
                    ft.Container(
                        rom_card,
                        col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                    ),
                    ft.Container(
                        rom_card,
                        col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                    ),
                    ft.Container(
                        rom_card,
                        col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                    ),
                    ft.Container(
                        rom_card,
                        col={"xs": 12, "sm": 10, "md": 6, "lg": 4, "xl": 3},
                    ),
                ],
            ),
            width="100%",
            height="100%",
            padding=10,
        ),
    )

    Tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        width="100%",
        tab_alignment=ft.TabAlignment.CENTER,
        divider_color=ft.colors.GREY_200,
        divider_height=2,
        tabs=[
            WindowsTab,
            ft.Tab(
                text="Mac",
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Linux",
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Android",
            ),
            ft.Tab(
                text="Others",
            ),
        ],
        expand=1,
    )

    page_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
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
                                    "Install New Rom",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLUE_500,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                            ft.OutlinedButton(
                                icon=ft.icons.INSTALL_DESKTOP,
                                text="Custom Rom",
                                on_click=lambda _: page.go("/customroms"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                ),
                                ),
                        ],
                    ),
                ),
                Tabs,
            ]
        )
    )
    return page_container
