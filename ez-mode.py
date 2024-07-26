import json
import os
import shutil
import multiprocessing
file_path = 'roms.json'

# Open the local JSON file for reading
with open(file_path, 'r') as json_file:
    # Parse the JSON content of the file into a Python dictionary
    data = json.load(json_file)

# Now 'data' is a Python dictionary containing the JSON data

# generate sample data
contacts = []
for item in data:
    contacts.append((item["rom-name"], item["rom-os"], item["rom-arch"],item["rom-iso"],item["rom-vhd"],item["rom-cpu"],item["rom-vga"],item["rom-img"],item["rom-virtio"],item["rom-hyperv"],item["rom-ram"],item["rom-cores"]))


def addRom():

        new_row = {
            "rom-name": str(nameAdd),
            "rom-arch": str(archAdd),
            "rom-cpu": str(cpuAdd),
            "rom-cores": str(coresAdd),
            "rom-threads": str(threadsAdd),
            "rom-ram": str(ramAdd),
            "rom-vhd": str(vhdAdd),
            "rom-iso": str(isoAdd),
            "rom-virtio": str(virtioAdd),
            "rom-vga": str(vgaAdd),
            "rom-hyperv": str(hypervAdd),
            "rom-img": str(iconAdd),
            "rom-os": str(osAdd)
        }

        # Append the new row to the data
        data.append(new_row)

        # Write the updated JSON data back to the file
        with open('roms.json', 'w') as file:
            json.dump(data, file, indent=4)
        
print("Choose the name for OS")
nameAdd = input("")
print("Choose OS You Want")
print("1) Windows")
print("2) Mac OS")
print("3) Linux")
print("4) Other")
osinput = input ()
if osinput == "1":
    print("Choose Windows Version")
    print("1) Windows 9X or NT (3.X, 4, 5)")
    print("2) Windows XP or Vista")
    print("3) Windows 7 or 8 or 8.1 or 10")
    print("4) Windows 11")
    print("5) Windows 10 ARM or Windows RT")
    print("6) Windows 11 Arm")
    print("7) Other")
    choise = input()
    if choise == "1":
        
        archAdd = "x86"
        osAdd = "Windows"
        cpuAdd = "pentium"
        vgaAdd = "cirrus"
        iconAdd = "Textures/roms-icons/win9x.png"
        coresAdd = "1"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "tcg"
    if choise == "2":
        archAdd = "x86_64"
        osAdd = "Windows"
        cpuAdd = "core2duo"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/winxp.png"
        coresAdd = "2"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "tcg"
    if choise == "3":
        
        archAdd = "x86_64"
        osAdd = "Windows"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/win10.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "4":

        archAdd = "x86_64"
        osAdd = "Windows"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/win11.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "5":
        
        archAdd = "aarch64"
        osAdd = "Windows"
        cpuAdd = "Haswell"
        vgaAdd = "virtio"
        iconAdd = "Textures/roms-icons/win10.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "6":
        
        archAdd = "aarch64"
        osAdd = "Windows"
        cpuAdd = "Haswell"
        vgaAdd = "virtio"
        iconAdd = "Textures/roms-icons/win10.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "7":

        archAdd = "x86_64"
        osAdd = "Windows"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/winother.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "whpx"
        
    
if osinput == "2":
    print("Choose Mac OS Version")
    print("1) Mac OS 9.X")
    print("2) Mac OS X PPC")
    print("3) Mac OS X x86 (10.5 - 10.10) (Hackintosh ISO ONLY)")
    print("4) Other")
    choise = input()
    if choise == "1":
        
        archAdd = "PPC"
        osAdd = "Mac OS"
        cpuAdd = "g3"
        vgaAdd = "std"
        iconAdd = "Textures/roms-icons/mac9.png"
        coresAdd = "1"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "tcg"
    if choise == "2":
        
        archAdd = "PPC"
        osAdd = "Mac OS"
        cpuAdd = "g4"
        vgaAdd = "std"
        iconAdd = "Textures/roms-icons/macx.png"
        coresAdd = "1"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "tcg"
    if choise == "3":
        archAdd = "x86_64"
        osAdd = "Mac OS"
        cpuAdd = "core2duo"
        vgaAdd = "std"
        iconAdd = "Textures/roms-icons/mac10.png"
        coresAdd = "1"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "tcg"

    if choise == "4":
        
        archAdd = "x86_64"
        osAdd = "Mac OS"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/mac10.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "whpx"
    
if osinput == "3":
    print("Choose Linux Version")
    print("1) Ubuntu Based")
    print("2) Debian Based")
    print("3) Arch Based ")
    print("4) Fedora-Redhat Based")
    print("5) SuSE Based")
    print("6) Other")
    choise = input()
    if choise == "1":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/ubuntu.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "2":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/debian.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "3":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/arch.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "4":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/redhat.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
    if choise == "5":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/ubuntu.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
        
    if choise == "6":
        
        archAdd = "x86_64"
        osAdd = "Linux"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/linux.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "true"
        hypervAdd = "whpx"
        
    
