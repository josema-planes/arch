#!/bin/sh

# color variables
RE='\033[1;31m'
YE='\033[1;33m'
PU='\033[1;35m'
NC='\033[0m'

echo -e "${YE}Setting up qtile and zsh config${NC}"

# Installing necessary pakages------------------------------------------
echo -e "${YE}Installing necessary pakages...${NC}"
sleep 1
sudo pacman -S --noconfirm thunar nitrogen dmenu git brightnessctl python-psutil acpi alsa-utils volumeicon cbatticon network-manager-applet geeqie xcb-util-cursor xf86-video-intel xf86-video-nouveau exa gvfs ntfs-3g dunst scrot redshift bc unzip evince zsh
echo -e "${YE}Done${NC}"

# Installing yay--------------------------------------------------------
if [ ! -d ~/yay ]; then
    echo -e "${PU}Installing yay...${NC}"
    sleep 1
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -sic --noconfirm
    cd ~
    echo -e "${YE}Done${NC}"
else
    break
fi

# Installing yay pakages------------------------------------------------
cmd=`pacman -Qqm`
if [[ $cmd != *vscodium-bin* ]]; then
    echo -e "${YE}Installing yay pakages...${NC}"
    sleep 1
    yay -S --noconfirm vscodium-bin
fi
if [[ $cmd != *nerd-fonts-ubuntu-mono* ]]; then
    yay -S --noconfirm nerd-fonts-ubuntu-mono
fi
if [[ $cmd != *ccat* ]]; then
    yay -S --noconfirm ccat
fi

# Cloning repository and moving files
echo -e "${YE}Cloning repository...${NC}"
git clone https://github.com/josemapt/dotfiles.git

echo -e "${YE}Relocating files...${NC}"
sleep 1
mv -f dotfiles/.config/qtile/* .config/qtile
chmod +x .config/qtile/autostart.sh
mv dotfiles/.config/* .config

# Neovim plugins installation
if [ ! -f ~/.local/share/nvim/site/autoload/plug.vim ]; then
    curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    nvim -c 'PlugInstall --sync' +qa
else
    break
fi
#----------------------------

mv dotfiles/.local/bin .local
chmod +x .local/bin/*
mv dotfiles/.zsh_config ~
mv dotfiles/scripts ~
chmod +x scripts/*
mv dotfiles/zsh-autosuggestions ~
mv dotfiles/zsh-syntax-highlighting ~
mv dotfiles/.bashrc ~
mv dotfiles/.xinitrc ~
mv dotfiles/.zshrc ~
rm -rf dotfiles
echo -e "${YE}Done${NC}"

# Creating gtk3 config file
if [ ! -d ~/.config/gtk-3.0 ]; then
    mkdir .config/gtk-3.0
    touch .config/gtk-3.0/settings.ini
    echo "[Settings]" >> .config/gtk-3.0/settings.ini
else
    if [ ! -f ~/.config/gtk-3.0/settings.ini ]; then
        touch .config/gtk-3.0/settings.ini
        echo "[Settings]" >> .config/gtk-3.0/settings.ini
    else
        break
    fi
fi
#--------------------------

#Installing extra pakages
echo -e -n "${PU}Do you want to install the Marwaita theme and the Tela icon theme (y/n)?${NC}"
read a1

if [ "${a1}" = "y" ] || [ "${a1}" = "" ]; then
    echo -e -n "${RE}Make sure you have downloaded them from ${PU}https://www.gnome-look.org/p/1239855/ ${RE}(Marwaita) and ${PU}https://www.gnome-look.org/p/1279924/ ${RE}(Tela icon theme) and then press ${PU}enter${NC}"
    read any1
    if [ -f ~/Downloads/01-Tela.tar.xz ] && [ -f ~/Downloads/Marwaita.tar.xz ]; then
        echo -e "${YE}Installing the Marwaita theme and the Tela icon theme...${NC} "
        sleep 1
        cd Downloads/

        tar -xf 01-Tela.tar.xz
        rm 01-Tela.tar.xz
        sudo mv Tela /usr/share/icons/
        sudo mv Tela-dark/ /usr/share/icons/

        tar -xf Marwaita.tar.xz
        rm Marwaita.tar.xz
        sudo mv Marwaita /usr/share/themes/
        sudo mv Marwaita\ Dark/ /usr/share/themes/
        sudo mv Marwaita\ Light/ /usr/share/themes/

        cd ~

        echo "gtk-icon-theme-name = Tela" >> .config/gtk-3.0/settings.ini
        echo "gtk-theme-name = Marwaita Dark" >> .config/gtk-3.0/settings.ini

        echo -e "${YE}Done${NC}"
    else
        echo -e "${RE}Files haven't been found${NC}"
        break
    fi

else
    break
fi


echo -e -n "${PU}Do you want to install he Breeze cursor theme (y/n)?${NC}"
read a2

if [ "${a2}" = "" ] || [ "${a2}" = "y" ]; then
    echo -e -n "${RE}Make sure that you have downloaded it from ${PU}https://www.gnome-look.org/p/999927/ ${RE} and then press ${PU}enter${NC}"
    read any2
    
    if [ -f ~/Downloads/165371-Breeze.tar.gz ]; then
        echo -n -e "${PU}Installing the Breeze cursor theme...${NC} "
        sleep 1

        cd Downloads
        tar -xf 165371-Breeze.tar.gz
        rm 165371-Breeze.tar.gz
        sudo mv Breeze /usr/share/icons

        cd ~
        echo "gtk-cursor-theme-name = Breeze" >> .config/gk-3.0/settings.ini

        sudo sed -i 's/Adwaita/Breeze/g' /usr/share/icons/default/index.theme
        echo -e "${YE}Done${NC}"

    else
        echo -e "${RE}Files haven't been found${NC}"
        break
    fi
else
    break
fi


echo -e -n "${PU}Do you want to install he Vimix grub theme (y/n)?${NC}"
read a3

if [ "${a3}" = "" ] || [ "${a3}" = "y" ]; then
    echo -e -n "${RE}Make sure that you have downloaded it from ${PU}https://www.gnome-look.org/p/1009236/ ${RE}and then press ${PU}enter${NC}"
    read any3

    if [ -f ~/Downloads/Vimix-1080p.tar.xz ]; then
        echo -e "${PU}Installing the Vimix grub theme...${NC} "
    
        cd Downloads

        tar -xf Vimix-1080p.tar.xz
        rm Vimix-1080p.tar.xz
        sudo mv Vimix-1080p/Vimix/ /boot/grub/themes/
        rm -r Vimix-1080p

        sudo chmod 777 /etc/default/grub
        echo "GRUB_THEME='/boot/grub/themes/Vimix/theme.txt'" >> /etc/default/grub
        sudo chmod 644 /etc/default/grub

        sudo grub-mkconfig -o /boot/grub/grub.cfg

        echo -e "${YE}Done${NC}"
    
    else
        echo -e "${RE}Files haven't been found${NC}"
        break
    fi

else
    break
fi


echo -e -n "${YE}Setting up completed. Press ${PU}enter ${YE}to reboot now${NC} "
read a0

if [ "${a0}" = "" ]; then
    reboot
else
    break
fi
