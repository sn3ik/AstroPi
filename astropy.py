import csv
import sys
import os

def main():
    print()
    print("*******************************************")
    print("*                                         *")
    print("*            AstroPi Installer            *")
    print("*                                         *")
    print("*******************************************")


    choice = input("""
       A: Installazione automatica
       M: Installazione manuale
       H: Hotspot
       Q: Esci

       Digita la tua scelta: """)

    if choice == "A" or choice =="a":
        automatic()
    elif choice == "M" or choice =="m":
        manual()
    elif choice == "H" or choice =="h":
        hotspot()    
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("Opzione non valida")
        print("Riprova")
        menu()

def automatic():
    print()
    print("Verranno scaricate ed installate le librerie necessarie e i seguenti software:")
    print()
    print("INDI - KSTARS/EKOS - PHD2")
    print("fxload - libXISF - indi-3rdparty - stellarsolver")
    print()
    print("libnova-dev libcfitsio-dev libusb-1.0-0-dev zlib1g-dev libgsl-dev build-essential cmake git libjpeg-dev libcurl4-gnutls-dev libtiff-dev libfftw3-dev libftdi-dev libgps-dev libraw-dev libdc1394-dev libgphoto2-dev libboost-dev libboost-regex-dev librtlsdr-dev liblimesuite-dev libftdi1-dev libavcodec-dev libavdevice-dev libeigen3-dev extra-cmake-modules libkf5plotting-dev libqt5svg5-dev libkf5xmlgui-dev libkf5kio-dev kinit-dev libkf5newstuff-dev libkf5doctools-dev libkf5notifications-dev qtdeclarative5-dev libkf5crash-dev gettext libkf5notifyconfig-dev wcslib-dev libqt5websockets5-dev xplanet xplanet-images qt5keychain-dev libsecret-1-dev breeze-icon-theme qml-module-qtquick-controls pkg-config libev-dev libqt5datavisualization5-dev libzmq3-dev libzstd-dev")
    print()
    choice = input("""
        Premere S per continuare N per uscire: """)
        
    if choice=="S" or choice=="s":
        dependencies()

        #if not os.path.exists("AstroPi"):
        #    os.system("mkdir AstroPi")
        #    os.chdir("AstroPi")
        
        fxload()
        indi()
        indi3rdparty()
        stellarsolver()
        kstars()
        phd2()
        menu()

    else:
        sys.exit
pass
    
def manual():
    
    #if not os.path.exists("AstroPi"):
    #    os.system("mkdir AstroPi")
    #    os.chdir("AstroPi")
    print()
    print("Software disponibili:")
    choice = input("""
       0: Librerie mancanti
       1: Fxload
       2: INDI
       3: INDI 3dparty
       4: Stellarsolver
       5: Kstars - Ekos
       6: PHD2

       Digita la tua scelta: """)
    
    if choice=="0":
        dependencies()
        menu()
    elif choice=="1":
        fxload()
        menu()
    elif choice=="2":
        indi()
        menu()
    elif choice=="3":
        indi3rdparty()
        menu()
    elif choice=="4":
        stellarsolver()
        menu()
    elif choice=="5":
        kstars()
        menu()
    elif choice=="6":
        phd2()
        menu()
    else:
        menu()
   
pass
    
def hotspot():
    print()
    print("La modalità hotspot trasforma questo dispositivo in un Access Point Wi-Fi")
    choice = input("""
       A: Abilita 
       D: Disabilita
       Q: Esci

       Digita la tua scelta: """)
    
    if choice == "A" or choice =="a":
        hotspot_on()
    elif choice == "D" or choice =="d":
        hotspot_off()
    else:
        sys.exit

pass

def dependencies():
    os.system("sudo apt update && sudo apt upgrade")
    os.system("sudo apt install libnova-dev libcfitsio-dev libusb-1.0-0-dev zlib1g-dev libgsl-dev build-essential cmake git \
        libjpeg-dev libcurl4-gnutls-dev libtiff-dev libfftw3-dev libftdi-dev libgps-dev libraw-dev libdc1394-dev libgphoto2-dev \
        libboost-dev libboost-regex-dev librtlsdr-dev liblimesuite-dev libftdi1-dev libavcodec-dev libavdevice-dev \
        libeigen3-dev extra-cmake-modules libkf5plotting-dev libqt5svg5-dev libkf5xmlgui-dev libkf5kio-dev kinit-dev \
        libkf5newstuff-dev libkf5doctools-dev libkf5notifications-dev qtdeclarative5-dev libkf5crash-dev gettext libkf5notifyconfig-dev \
        wcslib-dev libqt5websockets5-dev xplanet xplanet-images qt5keychain-dev libsecret-1-dev breeze-icon-theme qml-module-qtquick-controls \
        pkg-config libev-dev libqt5datavisualization5-dev libzmq3-dev libzstd-dev ")
        
    print('\033[92m'"Librerire installate con successo'\033[0m'")
