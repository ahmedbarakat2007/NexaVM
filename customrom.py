import flet as ft
from typing import Optional

def custom_roms_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Vectras Desktop - Custom ROMs"

    selected_file: Optional[ft.FilePickerResultEvent] = None
    page.window_height = 800

    def pick_files_result(e: ft.FilePickerResultEvent):
        nonlocal selected_file
        selected_file = e

        if e.files and len(e.files) > 0:
            rom_image.content.src = e.files[0].path
            rom_image.content.update()
        else:
            rom_image.content.src = "assets/placeholder.png"
            rom_image.content.update()

    pick_image = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_image)
    rom_name = ft.TextField(label="Rom Name", prefix_icon=ft.icons.EDIT)
    rom_icon = ft.TextField(label="Rom Icon", prefix_icon=ft.icons.IMAGE, suffix_icon=ft.icons.EDIT)
    rom_drive = ft.TextField(label="Rom Drive", prefix_icon=ft.icons.STORAGE)
    cd_rom = ft.TextField(label="CD Rom (iso only)", prefix_icon=ft.icons.ALBUM)
    qemu_params = ft.TextField(label="Qemu Params", prefix_icon=ft.icons.MEMORY)
    import_button = ft.CupertinoButton("Import", on_click=lambda _: pick_image.pick_files(), width=450, bgcolor = ft.colors.BLUE_500)
    add_button = ft.OutlinedButton("Add", on_click=lambda _: print("Add"), width=450, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))

    rom_image = ft.Container(
        width=450,
        height=200,
        border=ft.border.all(2, ft.colors.BLACK),
        content=ft.Image(src="assets/placeholder.png"),
        on_click=lambda _: pick_image.pick_files(
            allow_multiple=False, allowed_extensions=["jpg", "png", "gif"]
        ),
    )

    rom_container = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=450,
            controls=[
                rom_image,
                rom_name,
                rom_icon,
                rom_drive,
                cd_rom,
                qemu_params,
                import_button,
                add_button,
            ]
        )
    )

    page_container = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda _: page.go("/roms"),
                                left=True,
                            ),
                            ft.Container(
                                expand=True,
                                content=ft.Text(
                                    "Install Custom Rom",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLUE_500,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    width=500,
                    padding=10,
                    border=ft.border.all(2, ft.colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                    content=ft.Row(
                        expand=False,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            rom_container,
                        ],
                    ),
                ),
            ]
        )
    )

    return page_container
