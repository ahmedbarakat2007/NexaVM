import flet as ft
from utils import *
import json
from NexaVM import run_rom
import os

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
    icon_path = "assets/trlogo.png"
    custom_icon = ft.Image(src=icon_path, width=32, height=32)
    page.add(custom_icon)
    page.window.width = 1400
    page.window.height = 800
    page.theme_mode = ft.ThemeMode.DARK
    config_text = ft.Text(overflow=ft.TextOverflow.FADE, width=100, max_lines=2)
    config_image = ft.Container(
        border_radius=10,
        padding=10,
        content=ft.Image(
            height=80, width=80, src="assets/rom.png", fit=ft.ImageFit.CONTAIN
        ),
    )
    config_details = ft.Row(wrap=True)

    global contacts
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

    def handle_dlg_action_clicked(e):
        page.close(dlg)
        dlg.data.confirm_dismiss(e.control.data)
        page.update()

    dlg = ft.AlertDialog(
        shape=ft.RoundedRectangleBorder(radius=10),
        modal=True,
        title=ft.Text("Please confirm 🚨"),
        content=ft.Text("Do you really want to delete this item?"),
        actions=[
            ft.TextButton("Yes", data=True, on_click=handle_dlg_action_clicked),
            ft.TextButton("No", data=False, on_click=handle_dlg_action_clicked),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    def handle_confirm_dismiss(e: ft.DismissibleDismissEvent):
        if e.direction == ft.DismissDirection.END_TO_START:  # right-to-left slide
            dlg.data = e.control
            page.update()
            page.open(dlg)
            page.update()
        else:  # left-to-right slide
            page.go("/settings")
            e.control.confirm_dismiss(False)

    def handle_dismiss(e):
        dismissed_item = e.control.data  # Get the full item data
        rom_name = dismissed_item[0]

        # Remove the item from the contacts list
        global contacts
        contacts = [contact for contact in contacts if contact[0] != rom_name]

        # Remove the ROM data from the JSON file
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        data = [item for item in data if item["rom-name"] != rom_name]

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        # Delete the qcow2 file
        qcow2_path = f"Roms\\{rom_name}\\{rom_name}.qcow2"
        if os.path.exists(qcow2_path):
            os.remove(qcow2_path)

        # Remove the ROM folder if it's empty
        rom_folder = f"Roms\\{rom_name}"
        if os.path.exists(rom_folder) and not os.listdir(rom_folder):
            os.rmdir(rom_folder)

        # Remove the dismissed item from the UI
        e.control.parent.controls.remove(e.control)

        # Update the page
        page.update()
    def on_signal(msg):
        if msg == "started":
            signaltext.current.value = "Running"
            signaltext.current.color = ft.colors.GREEN
        else:
            signaltext.current.value = "Stopped"
            signaltext.current.color = ft.colors.RED
        page.update()
    page.pubsub.subscribe(on_signal)
    signaltext = ft.Ref[ft.Text]()

    def create_list_tile(item):
        def update_config(item):
            try:
                config_text.value = item[0]  
                config_image.content.src = item[7]
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

        return ft.Dismissible(
            data=item,
            background=ft.Container(
                border_radius=8,
                padding=20,
                alignment=ft.alignment.center_left,
                bgcolor=ft.colors.GREEN,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Icon(name=ft.icons.SETTINGS, color=ft.colors.WHITE),
                        ft.Text("Settings"),
                    ],
                ),
            ),
            on_dismiss=handle_dismiss,
            on_confirm_dismiss=handle_confirm_dismiss,
            secondary_background=ft.Container(
                border_radius=8,
                padding=20,
                alignment=ft.alignment.center_right,
                bgcolor=ft.colors.RED,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Text("Delete"),
                        ft.Icon(name=ft.icons.DELETE, color=ft.colors.WHITE),
                    ],
                ),
            ),
            dismiss_thresholds={
                ft.DismissDirection.END_TO_START: 0.6,
                ft.DismissDirection.START_TO_END: 0.6,
            },
            dismiss_direction=ft.DismissDirection.HORIZONTAL,
            content=ft.Container(
                height=100,
                alignment=ft.alignment.center,
                on_click=lambda e, item=item: update_config(item),
                bgcolor=ft.colors.BLACK,
                border_radius=8,
                padding=ft.padding.only(left=20, right=20),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=30,
                            controls=[
                                ft.Container(image_src=item[7], height=50, width=50),
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            item[0], size=16, weight=ft.FontWeight.BOLD
                                        ),
                                        ft.Text(
                                            ref=signaltext,
                                            value="Not Started Yet",
                                            color=ft.colors.RED
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ],
                        ),
                        ft.ElevatedButton(
                            text="Launch",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                bgcolor=maincolor,
                                padding={ft.MaterialState.DEFAULT: 15},
                            ),
                            on_click=lambda e: run_rom(item, page),
                        ),
                    ],
                ),
            ),
        )

    contact_list = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.HIDDEN,
        spacing=10,
        controls=[create_list_tile(item) for item in contacts],
    )
    contact_list.controls = [create_list_tile(item) for item in contacts]

    def change_destination(e):
        if e.control.selected_index == 0:
            page.go("/home")
        elif e.control.selected_index == 1:
            page.go("/team")

    rail = ft.NavigationRail(
        indicator_shape=ft.RoundedRectangleBorder(radius=10),
        indicator_color=ft.colors.with_opacity(color=maincolor, opacity=0.5),
        expand=True,
        bgcolor=ft.colors.TRANSPARENT,
        selected_index=0,
        extended=True,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.Row(
            alignment=ft.alignment.center,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(width=10),
                ft.Container(
                    image_fit=ft.ImageFit.CONTAIN,
                    image_src="assets/trlogo.png",
                    width=100,
                    height=100,
                ),
                ft.Text(value="NexaVM", size=30, weight=ft.FontWeight.BOLD),
            ],
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                label="Home",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PEOPLE_OUTLINE_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.PEOPLE),
                label_content=ft.Text("Team"),
            ),
        ],
        on_change=lambda e: change_destination(e),
    )
    live_replay = ft.Container(
        padding=10,
        height=200,
        width=300,
        border_radius=15,
        bgcolor=page_color,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=(
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.COMPUTER, color=maincolor),
                        ft.Text("LIVE PREVIEW", weight=ft.FontWeight.BOLD, size=12),
                    ]
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    border=ft.border.all(color=ft.colors.WHITE, width=1),
                    expand=False,
                    height=150,
                    width=270,
                    bgcolor=ft.colors.BLACK,
                    border_radius=15,
                    content=ft.Text("Coming Soon")
                ),
            ),
        ),
        alignment=ft.alignment.center,
    )
    page.window.always_on_top = True
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
                        border_radius=15,
                        width=300,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                rail,
                                ft.FloatingActionButton(
                                    bgcolor=maincolor,
                                    icon=ft.icons.ADD,
                                    text="ADD NEW ROM",
                                    on_click=lambda e: page.go(ROUTE_ADD),
                                ),
                                ft.Container(height=20),
                            ],
                        ),
                        bgcolor=page_color,
                    ),
                    ft.Container(
                        expand=True,
                        content=(
                            ft.Column(
                                expand=True,
                                controls=(
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                expand=True,
                                                border_radius=15,
                                                height=200,
                                                bgcolor=page_color,
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            value="Rom Details",
                                                            style=ft.TextStyle(
                                                                letter_spacing=2
                                                            ),
                                                            weight=ft.FontWeight.BOLD,
                                                            color=text_color,
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
                                            live_replay,
                                        ]
                                    ),
                                    ft.Container(
                                        expand=True,
                                        bgcolor=page_color,
                                        border_radius=15,
                                        padding=20,
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Text(
                                                            value="Virtual Machines",
                                                            weight=ft.FontWeight.BOLD,
                                                            size=20,
                                                        ),
                                                        ft.Tooltip(
                                                            message="All the avilable virtual machines will appear here, to delete hold and slide from right to left",
                                                            content=ft.Icon(
                                                                name=ft.icons.INFO_OUTLINE,
                                                                color=maincolor,
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                contact_list,
                                            ],
                                            spacing=20,
                                            expand=True,
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