pass

def fxload():
    #os.system("wget https://francescocangiani.com/osservatorio/fxload.zip")
    #os.system("unzip fxload.zip")
    os.chdir("fxload")
    os.system("cmake -B build -S . -DCMAKE_INSTALL_PREFIX=/usr || { echo 'fxload compilation failed'; exit 1; }")
    os.system("cmake --build ./build || { echo 'fxload compilation failed'; exit 1; }")
    os.system("sudo cmake --install ./build|| { echo 'fxload compilation failed'; exit 1; } ")
    os.chdir("..")
    print('\033[92m'"fxload installato con successo'\033[0m'")

pass

def libxisf():
    os.system("git clone https://gitea.nouspiro.space/nou/libXISF.git")
    os.chdir("libXISF")
    os.system("git pull origin")
    os.system("cmake -B ../build-libXISF ../libXISF -DCMAKE_BUILD_TYPE=Release || { echo 'LibXISF configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-libXISF")
    os.system("make || { echo 'ISF compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'libXISF installation failed'; exit 1; }")
    os.chdir("..")
    print('\033[92m'"libXISF installato con successo'\033[0m'")
    
pass

def indi():
    os.system("git clone https://github.com/indilib/indi.git")
    os.chdir("indi")
    os.system("git pull origin")
    os.system("cmake -B ../build-indi ../indi -DCMAKE_BUILD_TYPE=Release || { echo 'INDI configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-indi")
    os.system("make || { echo 'INDI compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'INDI installation failed'; exit 1; }")
    os.chdir("..")
    print('\033[92m'"INDI installato con successo'\033[0m'")
    
pass

def indi3rdparty():
    os.system("git clone https://github.com/indilib/indi-3rdparty.git")
    os.chdir("indi-3rdparty")
    os.system("git pull origin")
    os.system("cmake -B ../build-indi-lib ../indi-3rdparty -DCMAKE_BUILD_TYPE=Release || { echo 'INDI 3dparty configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-indi-lib")
    os.system("make || { echo 'INDI 3dparty compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'INDI 3dparty installation failed'; exit 1; }")
    
    os.system("cmake -B ../build-indi-3rdparty ../indi-3rdparty -DCMAKE_BUILD_TYPE=Release || { echo 'INDI 3dparty configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-indi-3rdparty")
    os.system("make || { echo 'INDI 3dparty compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'INDI 3dparty installation failed'; exit 1; }")
    
    print('\033[92m'"INDI 3dparty installato con successo'\033[0m'")
    
pass

def stellarsolver():
    os.system("git clone https://github.com/rlancaste/stellarsolver.git")
    os.chdir("stellarsolver")
    os.system("git pull origin")
    os.system("cmake -B ../build-stellarsolver ../stellarsolver -DCMAKE_BUILD_TYPE=Release || { echo 'INDI configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-stellarsolver")
    os.system("make || { echo 'Stellarsolver compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'Stellarsolver installation failed'; exit 1; }")
    os.chdir("..")
    print('\033[92m'"Stellarsolver installato con successo'\033[0m'")
    
pass

def kstars():
    os.system("git clone https://invent.kde.org/education/kstars.git")
    os.chdir("kstars")
    os.system("git pull origin")
    os.system("cmake -B ../build-kstars ../kstars -DCMAKE_BUILD_TYPE=Release || { echo 'Kstars configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-kstars")
    os.system("make || { echo 'Kstars compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'Kstars installation failed'; exit 1; }")
    os.chdir("..")
    print('\033[92m'"Kstars installato con successo'\033[0m'")
    
pass

def phd2():
    os.system("sudo apt-get install build-essential subversion cmake pkg-config libwxgtk3.0-gtk3-dev wx-common wx3.0-i18n libindi-dev libnova-dev zlib1g-dev")
    os.system("git clone https://github.com/OpenPHDGuiding/phd2.git")
    os.chdir("phd2")
    os.system("cmake -B ../build-phd2 ../phd2 -DCMAKE_BUILD_TYPE=Release || { echo 'PHD2 configuration failed'; exit 1; }")
    os.chdir("..")
    os.chdir("build-phd2")
    os.system("make || { echo 'PHD2 compilation failed'; exit 1; }")
    os.system("sudo make install || { echo 'PHD2 installation failed'; exit 1; }")
    os.chdir("..")
    print('\033[92m'"PHD2 installato con successo'\033[0m'")
    
pass
    
#the program is initiated, so to speak, here
main()