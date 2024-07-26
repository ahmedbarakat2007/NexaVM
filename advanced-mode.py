import json
import os
import shutil

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
        print (str(nameAdd))
        data.append(new_row)

        # Write the updated JSON data back to the file
        with open('roms.json', 'w') as file:
            json.dump(data, file, indent=4)
        


    
nameAdd = input ("Type The Rom Name> ")

print("Choose the OS (Type the Number)>")
print("1) Windows")
print("2) Mac OS")
print("3) Linux")
print("4) Other")

osinput = input ("")

if osinput == "1":
    
    osAdd="Windows"
    
    print("Choose the Archeticture (Type the Number)>")   
    print("1) x86")
    print("2) x86_64")
    print("3) ARM")
    print("4) AARCH64")
    
    archinput = input ("")
    
    if archinput == "1": 
        
        archAdd = "x86"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core Duo")
        print("2) Atom N270")
        print("3) Pentium 2")
        print("4) Pentium 3")
        print("5) Pentium")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'coreduo'
        elif cpuinput == "2":
            cpuAdd = 'n270'
        elif cpuinput == "3":
            cpuAdd = 'pentium2'
        elif cpuinput == "4":
            cpuAdd = 'pentium3'
        elif cpuinput == "5":
            cpuAdd = 'pentium'
        else:
            print("Wrong Value (Choosing Default '1')")
            cpuAdd='coreduo'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd = "1"
        
        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "2": 
        
        archAdd = "x86_64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core 2 Duo")
        print("2) Intel Haswell")
        print("3) qemu64")
        print("4) max")
        print("5) EPYC")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'core2duo'
        elif cpuinput == "2":
            cpuAdd = 'Haswell'
        elif cpuinput == "3":
            cpuAdd = 'qemu64'
        elif cpuinput == "4":
            cpuAdd = 'max'
        elif cpuinput == "5":
            cpuAdd = 'epyc'
        else:
            print("Wrong Value (Choosing Default '4')")
            cpuAdd='max'

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "3": 
        
        archAdd = "ARM"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd = "cortex-a57"

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        vgaAdd = "virtio"
        hypervAdd = "tcg"

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "4": 
        
        archAdd = "ARM64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")

        cpuinput = input ("")
    
        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd = "cortex-a57"   

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        vgaAdd = "virtio"
        hypervAdd = "tcg"
        
        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'

    else:
        print("Wrong Value (Choosing Default '2')")
        archAdd = "x86_64"
    
    


elif osinput == "2": 
    
    osAdd="Mac OS"

    print("Choose the Archeticture (Type the Number)>")   
    print("1) x86")
    print("2) x86_64")
    print("3) PPC")
    
    archinput = input ("")
    
    if archinput == "1": 
        
        archAdd = "x86"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core Duo")
        print("2) Atom N270")
        print("3) Pentium 2")
        print("4) Pentium 3")
        print("5) Pentium")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'coreduo'
        elif cpuinput == "2":
            cpuAdd = 'n270'
        elif cpuinput == "3":
            cpuAdd = 'pentium2'
        elif cpuinput == "4":
            cpuAdd = 'pentium3'
        elif cpuinput == "5":
            cpuAdd = 'pentium'
        else:
            print("Wrong Value (Choosing Default ('1')")
            cpuAdd="coreduo"

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Choose the GPU Model (Type the Number)>")   
        print("1) std")
        print("2) Vmware S-VGA")
        print('3) QXL')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'std'
        elif vgainput == "2":
            vgaAdd = 'vmware'
        elif vgainput == "3":
            vgaAdd = 'qxl'
        else:
            print("Wrong Value (Choosing Default '1')")
            vgaAdd="std"
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "2": 
        
        archAdd = "x86_64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core 2 Duo")
        print("2) Intel Haswell")
        print("3) qemu64")
        print("4) max")
        print("5) EPYC")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'core2duo'
        elif cpuinput == "2":
            cpuAdd = 'Haswell'
        elif cpuinput == "3":
            cpuAdd = 'qemu64'
        elif cpuinput == "4":
            cpuAdd = 'max'
            cpuAdd = 'epyc'
        else:
            print("Wrong Value (Choosing Default '4')")
            cpuAdd='max'

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Choose the GPU Model (Type the Number)>")   
        print("1) std")
        print("2) Vmware S-VGA")
        print('3) QXL')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'std'
        elif vgainput == "2":
            vgaAdd = 'vmware'
        elif vgainput == "3":
            vgaAdd = 'qxl'
        else:
            print("Wrong Value (Choosing Default '1')")
            vgaAdd="std"

        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "3": 
        
        archAdd = "PPC"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) G3")
        print("2) G4")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'g3'
        elif cpuinput == "2":
            cpuAdd = 'g4'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd = 'g4'

        vgaAdd = "std"
        virtioAdd = "false"
        hypervAdd = "tcg"
        coresAdd="1"
        threadsAdd="1"

    else:
        print("Wrong Value (Set Default to '2')")
        archAdd="x86_64"

