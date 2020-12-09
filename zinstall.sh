#!/bin/sh

YE='\033[0;33m'
PU='\033[0;35m'
NC='\033[0m'

echo -e "${YE}Setting up qtile and zsh config${NC}"

echo -e "${YE}Installing necessary pakages...${NC}"
sleep 1
sudo pacman -S --noconfirm thunar nitrogen dmenu git brightnessctl python-psutil acpi alsa-utils volumeicon cbatticon network-manager-applet geeqie xcb-util-cursor xf86-video-intel xf86-video-nouveau exa gvfs ntfs-3g dunst scrot redshift bc unzip evince zsh
echo "${YE}Done${NC}"

echo -n -e "${PU}Do you want to install yay (Y/n)?${NC} "
read answer1
if [ "$answer1" = "y" ] || [ "$answer1" = "" ] ;then
    echo "Installing yay..."
    sleep 1
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si
    cd ~
    echo "Done"
    echo "Installing yay pakages..."
    sleep 1
    yay -S --noconfirm vscodium-bin nerd-fonts-ubuntu-mono ccat
fi

echo "${YE}Cloning repository...${NC}"
git clone https://github.com/josemapt/dotfiles.git

echo "${YE}Relocating files...${NC}"
sleep 1
cd ~
mv -f dotfiles/.config/qtile/* .config/qtile
chmod +x .config/qtile/autostart.sh
mv dotfiles/.config/* .config

curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

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

echo -n -e "${PU}Do you want to install the Breeze cursor theme (needed to be downloaded first) (Y/n)?${NC} "
read answer2

if [ "$answer2" = "y" ] || [ "$answer1" = "" ] ;then
    cd Downloads/
    ex 165371-Breeze.tar.gz
    rm 165371-Breeze.tar.gz
    sudo mv Breeze /usr/share/icons
    
    cd ~
    mkdir .config/gtk-3.0
    touch .config/gtk-3.0/settings.ini
    echo "[Settings]" >> .config/gtk-3.0/settings.ini
    echo "gtk-cursor-theme-name = Breeze" >> .config/gtk-3.0/settings.ini
    
    sudo sed -i 's/Adwaita/Breeze/g' /usr/share/icons/default/index.theme
fi

#echo -n -e "${PU}Do you want to set zsh as default shell (Y/n)?${NC} "
#read answer3

#if [ "$answer3" = "y" ] || [ "$answer1" = "" ] ;then
#    chsh -s /bin/zsh $(whoami)
#    sudo -s /bin/zsh
#fi


echo -n -e "${YE}Setting up completed. ${PU}Do you want to reboot now (Y/n)?${NC} "
read answer10

if [ "$answer10" = "y" ] || [ "$answer1" = "" ] ;then
    reboot
fi
