# dotfiles

# Base pakages:

```
base base-devel linux linux-firmware neovim intel-ucode networkmanager
```


# Pakages to download first:
```
sudo pacman -S xorg xorg-server xorg-xinit qtile firefox alacritty
```
Then start qtile and copy the rest.

# Rest of pakages:
```
sudo pacman -S thunar nitrogen python dmenu brightnessctl git alsa-utils python-psutil acpi dunst exa unzip volumeicon cbatticon network-manager-applet udiskie ntfs-3g glib2 gvfs geeqie libreoffice xcb-util-cursor
```

# Installing yay.
```
git clone https://aur.archlinux.org/yay-git.git

cd yay

makepkg -si
```

# Whith yay:
```
yay -S visual-studio-code-bin nerd-fonts-ubuntu-mono ccat
```

# Cange GTK theme:
Download any theme in https://www.gnome-look.org/browse/cat/135/ord/rating/ and run:
```
cd Downloads/
tar -xf THEME.tar.gz
sudo mv THEME /usr/share/themes
```
Download the breeze cursor theme in https://www.gnome-look.org/p/999927/ and run:
```
cd Downloads/
tar -xf 165371-Breeze.tar.gz
rm 165371-Breeze.tar.gz
sudo mv Breeze /usr/share/icons
```
Now edit ~/.config/gtk-3.0/settings.ini by adding these lines:
```
[Settings]
gtk-icon-theme-name = ICON THEME
gtk-theme-name = THEME
gtk-cursor-theme-name = CURSOR THEME
```
And edit /usr/share/icons/default/index.theme:
```
[Icon Theme]
Inherits=Breeze
```
And reboot
