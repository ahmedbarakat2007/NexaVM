import os
import subprocess
import json
import flet as ft

page = ft.Page

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

contact_list = ft.ListView(
    expand=True,
    spacing=10,
    auto_scroll=True,
    controls=[
        ft.ListTile(
            leading=ft.Image(src=item[7], fit="contain"),
            title=ft.Text(item[0]),
            subtitle=ft.Text(
                f"{item[1]} ({item[2]}), CPU: {item[5]}, RAM: {item[10]}MB"
            ),
            trailing=ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color=ft.colors.GREEN,
                on_click=lambda e: run_rom(item, page),
            ),
        )
        for item in contacts
    ],
)


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

        if virtio == "true":
            if cdrom == "Null":
                if arch == "x86":
                    os.popen(
                        r"utils\\nexa-i386 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + " -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "x64":
                    os.popen(
                        r"utils\\nexa-x86_64 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + " -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci ')
                elif arch == "ARM":
                    os.popen(
                        r"utils\\nexa-arm -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "ARM64":
                    os.popen(
                        r"utils\\nexa-aarch64 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                else:
                    snackbar = ft.SnackBar(
                        content=ft.Text("No Supported Architicture Found!!"),
                        show_close_icon=True,
                        bgcolor=ft.colors.RED,
                    )
                    page.open(snackbar)
                    page.update()
            elif cdrom == "Null":
                if arch == "x86":
                    os.popen(
                        r'utils\\nexa-i386 -hda "'
                        + hda
                        + '" -vga virtio -m '
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + " -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "x64":
                    os.popen(
                        r'utils\\nexa-x86_64 -hda "'
                        + hda
                        + '" -vga virtio -m '
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + " -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "ARM":
                    os.popen(
                        r'utils\\nexa-arm -hda "'
                        + hda
                        + '" -vga virtio -m '
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "ARM64":
                    os.popen(
                        r'utils\\nexa-aarch64 -hda "'
                        + hda
                        + '" -vga virtio -m '
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                else:
                    snackbar = ft.SnackBar(
                        content=ft.Text("No Supported Architicture Found!!"),
                        show_close_icon=True,
                        bgcolor=ft.colors.RED,
                    )
                    page.open(snackbar)
                    page.update()
            elif hda == "Null":
                if arch == "x86":
                    os.popen(
                        r"utils\\nexa-i386 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + ' -cdrom "'
                        + cdrom
                        + '" -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "x64":
                    os.popen(
                        r"utils\\nexa-x86_64 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=virtio -net user -accel "
                        + hyperv
                        + ' -cdrom "'
                        + cdrom
                        + '" -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "ARM":
                    os.popen(
                        r"utils\\nexa-arm -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + ' -net nic,model=virtio -net user -cdrom "'
                        + cdrom
                        + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                elif arch == "ARM64":
                    os.popen(
                        r"utils\\nexa-aarch64 -vga virtio -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + ' -net nic,model=virtio -net user -cdrom "'
                        + cdrom
                        + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl  -device virtio-rng-pci  -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci '
                    )
                else:
                    snackbar = ft.SnackBar(
                        content=ft.Text("No Supported Architicture Found!!"),
                        show_close_icon=True,
                        bgcolor=ft.colors.RED,
                    )
                    page.open(snackbar)
                    page.update()
            else:
                if arch == "x86":
                    os.popen(
                        r'utils\\nexa-i386 -hda "'
                        + hda
                        + '" -vga '
                        + vga
                        + " -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=e1000 -net user -accel "
                        + hyperv
                        + ' -cdrom "'
                        + cdrom
                        + '" -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci'
                    )
                elif arch == "x64":
                    os.popen(
                        r'utils\\nexa-x86_64 -hda "'
                        + hda
                        + '" -vga '
                        + vga
                        + " -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + " -net nic,model=e1000 -net user -accel "
                        + hyperv
                        + ' -cdrom "'
                        + cdrom
                        + '" -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci'
                    )
                elif arch == "ARM":
                    os.popen(
                        r'utils\\nexa-arm -hda "'
                        + hda
                        + '" -vga '
                        + vga
                        + " -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + ' -net nic,model=e1000 -net user -cdrom "'
                        + cdrom
                        + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci'
                    )
                elif arch == "ARM64":
                    os.popen(
                        r'utils\\nexa-aarch64 -hda "'
                        + hda
                        + '" -vga '
                        + vga
                        + " -m "
                        + str(ram)
                        + " -cpu "
                        + cpu
                        + ' -net nic,model=e1000 -net user -cdrom "'
                        + cdrom
                        + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                        + str(threads)
                        + ",cores="
                        + str(cores)
                        + ' -name "'
                        + name
                        + ':Running" -display sdl -device virtio-net-pci -device virtio-scsi-pci -device virtio-balloon-pci -device virtio-serial-pci'
                    )
                else:
                    snackbar = ft.SnackBar(
                        content=ft.Text("No Supported Architicture Found!!"),
                        show_close_icon=True,
                        bgcolor=ft.colors.RED,
                    )
                    page.open(snackbar)
                    page.update()
        else:
            try:
                if hda == "Null" and cdrom == "Null":
                    if arch == "x86":
                        os.popen(
                            r"utils\\nexa-i386 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "x64":
                        os.popen(
                            r"utils\\nexa-x86_64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "PPC":
                        os.popen(
                            r"utils\\nexa-ppc -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user "
                            + '-name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "PPC64":
                        os.popen(
                            r"utils\\nexa-ppc64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM":
                        os.popen(
                            r"utils\\nexa-arm -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM64":
                        os.popen(
                            r"utils\\nexa-aarch64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    else:
                        snackbar = ft.SnackBar(
                            content=ft.Text("No Supported Architicture Found!!"),
                            show_close_icon=True,
                            bgcolor=ft.colors.RED,
                        )
                        page.open(snackbar)
                        page.update()
                elif cdrom == "Null":
                    if arch == "x86":
                        os.popen(
                            r'utils\\nexa-i386 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "x64":
                        os.popen(
                            r'utils\\nexa-x86_64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "PPC":
                        os.popen(
                            r'utils\\nexa-ppc -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user "
                            + '-name "'
                            + name
                            + ':Running -display sdl"'
                        )
                    elif arch == "PPC64":
                        os.popen(
                            r'utils\\nexa-ppc64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -name "'
                            + name
                            + ':Running -display sdl"'
                        )
                    elif arch == "ARM":
                        os.popen(
                            r'utils\\nexa-arm -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM64":
                        os.popen(
                            r'utils\\nexa-aarch64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    else:
                        snackbar = ft.SnackBar(
                            content=ft.Text("No Supported Architicture Found!!"),
                            show_close_icon=True,
                            bgcolor=ft.colors.RED,
                        )
                        page.open(snackbar)
                        page.update()
                elif hda == "Null":
                    if arch == "x86":
                        os.popen(
                            r"utils\\nexa-i386 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + ' -cdrom "'
                            + cdrom
                            + '" -smp threads='
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "x64":
                        os.popen(
                            r"utils\\nexa-x86_64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + ' -cdrom "'
                            + cdrom
                            + '" -smp threads='
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "PPC":
                        os.popen(
                            r"utils\\nexa-ppc -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -cdrom "'
                            + cdrom
                            + '" -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "PPC64":
                        os.popen(
                            r"utils\\nexa-ppc64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -cdrom "'
                            + cdrom
                            + '" -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM":
                        os.popen(
                            r"utils\\nexa-arm -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -cdrom "'
                            + cdrom
                            + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM64":
                        os.popen(
                            r"utils\\nexa-aarch64 -vga "
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + ' -net nic,model=e1000 -net user -cdrom "'
                            + cdrom
                            + '" -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads='
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    else:
                        snackbar = ft.SnackBar(
                            content=ft.Text("No Supported Architicture Found!!"),
                            show_close_icon=True,
                            bgcolor=ft.colors.RED,
                        )
                        page.open(snackbar)
                        page.update()
                else:
                    if arch == "x86":
                        os.popen(
                            r'utils\\nexa-i386 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -cdrom "
                            + cdrom
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "x64":
                        os.popen(
                            r'utils\\nexa-x86_64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -accel "
                            + hyperv
                            + " -cdrom "
                            + cdrom
                            + " -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -bios Bios/nexa-x86-legacy.bin -display sdl'
                        )
                    elif arch == "PPC":
                        os.popen(
                            r'utils\\nexa-ppc -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -cdrom "
                            + cdrom
                            + " "
                            + '-name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "PPC64":
                        os.popen(
                            r'utils\\nexa-ppc64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -cdrom "
                            + cdrom
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM":
                        os.popen(
                            r'utils\\nexa-arm -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -cdrom "
                            + cdrom
                            + " -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    elif arch == "ARM64":
                        os.popen(
                            r'utils\\nexa-aarch64 -hda "'
                            + hda
                            + '" -vga '
                            + vga
                            + " -m "
                            + str(ram)
                            + " -cpu "
                            + cpu
                            + " -net nic,model=e1000 -net user -cdrom "
                            + cdrom
                            + " -M virt -device nec-usb-xhci -device VGA -device usb-kbd -device usb-mouse -display stdio -bios Bios/nexa-arm-efi.bin -smp threads="
                            + str(threads)
                            + ",cores="
                            + str(cores)
                            + ' -name "'
                            + name
                            + ':Running" -display sdl'
                        )
                    else:
                        snackbar = ft.SnackBar(
                            content=ft.Text("No Supported Architicture Found!!"),
                            show_close_icon=True,
                            bgcolor=ft.colors.RED,
                        )
                        page.open(snackbar)
                        page.update()
            except FileNotFoundError as e:
                snackbar = ft.SnackBar(
                    content=ft.Text(f"Error: File not found - {e}"),
                    show_close_icon=True,
                    bgcolor=ft.colors.RED,
                )
                page.open(snackbar)
                page.update()
            except ValueError as e:
                snackbar = ft.SnackBar(
                    content=ft.Text(f"Error: Invalid Value - {e}"),
                    show_close_icon=True,
                    bgcolor=ft.colors.RED,
                )
                page.open(snackbar)
                page.update()
            except Exception as e:
                snackbar = ft.SnackBar(
                    content=ft.Text(f"Somethign Went Wrong - {e}"),
                    close_icon_color=True,
                    bgcolor=ft.colors.RED,
                )
                page.open(snackbar)
                page.update()
        page.pubsub.send_all(message="started")
        snackbar = ft.SnackBar(
                content=(ft.Text("Rom started successfully! You can minimize this window")),
                show_close_icon=True,
                bgcolor=ft.colors.GREEN,
            )
        page.open(snackbar)
        page.update()
    except Exception as e:
        snackbar = ft.SnackBar(
            content=ft.Text("Error - {e}"),
            show_close_icon=True,
            bgcolor=ft.colors.RED,
        )
        page.open(snackbar)
        page.update()
        


def add_rom(e, page):
    subprocess.run(["python", "rommaker.py"])
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    contacts.clear()
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
    contact_list.items = [
        ft.ListTile(
            leading=ft.Image(src=item[7], fit="contain"),
            title=ft.Text(item[0]),
            subtitle=ft.Text(
                f"{item[1]} ({item[2]}), CPU: {item[5]}, RAM: {item[10]}MB"
            ),
            trailing=ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color=ft.colors.GREEN,
                on_click=lambda e: run_rom(item, page),
            ),
        )
        for item in contacts
    ]
    page.update()


def main(page: ft.Page):
    page.title = "ROM Launcher"
    page.vertical_alignment = "center"

    page.horizontal_alignment = page.vertical_alignment = "center"

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_rom
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

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    contact_list,
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
