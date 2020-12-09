#!/bin/sh

YE='\033[0;33m'
PU='\033[0;35m'
NC='\033[0m'

echo -e "${YE}Setting up qtile and zsh config${NC}"

echo -e "${YE}Installing necessary pakages...${NC}"
sleep 1
sudo pacman -S --noconfirm thunar nitrogen dmenu git brightnessctl python-psutil acpi alsa-utils volumeicon cbatticon network-manager-applet geeqie xcb-util-cursor xf86-video-intel xf86-video-nouveau exa gvfs ntfs-3g dunst scrot redshift bc unzip evince zsh
echo -e "${YE}Done${NC}"

echo -e "${PU}Installing yay...${NC}"
sleep 1
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ~
echo -e "${YE}Done${NC}"
echo -e "${YE}Installing yay pakages...${NC}"
sleep 1
yay -S --noconfirm vscodium-bin nerd-fonts-ubuntu-mono ccat

echo -e "${YE}Cloning repository...${NC}"
git clone https://github.com/josemapt/dotfiles.git

echo -e "${YE}Relocating files...${NC}"
sleep 1
cd ~
mv -f dotfiles/.config/qtile/* .config/qtile
chmod +x .config/qtile/autostart.sh
mv dotfiles/.config/* .config

curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

nvim -c 'PlugInstall --sync' +qa

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
echo -e "${YE}Done${NC}"

mkdir .config/gtk-3.0
touch .config/gtk-3.0/settings.ini
echo "[Settings]" >> .config/gtk-3.0/settings.ini

echo -n -e "${PU}Installing the Marwaita theme and the Tela icon theme...{NC} "
sleep 1

curl -O "https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2MDY0ODc4OTkiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjEyNGM5NTBiMTBhODdlZjIzNzQ1ODNlNzg0NTg5NDllMGRjMDljZmY5MjkwNDJlMWNkMjg0Yjg1ODVkZTU2ODFhOTQ2YTEyMDYwNmI3N2QxMTE0MjY2NTA0NmU2MmQyZmQ5NzYwYjRmZWIyZGJhMDdkN2NiMzczM2E1YzU0ODVlIiwidCI6MTYwNzUyOTM5NSwic3RmcCI6IjBmZGZmZmU0NDEwOGU2YzZiNGNhODAzM2EzNDNkZTI5Iiwic3RpcCI6IjE4OC43OS42NS4xMDgifQ.cWKIUlIt7Y-1BBrQwl6PdDEzAY-sHs77b6fesmagPXg/01-Tela.tar.xz"
curl -O "https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2MDUzNTE5MjUiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjQ4MTljYjlmZDAwODkwNDQ3OTA1NWY3MjZiZjFmNDBkZDkwOTNjNWMxNWQ0M2ZhZjliNWU3NjI0ZmNkNjUwNGFhZTEzNTA1MjQ0OGUyMmNjZjBiN2MyNDQ5ODlmMWQxOTZhZGJmMjRlMjVkY2MzNmU0MDU4Yzk2ODZjOWVlZDhkIiwidCI6MTYwNzUyNjgzNSwic3RmcCI6IjBmZGZmZmU0NDEwOGU2YzZiNGNhODAzM2EzNDNkZTI5Iiwic3RpcCI6IjE4OC43OS42NS4xMDgifQ.-CHpmosiBNX2q7JEZE1bQxwNtJvJczUHkOal3NgMqGM/Marwaita.tar.xz"

tar -xf 01-Tela.tar.xz
rm 01-Tela.tar.xz
sudo mv Tela /usr/share/icons/
sudo mv Tela-dark/ /usr/share/icons/

tar -xf Marwaita.tar.xz
rm Marwaita.tar.xz
sudo mv Marwaita /usr/share/themes/
sudo mv Marwaita\ Dark/ /usr/share/themes/
sudo mv Marwaita\ Light/ /usr/share/themes/

echo "gtk-icon-theme-name = Tela" >> .config/gtk-3.0/settings.ini
echo "gtk-theme-name = Marwaita Dark" >> .config/gtk-3.0/settings.ini

echo -e "${YE}Done${NC}"


echo -n -e "${PU}Installing the Breeze cursor theme...${NC} "
sleep 1

curl -O "https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE0NjA3MzUyNjkiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6ImZmYTc5OWRmNzUwYmQ5MzM3ZDA5ZGNiOTEzYTFjNzRlZDY5M2MxNTJkM2ZjMzJhYzZlNmYxNTgwOWJlZmJjMjc5MmMyNTg0ZTY2OTg3ODcwOGI0MWMzYzE4ZjMzN2RkMTU2ZDE3NzdkYTBjM2Y0YmQ4YzZjNzE3MzM3YTRiZTc0IiwidCI6MTYwNzUyNjE4NCwic3RmcCI6IjUzZmVmYTE0YTM0ZTIyZjVkNmM0N2U5YjI0ZDE3NGU1Iiwic3RpcCI6IjE4OC43OS42NS4xMDgifQ.3ROKH6C9yEk4d-SjoUqe8tCa03X-zWHzzgnibkpeOIc/165371-Breeze.tar.gz"

tar -xf 165371-Breeze.tar.gz
rm 165371-Breeze.tar.gz
sudo mv Breeze /usr/share/icons

echo "gtk-cursor-theme-name = Breeze" >> .config/gtk-3.0/settings.ini

sudo sed -i 's/Adwaita/Breeze/g' /usr/share/icons/default/index.theme
echo -e "${YE}Done${NC}"


echo -n -e "${PU}Installing the Vimix grub theme...${NC} "

curl -O "https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1NzIyNTAzOTIiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjNkYWVhMzExNzIxYTViYzIzMWRjMjJiM2IyNjFkNzBkODU0OGVkNjRkNzg1MDc2ZDlmZDhhNjU5ZjgyM2M5YmYzOTA0ZTcwMWM0YTMxNWNkNTI5OWMwNTZhMmVlNjJmNzMzNjc1NGFiOGUzOGE4YTE5ZjUwZjFjYjkyYWY1YmI1IiwidCI6MTYwNzUyOTc2MCwic3RmcCI6IjBmZGZmZmU0NDEwOGU2YzZiNGNhODAzM2EzNDNkZTI5Iiwic3RpcCI6IjE4OC43OS42NS4xMDgifQ.8hcG5V6BSShxQAj6MoO8dJre5Pe0hHVsrS0_87QQWlo/Vimix-1080p.tar.xz"

tar -xf Vimix-1080p.tar.xz
rm Vimix-1080p.tar.xz
sudo mv Vimix-1080p /boot/grub/themes

sudo chmod 777 /etc/default/grub
echo "GRUB_THEME='/boot/grub/themes/Vimix-1080p/Vimix/theme.txt'" >> /etc/default/grub
sudo chmod 644 /etc/default/grub

sudo grub-mkconfig -o /boot/grub/grub.cfg

echo -e "${YE}Done${NC}"


echo -e "${YE}Setting up completed. Rebooting...${NC} "
sleep 1
reboot
