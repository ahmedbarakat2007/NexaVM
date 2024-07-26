import os
import subprocess
import json
import flet as ft
import threading

file_path = "roms.json"


def load_contacts():
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
    return contacts


def started_signal(page: ft.Page, rom_name: str):
    page.pubsub.send_all(message=f"started")
    snackbar = ft.SnackBar(
        content=ft.Text(f"ROM '{rom_name}' started successfully! You can minimize this window"),
        show_close_icon=True,
        bgcolor=ft.colors.GREEN,
    )
    page.open(snackbar)
    page.update()

def stopped_signal(page: ft.Page, rom_name: str):
    page.pubsub.send_all(message=f"stopped")
    snackbar = ft.SnackBar(
        content=ft.Text(f"ROM '{rom_name}' has stopped running"),
        show_close_icon=True,
        bgcolor=ft.colors.ORANGE,
    )
    page.open(snackbar)
    page.update()

def run_qemu_process(command, page: ft.Page, rom_name: str):
    def run_process():
        process = os.popen(command)
        started_signal(page, rom_name)
        process.wait()
        stopped_signal(page, rom_name)

    thread = threading.Thread(target=run_process)
    thread.start()

def run_rom(item, page: ft.Page):
    try:
        (
            name,
            rom_os,
            arch,
            cdrom,
            hda,
            cpu,
            vga,
            icon,
            virtio,
            hyperv,
            ram,
            cores,
            threads,
        ) = item

        base_command = (
            f"-vga {vga} -m {ram} -cpu {cpu} "
            f"-smp threads={threads},cores={cores} "
            f'-name "{name}:Running" -display sdl'
        )

        # Updated network configuration
        base_command += " -netdev user,id=mynet0 -device virtio-net-pci,netdev=mynet0"

        if virtio == "true":
            virtio_devices = (
                " -device virtio-rng-pci -device virtio-scsi-pci "
                "-device virtio-balloon-pci -device virtio-serial-pci"
            )
            base_command += virtio_devices

        if arch == "x86":
            command = f"utils\\nexa-i386 {base_command} -bios Bios/nexa-x86-legacy.bin"
        elif arch == "x64":
            command = (
                f"utils\\nexa-x86_64 {base_command} -bios Bios/nexa-x86-legacy.bin"
            )
        elif arch in ["ARM", "ARM64"]:
            arm_type = "arm" if arch == "ARM" else "aarch64"
            command = (
                f"utils\\nexa-{arm_type} {base_command} "
                "-M virt -device nec-usb-xhci -device VGA -device usb-kbd "
                "-device usb-mouse -bios Bios/nexa-arm-efi.bin"
            )
        elif arch in ["PPC", "PPC64"]:
            ppc_type = "ppc" if arch == "PPC" else "ppc64"
            command = f"utils\\nexa-{ppc_type} {base_command}"
        else:
            raise ValueError(f"Unsupported architecture: {arch}")

        if cdrom != "Null":
            command += f' -cdrom "{cdrom}"'
        if hda != "Null":
            hda = hda.replace("\\", "/")  # Replace backslashes with forward slashes
            command += f' -drive file="{hda}",format=raw'

        if hyperv == "whpx":
            command += " -accel whpx,kernel-irqchip=off"
        elif hyperv == "tcg":
            command += " -accel tcg,thread=multi"

        run_qemu_process(command, page, name)

    except Exception as e:
        snackbar = ft.SnackBar(
            content=ft.Text(f"Error starting '{name}' - {e}"),
            show_close_icon=True,
            bgcolor=ft.colors.RED,
        )
        page.open(snackbar)
        page.update()


def add_rom(e, page):
    os.popen(["python", "rommaker.py"])
    contacts = load_contacts()
    update_contact_list(page, contacts)


def create_contact_list_item(item, page):
    return ft.ListTile(
        leading=ft.Image(src=item[7], fit="contain"),
        title=ft.Text(item[0]),
        subtitle=ft.Text(f"{item[1]} ({item[2]}), CPU: {item[5]}, RAM: {item[10]}MB"),
        trailing=ft.IconButton(
            icon=ft.icons.PLAY_ARROW,
            icon_color=ft.colors.GREEN,
            on_click=lambda _, item=item: run_rom(item, page),
        ),
    )


def update_contact_list(page: ft.Page, contacts):
    contact_list = page.get_control("contact_list")
    if contact_list is None:
        print("Error: contact_list not found")
        return

    contact_list.controls = [create_contact_list_item(item, page) for item in contacts]
    page.update()


def main(page: ft.Page):
    page.title = "ROM Launcher"
    page.vertical_alignment = page.horizontal_alignment = "center"

    contacts = load_contacts()

    contact_list = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        controls=[create_contact_list_item(item, page) for item in contacts],
    )
    contact_list.key = "contact_list"

    page.add(ft.Container(content=ft.Column(controls=[contact_list]), expand=True))

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=lambda e: add_rom(e, page)
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
