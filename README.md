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
sudo pacman -S thunar nitrogen python dmenu brightnessctl git alsa-utils python-psutil acpi dunst exa unzip volumeicon cbatticon network-manager-applet udiskie ntfs-3g glib2 gvfs geeqie libreoffice
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