if osinput == "4":
    print("Choose The OS")
    print("1) FreeBSD Based")
    print("2) BeOS PPC")
    print("3) Haiku")
    print("4) Other")
    choise = input()
    if choise == "1":
        
        archAdd = "x86_64"
        osAdd = "Other"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/freebsd.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "whpx"
    if choise == "2":
        
        archAdd = "PPC"
        osAdd = "Other"
        cpuAdd = "Haswell"
        vgaAdd = "std"
        iconAdd = "Textures/roms-icons/beos.png"
        coresAdd = "1"
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "false"
    if choise == "3":
        ramAdd = input ("Type the Amount of Ram you Want in MB> ")
        print("What do you Want do with VHD? (Type the Number)>")   
        print("1) Create a New One")
        print("2) Use an Existing One")
        print("3) I Don't Need One Right Now")
        
        vhdinput = input ("")
        os.mkdir ("Roms/" + nameAdd)
        if vhdinput == "1":
            size = input ("How much Size Do you Want in GB?> ")
            os.popen('utils\\nexa-img create -f qcow2 "Roms\\'+ nameAdd + '\\' + nameAdd + '.qcow2" ' + size + 'G')
            vhdAdd= "Roms\\" + nameAdd + "\\" + nameAdd + ".qcow2"
        elif vhdinput == "2":
            vhd = input ("Type Here the Path of the Existing (QCOW2, VHD, VMDK) File> ")
            shutil.copy(vhd, "Roms/"+ nameAdd)
            file_path = vhd
            file_name = os.path.basename(file_path)
            vhdAdd = "Roms/" + nameAdd + "/" + file_name
        elif vhdinput == "3":
            vhdAdd = "Null"
        else:
            print("Wrong Value")
        archAdd = "x86_64"
        osAdd = "Other"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/haiku.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "whpx"

        print("What do you Want do with ISO? (Type the Number)>")   
        print("1) Use an Existing One")
        print("2) I Don't Need One Right Now")
        
        isoinput = input ("")

        if isoinput == "1":
            iso = input ("Type Here the Path of the Existing ISO File> ")
            shutil.copy(iso, "Roms\\"+ nameAdd)
            file_path = iso
            file_name = os.path.basename(file_path)
            isoAdd = "Roms\\" + nameAdd + "\\" + file_name
        elif isoinput == "2":
            isoAdd = "Null"
        else:
            print("Wrong Value")
    if choise == "4":
        
        archAdd = "x86_64"
        osAdd = "other"
        cpuAdd = "Haswell"
        vgaAdd = "vmware"
        iconAdd = "Textures/roms-icons/other.png"
        coresAdd = str(multiprocessing.cpu_count())
        threadsAdd = "1"
        virtioAdd = "false"
        hypervAdd = "whpx"

ramAdd = input ("Type the Amount of Ram you Want in MB> ")
print("What do you Want do with VHD? (Type the Number)>")   
print("1) Create a New One")
print("2) Use an Existing One")
print("3) I Don't Need One Right Now")
        
vhdinput = input ("")
os.mkdir ("Roms/" + nameAdd)
if vhdinput == "1":
            size = input ("How much Size Do you Want in GB?> ")
            os.popen('utils\\nexa-img create -f qcow2 "Roms\\'+ nameAdd + '\\' + nameAdd + '.qcow2" ' + size + 'G')
            vhdAdd= "Roms\\" + nameAdd + "\\" + nameAdd + ".qcow2"
elif vhdinput == "2":
            vhd = input ("Type Here the Path of the Existing (QCOW2, VHD, VMDK) File> ")
            shutil.copy(vhd, "Roms/"+ nameAdd)
            file_path = vhd
            file_name = os.path.basename(file_path)
            vhdAdd = "Roms/" + nameAdd + "/" + file_name
elif vhdinput == "3":
            vhdAdd = "Null"
else:
    print("Wrong Value (Set Default to No VHD)")
    vhdAdd = "Null"

print("What do you Want do with ISO? (Type the Number)>")   
print("1) Use an Existing One")
print("2) I Don't Need One Right Now")
        
isoinput = input ("")

if isoinput == "1":
            iso = input ("Type Here the Path of the Existing ISO File> ")
            shutil.copy(iso, "Roms\\"+ nameAdd)
            file_path = iso
            file_name = os.path.basename(file_path)
            isoAdd = "Roms\\" + nameAdd + "\\" + file_name
elif isoinput == "2":
            isoAdd = "Null"
else:
    print("Wrong Value (Set Default to No CDROM)")
    isoAdd = "Null"
addRom()
print (nameAdd +" Rom Has Been Created Successfully")
input("Press Enter to Exit.... ")