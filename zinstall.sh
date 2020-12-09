#!/bin/sh

echo "\033[0;33mSetting up qtile and zsh config\033[0m"

echo "\033[0;33mInstalling necessary pakages\033[0m"
sudo pacman -S thunar nitrogen dmenu git brightnessctl python-psutil acpi alsa-utils volumeicon cbatticon network-manager-applet geeqie xcb-util-cursor xf86-video-intel xf86-video-nouveau exa gvfs ntfs-3g dunst scrot redshift bc unzip evince zsh
echo "\033[0;33mDone\033[0m"

echo "\033[0;33mInstalling yay\033[0m"
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ~
echo "\033[0;33mDone\033[0m"

echo "\033[0;33mCloning repository\033[0m"
git clone https://github.com/josemapt/dotfiles.git

echo "\033[0;33mRelocating files\033[0m"
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
chsh -s /bin/zsh $(whoami)
sudo -s /bin/zsh
rm -r dotfiles
echo "\033[0;33mDone\033[0m"

echo -n "Setting up complete. Do you want to reboot now (y/n)? "
read answer

if [ "$answer" = "y" ] ;then
    reboot
fi
