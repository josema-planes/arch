#!/bin/sh

YE='\033[0;33m'
PU='\033[0;35m'
NC='\033[0m'

echo -e "${YE}Setting up qtile and zsh config${NC}"

echo -e "${YE}Installing necessary pakages${NC}"
sudo pacman -S --noconfirm thunar nitrogen dmenu git brightnessctl python-psutil acpi alsa-utils volumeicon cbatticon network-manager-applet geeqie xcb-util-cursor xf86-video-intel xf86-video-nouveau exa gvfs ntfs-3g dunst scrot redshift bc unzip evince zsh
echo "${YE}Done${NC}"

echo -n -e "${PU}Do you want to install yay (y/n)${NC}? "
read answer1
if [ "$answer1" = "y" ] ;then
    echo "${YE}Installing yay${NC}"
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si
    cd ~
    echo "${YE}Done${NC}"
    
    echo "${YE}Installing yay pakages${NC}"
    yay -S --noconfirm vscodium-bin nerd-fonts-ubuntu-mono ccat
fi

echo "${YE}Cloning repository${NC}"
git clone https://github.com/josemapt/dotfiles.git

echo "${YE}Relocating files${NC}"
cd ~
mv -f dotfiles/.config/qtile/* .config/qtile
chmod +x .config/qtile/autostart.sh
mv dotfiles/.config/* .config
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
rm -r dotfiles
echo "${YE}Done${NC}"

echo -n -e "${PU}Do you want to install the Breeze cursor theme (needed to be downloaded first) (y/n)?${NC} "
read answer2

if [ "$answer2" = "y" ] ;then
    cd Downloads/
    ex 165371-Breeze.tar.gz
    rm 165371-Breeze.tar.gz
    sudo mv Breeze /usr/share/icons
    
    touch .config/gtk-3.0/settings.ini
    echo "[Settings]" >> .config/gtk-3.0/settings.ini
    echo "gtk-cursor-theme-name = Breeze" >> .config/gtk-3.0/settings.ini
    
    sudo sed 'Inherits=Adwaita' /usr/share/icons/default/index.theme
    sudo echo "Inherits=Breeze" >> /usr/share/icons/default/index.theme
fi

echo -n -e "${PU}Do you want to set zsh as default shell (y/n)?${NC} "
read answer3

if [ "$answer3" = "y" ] ;then
    chsh -s /bin/zsh $(whoami)
    sudo -s /bin/zsh
fi


echo -n -e "${YE}Setting up complete. ${PU}Do you want to reboot now (y/n)?${NC} "
read answer10

if [ "$answer10" = "y" ] ;then
    reboot
fi
