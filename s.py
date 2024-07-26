import flet as ft
from utils import *
import json
from NexaVM import run_rom, add_rom

file_path = "roms.json"

with open(file_path, "r") as json_file:
    data = json.load(json_file)

contacts = []
for item in data:
    contacts.append(
        (
            item["rom-name"],
            item["rom-os"],
            item["rom-arch"],
            item["rom-iso"],
            item["rom-vhd"],
            item["rom-cpu"],
            item["rom-vga"],
            item["rom-img"],
            item["rom-virtio"],
            item["rom-hyperv"],
            item["rom-ram"],
            item["rom-cores"],
            item["rom-threads"],
        )
    )


def home_page(page: ft.Page):
    page.title = "NexaVM - Home"
    page.window.width = 1400
    page.window.height = 800
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.always_on_top = True
    config_text = ft.Text()
    config_image = ft.Container(
        border_radius=10,
        padding=10,
        content=ft.Image(
            height=100, width=100, src="assets/rom.png", fit=ft.ImageFit.CONTAIN
        ),
    )
    config_details = ft.Row()

    def create_list_tile(item):
        def update_config(item):
            try:
                config_text.value = item[0]  # Assuming item[0] is the rom-name
                config_image.content.src = item[7]  # Assuming item[7] is the rom-img
                config_details.controls.clear()
                config_details.controls.extend(
                    [
                        ft.Text(f"OS: {item[1]}"),
                        ft.Text(f"Architecture: {item[2]}"),
                        ft.Text(f"CPU: {item[5]}"),
                        ft.Text(f"VGA: {item[6]}"),
                        ft.Text(f"RAM: {item[10]}"),
                        ft.Text(f"Cores: {item[11]}"),
                        ft.Text(f"Threads: {item[12]}"),
                    ]
                )
            except (IndexError, KeyError):
                print("Error: Invalid item format.")
            finally:
                page.update()

        return ft.ListTile(
            leading=ft.Image(src=item[7], fit="contain"),
            on_click=lambda e, item=item: update_config(item),
            title=ft.Text(item[0]),
            trailing=ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color=ft.colors.GREEN,
                on_click=lambda e: run_rom(item, page),  # Capture item in closure
            ),
        )

    contact_list = ft.ListView(
        spacing=10,
        auto_scroll=True,
        controls=[create_list_tile(item) for item in contacts],
    )

    rail = ft.NavigationRail(
        bgcolor=ft.colors.TRANSPARENT,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.Column(
            controls=[
                ft.Container(
                    image_fit=ft.ImageFit.CONTAIN,
                    image_src="assets/logo.png",
                    width=100,
                    height=100,
                ),
                ft.FloatingActionButton(
                    icon=ft.icons.CREATE,
                    text="Add",
                    on_click=lambda e: page.go(ROUTE_ADD),
                ),
            ]
        ),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.FAVORITE,
                label="First",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    Homepage = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=(
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                expand=True,
                controls=(
                    ft.Container(
                        width=300,
                        content=rail,
                        gradient=ft.LinearGradient(
                            tile_mode=ft.GradientTileMode.CLAMP,
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=["#eceeee", "#e6ebef"],
                        ),
                    ),
                    ft.Container(
                        expand=True,
                        content=(
                            ft.Column(
                                expand=True,
                                controls=(
                                    ft.Container(
                                        height=200,
                                        gradient=ft.LinearGradient(
                                            tile_mode=ft.GradientTileMode.CLAMP,
                                            begin=ft.alignment.top_left,
                                            end=ft.alignment.bottom_right,
                                            colors=["#d5e4eb", "#d8d9db"],
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                ft.Text(
                                                    value="Rom Details",
                                                    style=ft.TextStyle(
                                                        letter_spacing=2
                                                    ),
                                                    weight=ft.FontWeight.BOLD,
                                                    color=APP_COLOR,
                                                    size=20,
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        config_image,
                                                        ft.Column(
                                                            controls=[
                                                                config_text,
                                                                config_details,
                                                            ]
                                                        ),
                                                    ],
                                                    alignment=ft.alignment.center,
                                                ),
                                            ]
                                        ),
                                        alignment=ft.alignment.top_left,
                                        padding=20,
                                    ),
                                    ft.Container(
                                        alignment=ft.alignment.top_left,
                                        padding=20,
                                        content=(
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        value="Avilable Roms",
                                                        weight=ft.FontWeight.BOLD,
                                                        size=20,
                                                    ),
                                                    ft.Column(
                                                        controls=[contact_list],
                                                        alignment=ft.alignment.top_left,
                                                    ),
                                                ]
                                            )
                                        ),
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
            )
        ),
    )
    return Homepage


def main(page: ft.Page):
    page.add(home_page(page))
    page.go("/home")


ft.app(target=main, assets_dir="assets")