elif osinput == '3': 
    
    osAdd="Linux"

    print("Choose the Archeticture (Type the Number)>")   
    print("1) x86")
    print("2) x86_64")
    print("3) ARM")
    print("4) AARCH64")
    print("5) PPC")
    print("6) PPC64")
    
    archinput = input ("")
    
    if archinput == "1": 
        
        archAdd = "x86"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core Duo")
        print("2) Atom N270")
        print("3) Pentium 2")
        print("4) Pentium 3")
        print("5) Pentium")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'coreduo'
        elif cpuinput == "2":
            cpuAdd = 'n270'
        elif cpuinput == "3":
            cpuAdd = 'pentium2'
        elif cpuinput == "4":
            cpuAdd = 'pentium3'
        elif cpuinput == "5":
            cpuAdd = 'pentium'
        else:
            print("Wrong Value (Choosing Default '1')")
            cpuAdd='coreduo'

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "2":
        
        archAdd = "x86_64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core 2 Duo")
        print("2) Intel Haswell")
        print("3) qemu64")
        print("4) max")
        print("5) EPYC")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'core2duo'
        elif cpuinput == "2":
            cpuAdd = 'Haswell'
        elif cpuinput == "3":
            cpuAdd = 'qemu64'
        elif cpuinput == "4":
            cpuAdd = 'max'
            cpuAdd = 'epyc'
        else:
            print("Wrong Value (Choosing Default '4')")
            cpuAdd='max'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "3": 
        
        archAdd = "ARM"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='cortex-a57'

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'

        vgaAdd = "virtio"
        hypervAdd="tcg"
    
    elif archinput == "4": 
        
        archAdd = "ARM64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='cortex-a57'

        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
        
        vgaAdd = "virtio"
    
    elif archinput == "5": 
        
        archAdd = "PPC"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) G3")
        print("2) G4")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'g3'
        elif cpuinput == "2":
            cpuAdd = 'g4'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='g4'
        
        vgaAdd= "std"
        virtioAdd = "false"
        hypervAdd = "tcg"
        coresAdd="1"
        threadsAdd="1"
    
    elif archinput == "6": 
        
        archAdd = "PPC64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) power9_v2.1")
        print("2) power10_v2.0")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'power9_v2.1'
        elif cpuinput == "2":
            cpuAdd = 'power10_v2.0'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='power10_v2.0'
        
        vgaAdd = "std"
        virtioAdd = "false"
        hypervAdd = "tcg"
        coresAdd="1"
        threadsAdd="1"

    else:
        print("Wrong Value (Set Default to '2')")
        archAdd="x86_64"

