#!/bin/sh

cd ~
mv dotfiles/.config/qtile .config/qtile
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
chsh -s $(whoami) /bin/zsh
sudo -s /bin/zsh
rm -r dotfiles
