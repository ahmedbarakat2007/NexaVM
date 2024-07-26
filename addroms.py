import flet as ft
import os
import json
from utils import *


def addroms(page: ft.Page):
    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            if file_picker.data == "iso":
                iso_path_field.value = e.files[0].path
            elif file_picker.data == "hdd":
                hdd_path_field.value = e.files[0].path
            page.update()

    page.title = "NexaVM - Rom Maker"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 800
    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    page.overlay.append(file_picker)

    def pick_file(*file_type: str):
        return lambda _: file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=list(file_type),
        )

    def create_hdd(e):
        if rom_name.value == "":
            content.scroll_to(offset=0, duration=300)
            rom_name.error_text = "Please enter a name for the ROM"
            page.update()
        else:
            rom_name.error_text = None
            hdd_path = f"Roms\\{rom_name.value}\\{rom_name.value}.qcow2"
            os.makedirs("Roms\\" + rom_name.value + "\\")
            os.popen('utils\\nexa-img create -f qcow2 "' + hdd_path + '" 100G')
            hdd_path_field.value = hdd_path
            page.update()

    def choose_iso(e):
        file_picker.data = "iso"
        pick_file('iso')(e)

    def choose_hdd(e):
        file_picker.data = "hdd"
        pick_file('vhd', 'qcow2', 'vdi', 'vmdk')(e)

    def update_os_options(e):
        os_type = os_type_dropdown.value
        if os_type == "Windows":
            os_dropdown.options = [
                ft.dropdown.Option("Windows 9x"),
                ft.dropdown.Option("Windows XP"),
                ft.dropdown.Option("Windows Vista/7"),
                ft.dropdown.Option("Windows 8/10"),
                ft.dropdown.Option("Windows 11"),
                ft.dropdown.Option("Other"),
            ]
        elif os_type == "Linux":
            os_dropdown.options = [
                ft.dropdown.Option("Ubuntu"),
                ft.dropdown.Option("Debian"),
                ft.dropdown.Option("Fedora"),
                ft.dropdown.Option("CentOS"),
                ft.dropdown.Option("Arch Linux"),
                ft.dropdown.Option("Kali-Linux"),
                ft.dropdown.Option("Linux Mint"),
                ft.dropdown.Option("Other"),
            ]
        elif os_type == "Mac":
            os_dropdown.options = [
                ft.dropdown.Option("macOS 9x"),
                ft.dropdown.Option("macOS X"),
                ft.dropdown.Option("macOS"),
            ]
        else:
            os_dropdown.options = [
                ft.dropdown.Option("FreeBSD"),
                ft.dropdown.Option("OpenBSD"),
                ft.dropdown.Option("Haiku"),
                ft.dropdown.Option("BeOS"),
                ft.dropdown.Option("Other"),
            ]
        os_dropdown.value = None
        page.update()

    def update_arch_options(e):
        os_type = os_type_dropdown.value
        os_version = os_dropdown.value
        if os_type == "Windows":
            if os_version == "Windows 9x":
                arch_dropdown.options = [
                    ft.dropdown.Option("x86"),
                ]
            elif os_version == "Windows XP":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                ]
            elif os_version == "Windows Vista/7":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                ]
            elif os_version == "Windows 8/10":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("ARM"),
                    ft.dropdown.Option("ARM64"),
                ]
            elif os_version == "Windows 11":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("ARM64"),
                ]
            elif os_version == "Other":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("ARM"),
                    ft.dropdown.Option("ARM64"),
                    ft.dropdown.Option("PPC"),
                    ft.dropdown.Option("PPC64"),
                ]
        elif os_type == "Linux":
            arch_dropdown.options = [
                ft.dropdown.Option("x64"),
                ft.dropdown.Option("x86"),
                ft.dropdown.Option("ARM"),
                ft.dropdown.Option("ARM64"),
                ft.dropdown.Option("PPC"),
                ft.dropdown.Option("PPC64"),
            ]
        elif os_type == "Mac":
            if os_version == "macOS 9x":
                arch_dropdown.options = [
                    ft.dropdown.Option("x86"),
                ]
            elif os_version == "macOS X":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("PPC"),
                ]
            elif os_version == "macOS":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                ]
        elif os_type == "Other":
            if os_version == "FreeBSD":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("ARM"),
                    ft.dropdown.Option("ARM64"),
                    ft.dropdown.Option("PPC"),
                ]
            elif os_version == "OpenBSD":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("ARM"),
                    ft.dropdown.Option("ARM64"),
                    ft.dropdown.Option("PPC"),
                ]
            elif os_version == "Haiku":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                ]
            elif os_version == "BeOS":
                arch_dropdown.options = [
                    ft.dropdown.Option("PPC"),
                ]
            elif os_version == "Other":
                arch_dropdown.options = [
                    ft.dropdown.Option("x64"),
                    ft.dropdown.Option("x86"),
                    ft.dropdown.Option("ARM"),
                    ft.dropdown.Option("ARM64"),
                    ft.dropdown.Option("PPC"),
                    ft.dropdown.Option("PPC64"),
                ]
        arch_dropdown.value = None
        page.update()

    def add_img():
        os_type = os_type_dropdown.value
        os_version = os_dropdown.value
        img_path = "assets/roms-icons/placeholder.png"

        if os_type == "Windows":
            if os_version == "Windows 11":
                img_path = "assets/roms-icons/win11.png"
            elif os_version == "Windows 8/10":
                img_path = "assets/roms-icons/win10.png"
            elif os_version == "Windows Vista/7":
                img_path = "assets/roms-icons/win7.png"
            elif os_version == "Windows XP":
                img_path = "assets/roms-icons/winxp.png"
            elif os_version == "Windows 9x":
                img_path = "assets/roms-icons/win9x.png"
        elif os_type == "Linux":
            if os_version == "Ubuntu":
                img_path = "assets/roms-icons/ubuntu.png"
            elif os_version == "Debian":
                img_path = "assets/roms-icons/debian.png"
            elif os_version == "Fedora":
                img_path = "assets/roms-icons/fedora.png"
            elif os_version == "Kali-Linux":
                img_path = "assets/roms-icons/kali.png"
            elif os_version == "CentOS":
                img_path = "assets/roms-icons/cent.png"
            elif os_version == "Arch Linux":
                img_path = "assets/roms-icons/arch.png"
            elif os_version == "Linux Mint":
                img_path = "assets/roms-icons/mint.png"
        elif os_type == "Mac":
            if os_version == "macOS 9x":
                img_path = "assets/roms-icons/mac9.png"
            elif os_version == "macOS X":
                img_path = "assets/roms-icons/macx.png"
            elif os_version == "macOS":
                img_path = "assets/roms-icons/macos.png"

        return img_path

    def update_thread_slider_visibility(e):
        content.scroll_to(key=threads_slider.key, duration=300)
        threads_slider.visible = multithread_checkbox.value
        thread_slider_text.visible = multithread_checkbox.value
        page.update()

    def add_rom(e):
        # List of required fields
        required_fields = [
            (rom_name, "ROM Name"),
            (os_type_dropdown, "OS Type"),
            (os_dropdown, "OS Version"),
            (arch_dropdown, "Architecture"),
        ]

        # Check if all required fields are filled
        empty_fields = [field[1] for field in required_fields if not field[0].value]

        if empty_fields:
            error_message = f"Please fill in the following required fields: {', '.join(empty_fields)}"
            show_error_dialog(error_message)
            return

        rom_data = {
            "rom-name": rom_name.value,
            "rom-arch": arch_dropdown.value,
            "rom-cpu": "core2duo",
            "rom-cores": str(int(cores_slider.value)) if cores_slider.value else "1",
            "rom-threads": (
                str(int(threads_slider.value)) if multithread_checkbox.value else "1"
            ),
            "rom-ram": str(int(ram_slider.value)) if ram_slider.value else "2048",
            "rom-vhd": hdd_path_field.value,
            "rom-iso": iso_path_field.value,
            "rom-virtio": str(virtio_checkbox.value).lower(),
            "rom-vga": vga_dropdown.value if vga_dropdown.value else "std",
            "rom-hyperv": (str("whpx").lower() if hyperv_checkbox.value else "tcg"),
            "rom-img": add_img(),
            "rom-os": os_dropdown.value,
            "rom-network": (
                network_dropdown.value if network_dropdown.value else "e1000"
            ),
        }

        with open("roms.json", "r+") as f:
            data = json.load(f)
            data.append(rom_data)
            f.seek(0)
            json.dump(data, f, indent=4)

        show_success_dialog(rom_data)
        page.update()

    def show_error_dialog(message):
        dialog = ft.AlertDialog(
            title=ft.Text("Error", color=ft.colors.RED),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=lambda _: page.close(dialog))
            ],
        )
        page.open(dialog)
        page.update()

    def show_success_dialog(rom_data):
        dialog = ft.AlertDialog(
            title=ft.Text("ROM Created Successfully", color=ft.colors.GREEN),
            content=ft.Column([ft.Text(f"{k}: {v}") for k, v in rom_data.items()]),
            actions=[ft.TextButton("OK", on_click=lambda _: page.go("/home"))],
        )
        page.open(dialog)
        page.update()

    rom_name = ft.TextField(
        hint_text="Ex - Windows 11",
        focused_border_color=maincolor,
    )

    os_type_dropdown = ft.Dropdown(
        focused_border_color=maincolor,
        hint_text="Select OS Type",
        options=[
            ft.dropdown.Option("Windows"),
            ft.dropdown.Option("Linux"),
            ft.dropdown.Option("Mac"),
            ft.dropdown.Option("Other"),
        ],
        on_change=update_os_options,
    )

    os_dropdown = ft.Dropdown(
        focused_border_color=maincolor,
        hint_text="OS - Version",
        on_change=update_arch_options,
    )

    arch_dropdown = ft.Dropdown(
        focused_border_color=maincolor, hint_text="Architecture"
    )

    network_dropdown = ft.Dropdown(
        focused_border_color=maincolor,
        hint_text="Network Adapter",
        options=[
            ft.dropdown.Option("e1000"),
            ft.dropdown.Option("ne2k_pci"),
            ft.dropdown.Option("pcnet"),
            ft.dropdown.Option("virtio"),
        ],
    )
    thread_slider_text = ft.Text(
        "Threads (2 > or = 2)", color=ft.colors.GREY, visible=False
    )
    threads_slider = ft.Slider(
        key="threads_slider",
        min=2,
        max=32,
        divisions=31,
        value=4,
        label="{value} Threads",
        active_color=ft.colors.WHITE,
        visible=False,
    )

    ram_slider = ft.Slider(
        min=2000,
        max=16000,
        divisions=10,
        value=4000,
        label="{value}MB RAM",
        active_color=ft.colors.WHITE,
    )
    cores_slider = ft.Slider(
        min=1,
        max=16,
        divisions=10,
        value=2,
        label="{value} Cores",
        active_color=ft.colors.WHITE,
    )

    hdd_path_field = ft.TextField(hint_text="HDD Path", focused_border_color=maincolor)
    hdd_choose_button = ft.ElevatedButton(
        "Choose", on_click=choose_hdd, color=ft.colors.WHITE
    )
    hdd_create_button = ft.ElevatedButton(
        "Create", on_click=create_hdd, color=ft.colors.WHITE
    )
    hdd_row = ft.Row([hdd_choose_button, hdd_create_button])

    iso_path_field = ft.TextField(
        hint_text="Pah to ISO/CD", focused_border_color=maincolor
    )
    iso_choose_button = ft.ElevatedButton(
        "Choose", on_click=choose_iso, color=ft.colors.WHITE
    )

    vga_dropdown = ft.Dropdown(
        focused_border_color=maincolor,
        hint_text="VGA type",
        options=[
            ft.dropdown.Option("std"),
            ft.dropdown.Option("vmware"),
            ft.dropdown.Option("virtio"),
        ],
    )

    hyperv_checkbox = ft.Checkbox(active_color=maincolor, label="Hyper-V (Beta)")
    virtio_checkbox = ft.Checkbox(active_color=maincolor, label="VirtIO")
    multithread_checkbox = ft.Checkbox(
        active_color=maincolor,
        label="Multi-thread",
        on_change=update_thread_slider_visibility,
    )
    checkbox_row = ft.Row([hyperv_checkbox, virtio_checkbox, multithread_checkbox])

    content = ft.Column(
        controls=[
            ft.Text("ROM Name", color=ft.colors.GREY),
            rom_name,
            ft.Text("OS-Type", color=ft.colors.GREY),
            os_type_dropdown,
            os_dropdown,
            ft.Text("Architecture", color=ft.colors.GREY),
            arch_dropdown,
            ft.Row(
                [
                    ft.Text("RAM (In MB)", color=ft.colors.GREY),
                    ft.Tooltip(
                        message="Creating RAM equal or greater than your system ram may cause issues, its recommended to use 50-75% of your system ram. For example if you have 16 GB ram its recommended to use 8 GB ram and 12GB Maximum.",
                        content=ft.Icon(name=ft.icons.INFO_OUTLINE),
                    ),
                ]
            ),
            ram_slider,
            ft.Row(
                [
                    ft.Text("Cores", color=ft.colors.GREY),
                    ft.Tooltip(
                        message="4-12 (Recommended)",
                        content=ft.Icon(name=ft.icons.INFO_OUTLINE),
                    ),
                ]
            ),
            cores_slider,
            ft.Text("Choose Network Card", color=ft.colors.GREY),
            network_dropdown,
            ft.Row(
                [
                    ft.Text("Path to HDD", color=ft.colors.GREY),
                    ft.Tooltip(
                        message="(Recommended) Use Create button",
                        content=ft.Icon(name=ft.icons.INFO_OUTLINE),
                    ),
                ]
            ),
            hdd_path_field,
            hdd_row,
            ft.Text("Path to ISO/CD", color=ft.colors.GREY),
            iso_path_field,
            iso_choose_button,
            ft.Text("VGA", color=ft.colors.GREY),
            vga_dropdown,
            ft.Text(
                "Hyper-V may cause issues use at your own risk", color=ft.colors.GREY
            ),
            checkbox_row,
            thread_slider_text,
            threads_slider,
        ],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
    )

    scrollable_content = ft.Container(
        content=content,
        height=page.window.height - 200,  # Adjust this value as needed
    )

    return ft.Column(
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                content=(
                    ft.Text(
                        value="Add New ROM",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    )
                ),
            ),
            scrollable_content,
            ft.Container(
                content=ft.Column(
                    [
                        ft.Divider(color=ft.colors.TRANSPARENT),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Cancel",
                                    bgcolor="#1e1e1e",
                                    color=ft.colors.WHITE,
                                    on_click=lambda _: page.go("/home"),
                                ),
                                ft.ElevatedButton(
                                    "Add",
                                    bgcolor=maincolor,
                                    color=ft.colors.WHITE,
                                    on_click=add_rom,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
            ),
        ]
    )