elif osinput == "4": 
    
    osAdd="Other"

    print("Choose the Archeticture (Type the Number)>")   
    print("1) x86")
    print("2) x86_64")
    print("3) ARM")
    print("4) AARCH64")
    print("5) PPC")
    print("6) PPC64")
    
    archinput = input ("")
    
    if archinput == "1": 
        
        archAdd = "x86"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) coreduo")
        print("2) pentium")
        print("3) pentium2")
        print("4) pentium3")
        print("5) qemu32")
        
        cpuinput = input ("")
        
        if cpuinput == "1":
            cpuAdd = 'coreduo'
        elif cpuinput == "2":
            cpuAdd = 'pentium'
        elif cpuinput == "3":
            cpuAdd = 'pentium2'
        elif cpuinput == "4":
            cpuAdd = 'pentium3'
        elif cpuinput == "5":
            cpuAdd = 'qemu32'
        else:
            print("Wrong Value (Choosing Default '1')")
            cpuAdd='coreduo'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'

    
    elif archinput == "2":
        
        archAdd = "x86_64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) Core 2 Duo")
        print("2) Intel Haswell")
        print("3) qemu64")
        print("4) max")
        print("5) EPYC")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'core2duo'
        elif cpuinput == "2":
            cpuAdd = 'Haswell'
        elif cpuinput == "3":
            cpuAdd = 'qemu64'
        elif cpuinput == "4":
            cpuAdd = 'max'
            cpuAdd = 'epyc'
        else:
            print("Wrong Value (Choosing Default '4')")
            cpuAdd='max'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'

        print("Choose the GPU Model (Type the Number)>")   
        print("1) Cirrus")
        print("2) std")
        print("3) Vmware S-VGA")
        print('4) QXL')
        print('5) Virtio')

        vgainput = input ("")
        
        if vgainput == "1":
            vgaAdd = 'cirrus'
        elif vgainput == "2":
            vgaAdd = 'std'
        elif vgainput == "3":
            vgaAdd = 'vmware'
        elif vgainput == "4":
            vgaAdd = 'qxl'
        elif vgainput == "5":
            vgaAdd = 'virtio'
        else:
            print("Wrong Value (Choosing Default '2')")
            vgadd='std'
        
        print("What Acceleration Do You Want to Use? (Type the Number)>")   
        print("1) TCG")
        print("2) QEMU/KVM (Coming Soon)")
        print("3) Hyper-V")
        
        hypervinput = input ("")

        if hypervinput == "1":
            hypervAdd = 'tcg'
        elif hypervinput == "3":
            hypervAdd = 'whpx'
        else:
            print("Wrong Value (Choosing Default '2')")
            hypervAdd='whpx'

        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
    
    elif archinput == "3": 
        
        archAdd = "ARM"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='cortex-a57'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'

        vgaAdd = "virtio"
        hypervAdd ="tcg"
    
    elif archinput == "4": 
        
        archAdd = "ARM64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) cortex-a53")
        print("2) cortex-a57")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'cortex-a53'
        elif cpuinput == "2":
            cpuAdd = 'cortex-a57'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='cortex-a57'
        
        coresAdd = input("Type the Numbers of CPU Cores> ")
        print("Is Your CPU ")
        print("1) Single Threaded")
        print("2) Multi Threaded")
        threadsinput = input("")
        
        if threadsinput == "1":
            threadsAdd = "1"
        elif threadsinput == "2":
            threadsAdd = "2"
        else:
            print("Wrong Value (Choosing Default '1')")
            threadsAdd='1'
        
        print("Do You Want to Enable Virtio? (Type the Number)>")   
        print("1) Yes")
        print("2) No")
        
        virtioinput = input ("")

        if virtioinput == "1":
            virtioAdd = 'true'
        elif virtioinput == "2":
            virtioAdd = 'false'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='false'
        
        vgaAdd = "virtio"
        hypervAdd = "tcg"
    
    elif archinput == "5": 
        
        archAdd = "PPC"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) G3")
        print("2) G4")
        
        cpuinput = input ("")

        if cpuinput == "1":
            cpuAdd = 'g3'
        elif cpuinput == "2":
            cpuAdd = 'g4'
        else:
            print("Wrong Value (Choosing Default '2')")
            cpuAdd='g4'
        
        vgaAdd = "std"
        virtioAdd = "false"
        hypervAdd = "tcg"
        coresAdd="1"
        threadsAdd="1"
    
    elif archinput == "6": 
        
        archAdd = "PPC64"
        
        print("Choose the CPU Model (Type the Number)>")   
        print("1) power9_v2.1")
        print("2) power10_v2.0")
        
        cpuinput = input ("")
        
        if cpuinput == "1":
            cpuAdd = 'power9_v2.1'
        elif cpuinput == "2":
            cpuAdd = 'power10_v2.0'
        else:
            print("Wrong Value (Choosing Default 21')")
            cpuAdd='power10_v2.0'

        vgaAdd = "std"
        virtioAdd = "false"
        hypervAdd = "tcg"
        coresAdd="1"
        threadsAdd="1"

    else:
        print("Wrong Value (Set Default to '2')")
        archAdd="x86_64"
    
else:
    print("Wrong Value (Please Restart Operation)")
    quit()

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

iconAdd = input ("Type here the Path of the Icon you Want to Use> ")
if iconAdd == "":
    iconAdd = "Textures/roms-icons/other.png"

print("")
addRom()
print("Congratulation, Everything is Done")
print("Press Enter to Exit")
input()

   
    # Load existing data from the JSON file
try:
    with open('roms.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []